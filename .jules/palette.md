## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-12 - Improve CLI Error Usability
**Learning:** Raw assert statements in CLI parsers create confusing Python tracebacks for end-users, leading to poor UX.
**Action:** Always use parser.error() for graceful CLI termination and clear error messages, with a fallback to ValueErrors for API compatibility.
