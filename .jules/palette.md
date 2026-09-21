## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-21 - Replace assert with argparse.error() in CLI
**Learning:** Command-line applications that use manual `assert` statements for argument validation result in confusing Python stack traces (AssertionError) for users instead of standard CLI help messages. Using `parser.error()` provides a significantly better micro-UX by printing a clear message alongside the command's usage instructions.
**Action:** Always check if a Python CLI script can be refactored to pass the `argparse.ArgumentParser` object to validation functions, replacing raw `assert` statements or generic `ValueError` exceptions with `parser.error()` to improve error feedback usability.
