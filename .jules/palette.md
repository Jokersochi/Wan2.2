## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-24 - CLI Error Messaging
**Learning:** For Python CLI tools without a web frontend, substituting raw `assert` exceptions with `parser.error()` enhances the micro-UX by presenting users with clean, formatted, and intuitive error messages alongside usage help rather than alarming tracebacks.
**Action:** Proactively replace abrupt assertion failures with `argparse` native error handling in CLI entry points to improve usability and accessibility for end-users.
