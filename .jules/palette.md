## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-28 - Clean CLI Error Messages
**Learning:** Raw assert statements cause intimidating stack traces for simple validation failures. Using parser.error() for CLI arguments creates standard exit codes and clean usage-aware error messages, greatly improving CLI UX.
**Action:** When validating arguments in CLI scripts utilizing argparse, always prefer parser.error() over assert for user-facing inputs while preserving fallback ValueError for API imports.
