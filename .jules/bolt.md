## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.
## 2024-05-18 - Avoid Python list init for Tensors inside hot loops
**Learning:** Initializing PyTorch tensors directly on the device using `torch.full((size,), val, device=device)` is substantially faster and avoids memory overhead compared to `torch.tensor([val] * size).to(device)`.
**Action:** Always scan for redundant host-to-device transfers and list initializations inside critical layers like attention, and replace them with native PyTorch constructor functions directly allocating on the target device.
