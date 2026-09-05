## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-10 - Replace manual unscaled attention with SDPA
**Learning:** When replacing manual unscaled attention implementations (e.g., T5) with PyTorch's `F.scaled_dot_product_attention` (SDPA), explicitly pass `scale=1.0` to disable the default `1/sqrt(d)` scaling and preserve functional equivalence.
**Action:** When refactoring T5 attention blocks or other models that do not use scaling in attention, ensure `scale=1.0` is explicitly set in the SDPA call.
