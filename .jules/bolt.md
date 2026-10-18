## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2024-04-20 - PyTorch CPU tensor repeated allocation overhead
**Learning:** Instantiating tensors directly from a Python list and duplicating memory via `.unsqueeze(0).repeat(...)` (e.g., `torch.tensor([x, y, z]).unsqueeze(0).repeat(bs, 1)`) incurs CPU allocation, list conversion overhead, and memory duplication. Creating a single-element list and using `.expand(bs, -1)` (e.g., `torch.tensor([[x, y, z]]).expand(bs, -1)`) avoids duplicating data, saving memory and compute, as `.expand()` creates a zero-copy view with stride 0.
**Action:** Replace `torch.tensor([val1, val2]).unsqueeze(0).repeat(batch_size, 1)` with `torch.tensor([[val1, val2]]).expand(batch_size, -1)` in PyTorch shape manipulation or positional embeddings setups.
