## 2024-04-19 - unpatchify loop overhead
**Learning:** In Python/PyTorch high-frequency code paths like the 'unpatchify' loop, replacing generalized functional constructs like `math.prod` and list comprehensions with `zip` with direct tuple unpacking and scalar multiplication (e.g., `v[0] * v[1] * v[2]`) reduces execution overhead significantly.
**Action:** Replace `math.prod(v)` and `[i * j for i, j in zip(v, self.patch_size)]` with explicit unpacks like `v[0] * v[1] * v[2]` and direct multiplication elements `v[0] * self.patch_size[0]`, etc.

## 2026-10-12 - .repeat() vs .expand() for dynamic tensor duplication
**Learning:** In PyTorch, using `.unsqueeze(0).repeat(batch_size, 1)` or similar repeats to dynamically construct grid coordinates or tensors across batch dimensions creates unnecessary O(N) memory allocation and copy overhead (especially slow on CPU before syncing).
**Action:** Replace `.repeat()` with `.expand(batch_size, -1)` (e.g. `torch.tensor([-1, 0, 0]).unsqueeze(0).expand(batch_size, -1)`). This creates a broadcasted zero-copy view, leading to an almost 3x speedup in these hot loop path tensor constructions during sequence embedding preparation.
