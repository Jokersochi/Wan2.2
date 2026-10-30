import torch
import time

def test_chunk_vs_unbind():
    x = torch.randn(10, 64, 512)

    # Method 1: chunk + unpack
    t0 = time.perf_counter()
    for _ in range(10000):
        c1, c2 = x.chunk(2, dim=2)
    t1 = time.perf_counter()

    # Method 2: chunk + squeeze ?

test_chunk_vs_unbind()
