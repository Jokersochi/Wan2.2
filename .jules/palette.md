## 2025-04-05 - Add descriptive text to tqdm progress bars
**Learning:** In CLI-based Python tools, adding descriptive text (e.g., `desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback.
**Action:** Always include a clear, concise `desc` argument when using `tqdm` for potentially slow or repetitive operations.
