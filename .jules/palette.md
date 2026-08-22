## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-28 - CLI Argument Validation UX
**Learning:** Using raw `assert` statements for CLI argument validation provides a poor UX, as it exposes intimidating stack traces to the user.
**Action:** Replace `assert` statements with `parser.error()` in `argparse` scripts to provide clean, usage-aware error messages and standard exit codes.
