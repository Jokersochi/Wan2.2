## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2025-02-27 - SDPA for Manual Attention
**Learning:** PyTorch 2's `F.scaled_dot_product_attention` (SDPA) provides huge performance and memory improvements over manual `torch.einsum` + `F.softmax` implementations for attention. It requires `scale=1.0` if overriding the default 1/sqrt(d) scaling (like in T5).
**Action:** Always replace manual attention computations with `F.scaled_dot_product_attention` when maintaining PyTorch code, ensuring to match the `scale` and tensor layout (batch, heads, seq, dim).
