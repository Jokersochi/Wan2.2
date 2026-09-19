## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-09-19 - Use SDPA for unscaled attention (T5)
**Learning:** PyTorch's `F.scaled_dot_product_attention` can be safely used for T5's unscaled attention by explicitly setting `scale=1.0`. This provides >3x speedup on CPU/GPU over manual einsum/softmax implementations without altering the model behavior.
**Action:** Always refactor manual attention calculations (like `einsum(q, k) -> softmax -> einsum(attn, v)`) to use SDPA with appropriate scaling and masks, even for older models that do not use default `1/sqrt(d)` scaling.
