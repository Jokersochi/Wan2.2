## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2024-08-17 - Improve CLI error message clarity
**Learning:** For Python CLI applications using `argparse`, raw `assert` statements for argument validation throw unhandled `AssertionError` exceptions, presenting users with an intimidating stack trace. 'Palette' UX improvements include replacing these with `parser.error()`, which provides a clean, standard CLI error message alongside the usage text and exits gracefully with code 2.
**Action:** Always replace `assert` based argument validation with `parser.error()` in `argparse` setups to ensure a polished and robust command-line user experience.
