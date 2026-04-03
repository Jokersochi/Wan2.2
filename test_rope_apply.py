import sys
# Real modules we just installed
import torch

# Simply avoid importing wan, just extract rope functions to verify memory constraint idea.

def sinusoidal_embedding_1d(dim, position):
    # preprocess
    assert dim % 2 == 0
    half = dim // 2
    position = position.type(torch.float64)

    # calculation
    sinusoid = torch.outer(
        position, torch.pow(10000, -torch.arange(half).to(position).div(half)))
    x = torch.cat([torch.cos(sinusoid), torch.sin(sinusoid)], dim=1)
    return x

@torch.amp.autocast('cuda', enabled=False)
def rope_params(max_seq_len, dim, theta=10000):
    assert dim % 2 == 0
    freqs = torch.outer(
        torch.arange(max_seq_len),
        1.0 / torch.pow(theta,
                        torch.arange(0, dim, 2).to(torch.float64).div(dim)))
    freqs = torch.polar(torch.ones_like(freqs), freqs)
    return freqs

@torch.amp.autocast('cuda', enabled=False)
def rope_apply(x, grid_sizes, freqs):
    n, c = x.size(2), x.size(3) // 2

    # split freqs
    freqs = freqs.split([c - 2 * (c // 3), c // 3, c // 3], dim=1)

    # loop over samples
    output = []
    for i, (f, h, w) in enumerate(grid_sizes.tolist()):
        seq_len = f * h * w

        # precompute multipliers
        x_i = torch.view_as_complex(x[i, :seq_len].to(torch.float64).reshape(
            seq_len, n, -1, 2))
        freqs_i = torch.cat([
            freqs[0][:f].view(f, 1, 1, -1).expand(f, h, w, -1),
            freqs[1][:h].view(1, h, 1, -1).expand(f, h, w, -1),
            freqs[2][:w].view(1, 1, w, -1).expand(f, h, w, -1)
        ],
                            dim=-1).reshape(seq_len, 1, -1)

        # apply rotary embedding
        x_i = torch.view_as_real(x_i * freqs_i).flatten(2)
        x_i = torch.cat([x_i, x[i, seq_len:]])

        # append to collection
        output.append(x_i)
    return torch.stack(output).float()

def rope_apply_optimized(x, grid_sizes, freqs):
    n, c = x.size(2), x.size(3) // 2

    # split freqs
    freqs = freqs.split([c - 2 * (c // 3), c // 3, c // 3], dim=1)

    # loop over samples
    output = []
    for i, (f, h, w) in enumerate(grid_sizes.tolist()):
        seq_len = f * h * w

        # precompute multipliers
        x_i = torch.view_as_complex(x[i, :seq_len].to(torch.float64).reshape(
            seq_len, n, -1, 2))
        freqs_i = torch.cat([
            freqs[0][:f].view(f, 1, 1, -1).expand(f, h, w, -1),
            freqs[1][:h].view(1, h, 1, -1).expand(f, h, w, -1),
            freqs[2][:w].view(1, 1, w, -1).expand(f, h, w, -1)
        ],
                            dim=-1).reshape(seq_len, 1, -1)

        # apply rotary embedding
        x_i = torch.view_as_real(x_i * freqs_i).flatten(2)

        # KEY OPTIMIZATION HERE:
        if seq_len < x.size(1):
            x_i = torch.cat([x_i, x[i, seq_len:]])

        # append to collection
        output.append(x_i)
    return torch.stack(output).float()

def benchmark_rope():
    torch.manual_seed(0)
    b, s, n, d = 2, 4096, 16, 64
    x = torch.randn(b, s, n, d)

    grid_sizes = torch.tensor([[16, 16, 16], [16, 16, 16]]) # 16*16*16 = 4096 = s
    freqs = torch.cat([
        rope_params(4096, d - 4 * (d // 6)),
        rope_params(4096, 2 * (d // 6)),
        rope_params(4096, 2 * (d // 6))
    ], dim=1)

    # Correctness check
    orig_out = rope_apply(x, grid_sizes, freqs)
    opt_out = rope_apply_optimized(x, grid_sizes, freqs)
    print(f"Correctness: {torch.allclose(orig_out, opt_out)}")

    import time

    # Warmup
    for _ in range(5):
        rope_apply(x, grid_sizes, freqs)

    start = time.time()
    for _ in range(100):
        out = rope_apply(x, grid_sizes, freqs)
    end = time.time()
    print(f"Original Time: {end - start:.4f}s")

    start = time.time()
    for _ in range(100):
        out = rope_apply_optimized(x, grid_sizes, freqs)
    end = time.time()
    print(f"Optimized Time: {end - start:.4f}s")

if __name__ == '__main__':
    benchmark_rope()
