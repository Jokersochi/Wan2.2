## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-18 - Improve CLI UX with parser.error
**Learning:** For Python CLI applications, replacing raw `assert` statements with `parser.error()` during argument validation provides a better user experience by printing the command-line usage alongside the error message.
**Action:** Always prefer `parser.error()` over raw `assert` statements for validating argparse arguments in CLI scripts to enhance usability.
