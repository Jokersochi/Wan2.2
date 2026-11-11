## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-04-19 - T5 Manual Attention to SDPA overhead
**Learning:** PyTorch 2+ `F.scaled_dot_product_attention` is drastically faster and uses less memory than manual `torch.einsum` + `F.softmax` constructs, especially for transformer architectures like T5. Because T5 does not use the default 1/sqrt(d) scaling factor, it is critical to pass `scale=1.0` when migrating.
**Action:** Always replace manual attention computations with SDPA in PyTorch, but check if the original implementation had custom scaling, dropouts, or masking that must be mirrored in the SDPA parameters to avoid functional deviations.
