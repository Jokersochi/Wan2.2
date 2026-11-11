## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-15 - T5 manual attention to SDPA
**Learning:** In PyTorch 2+, replacing manual T5 attention computations (einsum + softmax) with `F.scaled_dot_product_attention(..., scale=1.0)` provides more than a 2x speedup and significantly reduces memory usage while maintaining numerical parity.
**Action:** When implementing or refactoring T5 style attention, directly use `F.scaled_dot_product_attention` with `scale=1.0` (to disable default 1/sqrt(d) scaling) instead of manually computing queries, keys, masks, and softmax with einsum.
