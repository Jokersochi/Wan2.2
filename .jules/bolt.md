## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2025-03-04 - PyTorch SDPA over manual einsum attention
**Learning:** In PyTorch 2+, replacing manual attention computations using `torch.einsum` and `F.softmax` with the highly optimized `F.scaled_dot_product_attention` (SDPA) provides significant execution speedups and memory reduction by utilizing fused CUDA kernels like FlashAttention, while ensuring numerical equivalence.
**Action:** Always replace manual mathematical approximations of attention with `torch.nn.functional.scaled_dot_product_attention` whenever possible.
