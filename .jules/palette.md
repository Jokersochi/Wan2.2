## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2025-02-09 - CLI Argument Validation Error Handling
**Learning:** Using raw assertions for command-line argument validation results in intimidating stack traces for users, confusing them about whether the software crashed or if their input was wrong.
**Action:** Always pass the `argparse.ArgumentParser` instance down to validation logic to use `parser.error()` for clean, usage-aware error messages with standard exit codes, falling back to `ValueError` when used programmatically.
