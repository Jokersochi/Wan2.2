## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-05-24 - PyTorch Native Functions over Manual Tensor Ops
**Learning:** Manual implementations of mathematical functions like GELU using combinations of tensor operations (`torch.pow`, `torch.tanh`, `add`, `mul`) are extremely inefficient compared to PyTorch's native `F.gelu(x, approximate="tanh")`. The native functions utilize optimized, fused CUDA/C++ kernels, avoiding intermediate tensor memory allocation and drastically reducing kernel launch overhead.
**Action:** Always verify if a complex mathematical formula in PyTorch has a native `torch.nn.functional` equivalent. Replace manual approximations with the highly optimized native counterparts.
