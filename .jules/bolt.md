## 2024-05-24 - Zero padding tensors

## 2024-05-25 - Prevent zero-tensor concatenation overhead
**Learning:** PyTorch allocates kernel overhead and new memory when conditionally concatenating tensors, even if the concatenated block (e.g. padding zeroes) is empty (size 0).
**Action:** Use inline conditionals (e.g., `torch.cat([u, u.new_zeros(...)]) if seq_len > u.size(1) else u`) rather than creating dynamic zero-tensors and letting `torch.cat` handle empty slices to prevent unnecessary allocations. Also replacing `keys()` in dict view with direct lookup.
