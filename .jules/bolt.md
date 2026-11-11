## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2025-02-12 - PyTorch SDPA without scaling
**Learning:** PyTorch's `F.scaled_dot_product_attention` applies a default scale factor of `1/sqrt(d)` to the query-key dot product. When optimizing manual attention code that doesn't use this standard scaling (like T5), you must explicitly set `scale=1.0` to override the default and preserve functional equivalence.
**Action:** Always verify scaling requirements and apply `scale=1.0` in `F.scaled_dot_product_attention` when replacing manual unscaled attention block code.
