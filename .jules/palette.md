## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-12 - Improved CLI Argument Validation
**Learning:** Using raw `assert` statements in Python CLI applications generates intimidating stack traces for simple user errors (like missing arguments).
**Action:** Replace `assert` with `parser.error()` in `argparse` validation to provide clean, usage-aware error messages and standard exit codes.
