## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-03-08 - Use `parser.error` for cleaner CLI argument validation
**Learning:** Using raw `assert` statements for validating CLI arguments (`argparse`) causes intimidating stack traces for users (e.g. `AssertionError`), creating a poor user experience.
**Action:** When validating parsed arguments manually, always pass the `argparse.ArgumentParser` instance to the validation function and use `parser.error(...)`. This prints proper usage instructions and cleanly exits, improving CLI usability.
