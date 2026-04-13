## 2024-04-13 - Add descriptive text to tqdm progress bars
**Learning:** In CLI-based applications with long-running inference tasks (like video generation), adding a `desc` parameter to `tqdm` progress bars provides crucial context to the user. Without it, users just see a progress bar and may not know what process is actually happening (e.g., "Sampling" vs "Retargeting").
**Action:** Always include a descriptive `desc="..."` parameter when initializing `tqdm` progress bars in CLI tools to improve the user experience and provide clear feedback on the current operation.
