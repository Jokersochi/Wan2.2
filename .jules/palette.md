## 2025-04-14 - Add tqdm progress descriptions for long-running iterations
**Learning:** For CLI-based Python tools, adding descriptive text (e.g., `desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback.
**Action:** Always include a `desc` parameter when utilizing `tqdm` for long-running loops in CLI scripts.
