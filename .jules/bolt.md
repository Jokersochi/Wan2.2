## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-03-24 - PyTorch Chunk to Unbind Optimization
**Learning:** Using `.chunk(N, dim=D)` followed by indexing and `.squeeze(D)` causes intermediate tensor allocations and multiple Python squeeze operations.
**Action:** Replace `.chunk(N, dim=D)` and subsequent `.squeeze(D)` with `.unbind(dim=D)`, which returns a tuple of tensors directly, eliminating the specified dimension and bypassing Python overhead. Note: strictly ensure the squeeze matches the unbind dimension to prevent functional shape regressions.
