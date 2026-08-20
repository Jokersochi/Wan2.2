## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI error messages UX
**Learning:** For Python CLI applications using `argparse`, raw `assert` statements used for argument validation can lead to intimidating stack traces and non-standard exit codes. Replacing them with `parser.error()` provides clean, usage-aware error messages and standard exit codes, which significantly improves the command-line user experience and accessibility for users dealing with improper inputs.
**Action:** Always replace `assert` validations in `argparse` scripts with `parser.error()` to ensure clean output and provide helpful context to users rather than raw stack traces.
