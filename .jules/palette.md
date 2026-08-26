## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-11-20 - CLI Argument Validation
**Learning:** Raw `assert` statements should not be used for argument validation in CLI tools, as they produce intimidating stack traces for users and can be stripped out when Python is executed with optimization flags.
**Action:** Replace `assert` with `parser.error()` in `argparse` based CLI tools to provide usage-aware error messages and standard exit codes.
