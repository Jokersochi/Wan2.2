## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2025-02-23 - Improve CLI error messages
**Learning:** Using `assert` for CLI argument validation causes scary tracebacks. Using `parser.error()` provides clean, actionable feedback to users.
**Action:** When validating CLI arguments in Python, always pass the `parser` object down and use `parser.error()` instead of `assert` to improve command-line usability.
