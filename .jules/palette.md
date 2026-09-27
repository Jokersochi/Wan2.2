## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-24 - Improve CLI Error Messages
**Learning:** Using raw `assert` statements for argparse validation produces confusing stack traces for users and fails under Python optimization (-O).
**Action:** Always pass the `parser` object to validation functions and use `parser.error()` to provide actionable, clean CLI error messages.
