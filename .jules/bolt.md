## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2025-02-23 - Chunk and Squeeze Overhead
**Learning:** In PyTorch, using `.chunk(N, dim=D)` followed by `.squeeze(D)` on the resulting tensors incurs overhead due to multiple calls and allocations. If the size of the dimension `D` matches `N`, they can be replaced by `.unbind(dim=D)`, which automatically splits the tensor and returns views with the dimension removed.
**Action:** Always prefer `.unbind(dim=D)` when unpacking a known dimension size where the dimension should also be removed (equivalent to chunk + squeeze).
