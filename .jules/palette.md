## 2024-04-19 - Added context to long-running console applications
**Learning:** For Python CLI applications like Wan2.2, long-running processes using standard tools like `tqdm` should provide context-rich descriptions (e.g., `desc="Generating video..."`) instead of blank progress bars.
**Action:** When adding or modifying `tqdm` bars, always include a `desc` argument to provide clear feedback.
