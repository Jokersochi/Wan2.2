## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-23 - Clean CLI Error Messages
**Learning:** Replacing raw `assert`s with `parser.error()` provides cleaner, user-friendly error output for missing or invalid CLI arguments, instead of ugly stack traces.
**Action:** Consistently use `parser.error()` or custom exceptions for argument validation in CLI-based tools to improve usability.
