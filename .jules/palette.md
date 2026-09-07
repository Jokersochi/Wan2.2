## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-06-15 - Improve CLI UX with parser.error
**Learning:** Raw assert statements in Python CLI scripts raise intimidating stack traces on invalid arguments, hurting usability. Replacing them with argparse's `parser.error()` provides clean, usage-aware error messages and standard exit codes.
**Action:** Always replace manual argument validation asserts with `parser.error(msg)` (passed via an optional parser object) to improve command-line user experience while maintaining internal API flexibility.
