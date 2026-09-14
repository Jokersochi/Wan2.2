## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2025-02-28 - SDPA for unscaled attention
**Learning:** PyTorch's F.scaled_dot_product_attention provides significant speedups over manual einsum+softmax implementations even when scaling is not desired, by explicitly passing scale=1.0.
**Action:** When refactoring manual attention blocks (like T5) to SDPA, always ensure layout dimensions (B, NumHeads, L, HeadDim) and scale are correctly aligned to preserve functional equivalence while improving performance.
