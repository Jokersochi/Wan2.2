## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-15 - Clean CLI Error Feedback
**Learning:** Using raw `assert` statements for CLI validation causes messy tracebacks that look like crashes, and they are silently ignored when Python runs in optimized mode (`-O`). This creates a poor command-line user experience.
**Action:** Always use `parser.error()` or explicit exception handling to return clean, actionable error messages instead of relying on `assert` for CLI inputs.
