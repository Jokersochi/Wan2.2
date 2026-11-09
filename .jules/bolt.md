## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-24 - Replace chunk-squeeze with unbind
**Learning:** In PyTorch, using `.chunk(N, dim=D)` followed by `.squeeze(D)` allocates intermediate tensors. Replacing it with `.unbind(dim=D)` directly returns a tuple of tensors without the specified dimension, reducing overhead.
**Action:** Always prefer `.unbind()` over `.chunk().squeeze()` when decomposing tensors along a dimension.
