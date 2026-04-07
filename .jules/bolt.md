
## 2024-03-05 - Avoid Unnecessary Memory Allocations with Conditional PyTorch Operations
**Learning:** In PyTorch, allocating empty or padded zero-tensors with sizes computed dynamically (e.g., `new_zeros` with dimensions evaluating to 0 like `u.new_zeros(1, seq_len - u.size(1), u.size(2))` when `seq_len == u.size(1)`) and concatenating them inherently invokes kernel overhead and redundant memory operations.
**Action:** Always wrap these padding or concatenation sequences in conditional checks (e.g., `if seq_len > u.size(1) else u`) to avoid unnecessary compute overhead and memory allocations.
