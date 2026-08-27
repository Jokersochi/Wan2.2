## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI error handling with parser.error
**Learning:** For Python CLI applications using `argparse`, 'Palette' UX improvements include replacing raw `assert` statements used for argument validation with `parser.error()`. This provides clean, usage-aware error messages and standard exit codes instead of intimidating stack traces via `AssertionError`.
**Action:** When validating CLI arguments inside `argparse` workflows, always use `parser.error("message")` instead of `assert` to gracefully handle user input errors.
