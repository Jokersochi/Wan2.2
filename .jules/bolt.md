## 2024-04-12 - Prevent Unnecessary Memory Allocation in PyTorch Concatenation
**Learning:** Calling `torch.cat()` with dynamic empty padding tensors (e.g. `new_zeros()` of size 0) introduces unnecessary kernel overhead and memory allocation.
**Action:** Wrap concatenations involving dynamic padding in inline conditional checks (e.g., `torch.cat([u, u.new_zeros(...)]) if seq_len > u.size(1) else u`) to bypass empty concatenation overhead.
