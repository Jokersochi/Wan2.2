## 2024-10-22 - Replacing `.chunk` + `.squeeze` with `.unbind` for PyTorch optimizations

**Learning:** In PyTorch, using `.chunk(N, dim=D)` followed by indexing or iterating and calling `.squeeze(D)` is a common pattern for splitting a tensor into multiple parts along a dimension. However, `.unbind(dim=D)` accomplishes the same result by returning a tuple of tensors with the specified dimension already removed. `.unbind` is generally more efficient because it skips the intermediate tensor allocation and avoids multiple squeeze operations, thus reducing Python execution overhead in critical sections (like Transformer blocks).

**Action:** Whenever identifying `.chunk` followed by `.squeeze(dim)` or `.chunk` returning size-1 chunks that are then squeezed, replace it with `.unbind(dim=dim)` to slightly reduce CPU overhead during dispatch, especially inside deep loops like attention layers.
