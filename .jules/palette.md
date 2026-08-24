## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-19 - Improve argparse validation UX
**Learning:** For Python CLI applications using `argparse`, replacing raw `assert` statements used for argument validation with `parser.error()` provides clean, usage-aware error messages (and standard exit codes) instead of intimidating stack traces. This greatly improves the developer UX when interacting with the CLI.
**Action:** Always replace raw assertions for command-line validation with `parser.error()` to provide graceful failure and helpful usage instructions.
