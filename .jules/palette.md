## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI error messages
**Learning:** Python `assert` statements must not be used for runtime validation or API response checks in CLI applications, as they are removed when Python is executed with optimization flags (e.g., `-O`). Additionally, throwing bare `AssertionError` tracebacks for invalid user arguments is a poor command-line interface user experience.
**Action:** Replace `assert` statements used for argument validation with `parser.error()` to provide clean, usage-aware error messages and standard exit codes.
