## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## $(date +%Y-%m-%d) - Improve CLI argument validation error messages
**Learning:** Using raw `assert` statements for CLI argument validation causes intimidating stack tracebacks (`AssertionError`) for the user.
**Action:** Replace `assert` statements used for CLI argument validation with `parser.error()` to provide clean, standard CLI error messages and usage instructions.
