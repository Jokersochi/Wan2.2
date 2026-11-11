## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-04-19 - Use SDPA for T5 attention
**Learning:** T5 attention uses unscaled queries/keys. Replacing the manual einsum/softmax implementations with PyTorch's `F.scaled_dot_product_attention` using `scale=1.0` achieves equivalent correctness and near 3x speedup on CPU.
**Action:** Replace `torch.einsum` attention computations with `F.scaled_dot_product_attention` for components that can benefit from it, but remember to preserve specific scale values like `scale=1.0` when a model overrides the `1/sqrt(d)` default.
