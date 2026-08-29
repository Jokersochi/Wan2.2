## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-08-29 - Use parser.error for Argument Validation in CLI
**Learning:** Using raw `assert` statements for validating command-line arguments in `argparse` scripts provides a terrible user experience by throwing intimidating stack traces. Using `parser.error()` is significantly better as it provides clean, usage-aware error messages and exits with a standard error code.
**Action:** Replace `assert` statements used for parameter checking in CLI scripts with `parser.error()` or `raise ValueError()` (if a parser isn't available) to ensure clean validation feedback to the user.
