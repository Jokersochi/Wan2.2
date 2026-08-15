## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-18 - Replace einsum attention with SDPA
**Learning:** Manual implementation of scaled dot product attention using `torch.einsum` and `F.softmax` introduces significant overhead and misses out on PyTorch's optimized kernels (Flash Attention).
**Action:** Replace `torch.einsum` based attention with PyTorch's native `F.scaled_dot_product_attention` combined with `.transpose(1, 2)` to achieve a ~3x performance boost.
