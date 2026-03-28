## 2026-03-28 - Prevent Redundant Memory Allocation in rope_apply
**Learning:** In PyTorch, calling `torch.cat()` with an empty tensor always allocates new memory and incurs a copy overhead. During `rope_apply` execution, `torch.cat([x_i, x[i, seq_len:]])` concatenates an empty slice when `seq_len` equals the sequence length.
**Action:** When conditionally concatenating tensors, specifically those sliced to potentially empty chunks (e.g. `x[i, seq_len:]`), wrap the operation in a size-check (`if seq_len < x.size(1):`) to prevent redundant memory allocation and improve efficiency.
