## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-19 - Improve CLI error messages
**Learning:** Raw assert statements produce stack traces which are poor UX for CLI tools. Using parser.error() provides clean, actionable feedback.
**Action:** Always validate arguments with parser.error() instead of assert in CLI scripts to improve the command-line usability.
