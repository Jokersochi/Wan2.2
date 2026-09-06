## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2025-02-28 - Clean CLI Error Outputs
**Learning:** Raw assert statements in Python CLI scripts lead to poor UX by displaying intimidating stack traces. Using `parser.error()` provides clean, usage-aware error messages and correct standard exit codes.
**Action:** Always replace `assert` used for argument validation with `parser.error()` in Python CLI applications.
