## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## $(date +%Y-%m-%d) - Improve CLI argument validation UX
**Learning:** Raw `assert` statements for validating CLI inputs lead to intimidating and messy Python tracebacks (`AssertionError`) for the end user, rather than helpful usage instructions.
**Action:** Replace `assert` statements used for argument validation with `parser.error()`. This ensures standard CLI error messages and usage text are presented cleanly to the user.
