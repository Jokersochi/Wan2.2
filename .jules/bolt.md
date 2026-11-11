## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-10 - PyTorch dimension splitting overhead
**Learning:** In PyTorch, using `.chunk(N, dim=D)` followed by manual squeezing of the extra dimension (e.g., `e = e.chunk(6, dim=1); e = [el.squeeze(1) for el in e]`) allocates intermediate tensor views and adds unnecessary `SqueezeBackward` nodes to the autograd graph. `.unbind(dim=D)` directly returns a tuple of tensors with the specified dimension removed, completely avoiding this overhead.
**Action:** Replace `tensor.chunk(N, dim=D)` followed by `.squeeze(D)` with `tensor.unbind(dim=D)` in high-frequency network code paths.
