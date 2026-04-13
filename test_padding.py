import torch
import time

def test_padding():
    u = torch.randn(1, 1024, 1024).cuda()
    seq_len = 1024

    # warmup
    for _ in range(100):
        x = torch.cat([u, u.new_zeros(1, seq_len - u.size(1), u.size(2))], dim=1)
        y = torch.cat([u, u.new_zeros(1, seq_len - u.size(1), u.size(2))], dim=1) if seq_len > u.size(1) else u

    torch.cuda.synchronize()
    t0 = time.time()
    for _ in range(1000):
        x = torch.cat([u, u.new_zeros(1, seq_len - u.size(1), u.size(2))], dim=1)
    torch.cuda.synchronize()
    t1 = time.time()

    torch.cuda.synchronize()
    t2 = time.time()
    for _ in range(1000):
        y = torch.cat([u, u.new_zeros(1, seq_len - u.size(1), u.size(2))], dim=1) if seq_len > u.size(1) else u
    torch.cuda.synchronize()
    t3 = time.time()

    print(f"Without optimization: {t1 - t0:.5f}s")
    print(f"With optimization: {t3 - t2:.5f}s")

if __name__ == "__main__":
    if torch.cuda.is_available():
        test_padding()
    else:
        print("CUDA not available")
