## 2025-02-20 - Adding descriptions to tqdm progress bars in CLI tools
**Learning:** For CLI-based Python tools, adding descriptive text (e.g., `desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback.
**Action:** Always check if `tqdm` loops in long-running processes have descriptive labels.
