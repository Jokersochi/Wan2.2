## 2024-05-20 - Descriptive Progress Bars
**Learning:** For CLI-based Python tools, adding descriptive text (e.g., `desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback.
**Action:** Always include a `desc` argument in `tqdm` loops to inform the user about the current long-running task.
