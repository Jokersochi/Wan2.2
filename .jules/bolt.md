## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-18 - SDPA for unscaled attention
**Learning:** Manual attention computation using `torch.einsum` and `F.softmax` is slow and memory-intensive. `F.scaled_dot_product_attention` (SDPA) provides highly optimized fused CUDA kernels. For models like T5 that do not use `1/sqrt(d)` scaling, we can still use SDPA by explicitly passing `scale=1.0`.
**Action:** Replace manual unscaled attention implementations (e.g., T5) with `F.scaled_dot_product_attention(..., scale=1.0)` to preserve functional equivalence while improving speed.
