## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-11-10 - `.chunk()` to `.unbind()` broadcasting nuance
**Learning:** When replacing PyTorch `.chunk(N, dim=D)` combined with `.squeeze(D)` into `.unbind(dim=D)` to reduce Python overhead, strictly ensure the `.squeeze()` is present in the original code. If `.squeeze()` is absent, replacing with `.unbind()` drops the dimension, changing the tensor shape from `[..., 1, ...]` to `[...]`. This breaks downstream PyTorch broadcasting (e.g., `[B, C]` will not broadcast correctly against `[B, L, C]`, whereas `[B, 1, C]` does).
**Action:** Always verify `.squeeze(D)` is explicitly called on the chunked outputs before refactoring to `.unbind(dim=D)`.
