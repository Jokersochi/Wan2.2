## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## $(date +%Y-%m-%d) - Optimize Tensor Chunking with Unbind
**Learning:** PyTorch `.chunk(N, dim=D)` followed immediately by `.squeeze(D)` and indexing is inefficient. It allocates intermediate chunked tensors that retain the dimension (size 1) before squeezing.
**Action:** Replace `.chunk(N, dim=D)` and subsequent `.squeeze(D)` calls with a single `.unbind(dim=D)`, which returns a tuple of squeezed tensors directly, avoiding intermediate views and repeated squeezes.
