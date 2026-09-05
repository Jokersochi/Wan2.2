## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2025-02-18 - Improve CLI error messaging
**Learning:** Raw assert statements for argument validation in CLI tools raise intimidating stack traces and generic errors. Wrapping validation to use `parser.error()` provides clean, usage-aware error messages with standard exit codes, greatly improving the developer experience.
**Action:** When implementing or refactoring Python CLI applications using `argparse`, pass the parser to validation functions to leverage `parser.error()` for clean, structured error outputs instead of relying on `assert`.
