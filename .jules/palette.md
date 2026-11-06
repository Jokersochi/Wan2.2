## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI error messages by using parser.error instead of assertions
**Learning:** Raw `assert` statements in Python CLIs dump intimidating stack traces to the user (e.g., `AssertionError`), which degrades the user experience. By replacing `assert` with `argparse`'s `parser.error()`, users receive standard, readable error messages and CLI usage instructions.
**Action:** Always replace basic argument validation assertions with `parser.error()` in Python CLI scripts to provide standard, user-friendly error formatting without exposing internal code structures.
