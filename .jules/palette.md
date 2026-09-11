## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-18 - Improve CLI error messages
**Learning:** Command-line interfaces without graphical UIs benefit greatly from user-friendly error handling. Raw stack traces for invalid inputs look like crashes.
**Action:** Always replace raw `assert` argument validation with `parser.error()` where `argparse` is used to cleanly guide the user with usage instructions.
