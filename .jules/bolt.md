## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-04-19 - SDPA for manual attention
**Learning:** In PyTorch, replacing manual attention computations using `torch.einsum` and `F.softmax` with the highly optimized `F.scaled_dot_product_attention` (SDPA) provides significant execution speedups (e.g. ~3x) and memory reduction. When doing so for architectures like T5 that do not use scaling, `scale=1.0` must be explicitly passed.
**Action:** Replace manual einsum/softmax attention implementations with `F.scaled_dot_product_attention` and ensure correct `scale` parameters are used.
