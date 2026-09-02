## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-06-25 - Improve CLI UX with parser.error
**Learning:** For Python CLI applications using `argparse`, raw `assert` statements for argument validation produce intimidating stack traces. Replacing them with `parser.error()` provides clean, usage-aware error messages and standard exit codes.
**Action:** Always replace `assert` statements with `parser.error()` in `argparse` validation logic, and use a fallback `ValueError` if the parser is not provided.
