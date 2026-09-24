## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-18 - Improve CLI Error Messages
**Learning:** Raw assert statements in CLI parsing lead to noisy Python stack traces that confuse users expecting standard CLI error formats.
**Action:** Always pass the ArgumentParser instance to validation functions and use `parser.error()` instead of `assert` to enforce validation rules, providing clean and actionable error messages.
