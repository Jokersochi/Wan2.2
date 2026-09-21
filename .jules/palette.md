## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-09 - Improve CLI Error Messages
**Learning:** In Python CLI tools, users frequently encounter raw AssertionError stack traces when validating configuration parameters, which feels like an application crash rather than an input error.
**Action:** Always pass the `argparse.ArgumentParser` to validation functions and use `parser.error()` to provide native, user-friendly CLI error messages with usage instructions.
