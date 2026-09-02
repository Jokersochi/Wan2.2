## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-18 - einsum to scaled_dot_product_attention
**Learning:** PyTorch's `F.scaled_dot_product_attention` is highly optimized and significantly faster than manual `torch.einsum` and softmax operations for computing attention. It utilizes specialized kernels (like FlashAttention) and reduces memory overhead.
**Action:** Always prefer `F.scaled_dot_product_attention` over manual `einsum` for attention mechanisms when using PyTorch 2.0+.
