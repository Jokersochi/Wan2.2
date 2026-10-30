import torch
import time

def test():
    # Model dimensions commonly seen in these blocks
    B, L, C = 2, 4096, 2048

    # modulation + e.unsqueeze(2) type tensor
    # shape [B, 6, 1, C] -> chunk(6, dim=1) -> 6 of [B, 1, 1, C]
    # then squeeze(1) or squeeze(2)
    t = torch.randn(B, 6, 1, C).cuda()

    # warmup
    for _ in range(10):
        c = t.chunk(6, dim=1)
        res1 = [x.squeeze(1) for x in c]

    torch.cuda.synchronize()

    # chunk + squeeze
    t0 = time.perf_counter()
    for _ in range(10000):
        c = t.chunk(6, dim=1)
        res1 = [x.squeeze(1) for x in c]
    torch.cuda.synchronize()
    t1 = time.perf_counter()

    # unbind
    t2 = time.perf_counter()
    for _ in range(10000):
        res2 = t.unbind(dim=1)
    torch.cuda.synchronize()
    t3 = time.perf_counter()

    print(f"chunk+squeeze: {t1-t0:.4f}s")
    print(f"unbind:        {t3-t2:.4f}s")

    for r1, r2 in zip(res1, res2):
        assert torch.allclose(r1, r2)
        assert r1.shape == r2.shape

test()
