## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI validation UX
**Learning:** Using raw `assert` statements for validating command line arguments in Python scripts results in confusing `AssertionError` stack traces for end users.
**Action:** Always replace `assert` validation in CLI scripts with `parser.error()`, which prints a clean error message and usage instructions.
