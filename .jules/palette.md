## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-19 - Replace assert with parser.error in CLI validations
**Learning:** For Python CLI applications using `argparse`, raw `assert` statements used for argument validation provide intimidating stack traces. Replacing them with `parser.error()` provides clean, usage-aware error messages and standard exit codes.
**Action:** When validating `argparse` arguments, avoid `assert` and instead pass the parser object into the validation function so you can call `parser.error()` with user-friendly messages.
