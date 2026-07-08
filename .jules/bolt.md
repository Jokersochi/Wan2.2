## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2026-07-08 - Replace torch.einsum with permute
**Learning:** In PyTorch, replacing simple dimension transposition via `torch.einsum` (e.g., `torch.einsum('fhwpqrc->cfphqwr', u)`) with `permute` (e.g., `u.permute(6, 0, 3, 1, 4, 2, 5)`) yields significant performance improvements by eliminating the overhead of string parsing and execution plan building inside high-frequency loops.
**Action:** Use `permute` for simple transpositions instead of `torch.einsum` in performance-critical paths like the `unpatchify` loop.
