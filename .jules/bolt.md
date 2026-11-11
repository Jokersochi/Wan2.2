## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2025-02-23 - Use PyTorch SDPA in T5 Module
**Learning:** Manual attention computation (einsum + softmax) is slow and memory-intensive; standard implementations can be safely upgraded to F.scaled_dot_product_attention if scaling differences (e.g. scale=1.0 for T5) are respected.
**Action:** Always check manual attention layers for opportunities to replace with SDPA, making sure to match dropout and scaling behavior exactly.
