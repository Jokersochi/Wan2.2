## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-05-19 - chunk and squeeze overhead
**Learning:** In PyTorch, using `.chunk(dim)` followed by `.squeeze(dim)` creates intermediate un-squeezed tensor views. Using `.unbind(dim)` directly returns slices with the specified dimension removed, avoiding the overhead of creating and processing dimensions of size 1.
**Action:** Replace patterns like `e = (a + b).chunk(N, dim=D); e = [x.squeeze(D) for x in e]` with `e = (a + b).unbind(dim=D)` in high-frequency paths like model forward passes.
