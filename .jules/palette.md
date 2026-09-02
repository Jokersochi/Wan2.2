## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2026-09-02 - Use parser.error for cleaner CLI validation messages
**Learning:** Python CLIs using `assert` for `argparse` validation throw intimidating stack traces for simple user errors like missing paths. Replacing raw `assert` statements with `parser.error()` inside `argparse` validation functions provides clean, usage-aware error messages and standard exit codes without blowing up the terminal.
**Action:** When validating `argparse` configurations, always use `parser.error()` instead of `assert` or standard exceptions to provide proper UX and exit codes.
