## 2024-05-24 - CLI UX Enhancements
**Learning:** For long-running video generation processes, adding contextual descriptions (`desc="..."`) to `tqdm` progress bars provides essential feedback, significantly improving the user experience for CLI users.
**Action:** Always add descriptive `desc` parameters when using `tqdm` to iterate over time steps or processing long batches in CLI tools.
