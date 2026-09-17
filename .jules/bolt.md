## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-04-19 - SDPA with T5 scaling
**Learning:** In PyTorch, replacing manual attention calculations (`torch.einsum` + `F.softmax`) with `F.scaled_dot_product_attention` in T5 models requires explicitly passing `scale=1.0` to override the default `1/sqrt(d)` scaling, ensuring exact mathematical equivalence.
**Action:** When refactoring T5 attention to use SDPA, always set `scale=1.0`.
