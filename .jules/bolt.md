## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2025-02-28 - PyTorch SDPA in T5
**Learning:** Manual attention computation using `torch.einsum` and `F.softmax` can be a significant performance bottleneck, especially for architectures like T5 that are often bypassed for FlashAttention due to missing default support.
**Action:** Always replace manual attention computations with `F.scaled_dot_product_attention` (SDPA), setting `scale=1.0` to disable the default `1/sqrt(d)` scaling to preserve functional equivalence for unscaled implementations.
