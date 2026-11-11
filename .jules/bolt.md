## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-11-11 - PyTorch Tensor Chunk vs Unbind Micro-optimization
**Learning:** PyTorch `.chunk()` followed by repeated element access and `.squeeze()` creates unnecessary intermediate tensor views and invokes Python indexing overhead repeatedly.
**Action:** When a dimension is being split perfectly into single-element slices and the trailing dimension needs to be removed, replace `.chunk(dim=D)` combined with `[index]` and `.squeeze(D)` with a single `.unbind(dim=D)` and explicit tuple unpacking. This significantly reduces tensor allocations and overhead in high-frequency paths like transformer blocks.
