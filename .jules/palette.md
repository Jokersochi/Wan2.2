## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-12 - Improve CLI error messages
**Learning:** Raw assertions in CLI entry points throw ugly stack traces to users. Using argparse's parser.error() provides a cleaner, standard CLI error format showing usage instructions.
**Action:** Always prefer parser.error() over assert statements for validation logic tied to argparse arguments.
