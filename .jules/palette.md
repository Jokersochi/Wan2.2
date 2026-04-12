## 2025-02-12 - Added clear descriptions to tqdm progress bars
**Learning:** For CLI-based Python tools executing long-running operations like video generation (e.g. DiT sampling steps), providing descriptive text (like `desc="DiT sampling"`) to `tqdm` progress bars gives users important context rather than just showing a generic progress bar.
**Action:** Always add a clear `desc` argument to `tqdm` instances when they are wrapping long-running loops in CLI tools to improve the user experience.
