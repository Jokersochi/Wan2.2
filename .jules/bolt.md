## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-24 - PyTorch SDPA Replacement
**Learning:** Manual attention computation using `torch.einsum` + `F.softmax` or `q @ k.transpose` + `F.softmax` leaves a lot of performance on the table in PyTorch.
**Action:** Always replace them with `F.scaled_dot_product_attention` for significant memory reductions and speedups without behavioral changes (using `scale=1.0` if no scale was originally used).
## 2024-05-24 - PyTorch SDPA Scale
**Learning:** `F.scaled_dot_product_attention` by default applies `scale=1 / sqrt(d)`. If the original code explicitly applied a custom or different scale (e.g. `scale_factor`), it is critical to explicitly pass it via the `scale` kwarg in SDPA to ensure mathematical equivalence and prevent silent regressions.
**Action:** When replacing manual attention, always check what scaling was applied and pass it to SDPA using `scale=...` if it differs from or explicitly matches a variable in the original code.
