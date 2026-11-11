## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-19 - GELU manual approximation performance
**Learning:** PyTorch native math functions written in C++ (like `F.gelu`) are significantly faster and use less memory than manual tensor compositions in Python (e.g., combining `pow`, `tanh`, `add`, `mul` to manually implement GELU) because they avoid allocating intermediate tensors and use optimized fused CUDA kernels.
**Action:** Always replace manual mathematical approximations of standard activation functions with their `torch.nn.functional` equivalents.
