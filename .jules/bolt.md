## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2025-02-27 - Optimize GELU activation with PyTorch native function
**Learning:** Manual mathematical implementations of GELU (using `0.5 * x * (1.0 + torch.tanh(...))`) compute the approximation by allocating multiple intermediate tensors and executing separate kernels. PyTorch provides a native `F.gelu(x, approximate='tanh')` which is significantly faster and uses less memory.
**Action:** Always replace manual mathematical approximations of standard activation functions with their `torch.nn.functional` equivalents (like `F.gelu` with `approximate='tanh'`) when optimizing models.
