## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-03-24 - PyTorch Tensor Initialization Overhead
**Learning:** In PyTorch, using `torch.tensor([val] * b).to(device)` inside hot loops (like attention layers) creates unnecessary overhead from Python list initialization, CPU tensor allocation, and device data transfer.
**Action:** Always use `torch.full((b,), val, device=device)` to allocate and fill the tensor directly on the target device.
