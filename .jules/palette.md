## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-27 - Better Error Messages for Python CLI Apps
**Learning:** For Python CLI tools, users are often greeted with ugly internal `AssertionError` tracebacks when they simply provide a bad argument or forget a required one. This is intimidating and creates a poor developer experience (DX/UX).
**Action:** When validating `argparse` arguments, avoid using bare `assert condition, msg` in functions after parsing. Instead, pass the parser instance into validation functions and use `parser.error(msg)`. This guarantees standard usage formatting (e.g., printing the help snippet) and cleanly exits with code 2, significantly improving the end-user experience.
