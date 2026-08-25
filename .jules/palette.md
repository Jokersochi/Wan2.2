## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-28 - Clean CLI Error Handling
**Learning:** Raw `assert` statements in CLI argument parsing create intimidating Python stack traces for end users when validation fails, rather than standard helpful CLI errors.
**Action:** Replace `assert` validations with `parser.error()` in `argparse` implementations to provide standard usage instructions and clean error messages with proper non-zero exit codes.
