## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-04-26 - T5 attention with SDPA
**Learning:** In PyTorch 2+, manual `einsum` and `softmax` attention implementations should be replaced with `F.scaled_dot_product_attention` (SDPA). When doing this for T5, `scale=1.0` must be used to disable the default `1/sqrt(d)` scaling factor, and `dropout_p=0.0` should be used because T5 applies dropout to the output projection, not the attention matrix directly.
**Action:** Replace manual attention implementations with SDPA where possible, taking care to preserve the exact scaling and dropout behavior of the original architecture.
