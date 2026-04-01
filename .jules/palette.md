## 2024-05-18 - CLI UX Feedback
**Learning:** For CLI-based Python tools, adding descriptive text (e.g., `desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback. Without it, users may be confused about what the progress bar represents.
**Action:** Always include a `desc` argument in `tqdm` loops for any long-running generation, sampling, or data processing steps to make the CLI interface more intuitive and pleasant to use.
