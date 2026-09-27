## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2024-10-24 - Improve CLI argument validation errors
**Learning:** Replaced bare `assert` statements in the CLI parameter validation of `generate.py` with `parser.error()`. This improves command-line usability by gracefully exiting and clearly printing the error message instead of throwing an unhandled `AssertionError` traceback, making the tool more accessible and intuitive to use.
**Action:** Use `parser.error()` for user-facing CLI inputs to provide clear feedback rather than tracebacks.
