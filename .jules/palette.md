## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-18 - Improve CLI UX by Replacing Assertions with Argparse Errors
**Learning:** Using raw `assert` statements in Python CLIs produces poor UX because it raises `AssertionError` with a full stack trace, hiding the actual cause from the user. Leveraging `parser.error()` inside `argparse` validation logic gracefully prints the usage string and a clean error message, making the CLI much more intuitive.
**Action:** Always validate CLI parameters using `parser.error()` rather than `assert`, and pass `parser` optionally to validation functions so they can safely fallback to `raise ValueError()` when imported directly as a library.
