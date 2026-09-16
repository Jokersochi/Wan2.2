## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2025-02-15 - CLI Error Message Polish
**Learning:** Using raw assert statements for CLI input validation results in ugly, hard-to-read Python stack traces that confuse users.
**Action:** Replace `assert` with `parser.error()` inside argument validation to gracefully exit with standard CLI error formatting while retaining fallback exceptions for direct API use.
