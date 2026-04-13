## 2025-02-20 - PyTorch torch.cat Memory Allocation Overhead with 0-size Tensors
**Learning:** In PyTorch, concatenating dynamic 'padding' zero-tensors (e.g., using `new_zeros()`) with a size of 0 still allocates new memory and introduces kernel overhead.
**Action:** When conditionally padding tensors via concatenation, always wrap the operation in an inline size-check (e.g., `torch.cat([u, u.new_zeros(...)]) if size < target_length else u`) to bypass redundant memory allocation and copying.
