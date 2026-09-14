## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-14 - Improve CLI UX by replacing asserts with parser errors
**Learning:** Using raw assert statements in a CLI application results in ugly AssertionErrors and stack traces for normal user errors (like missing arguments). This leads to a poor user experience as it looks like a program crash rather than invalid input.
**Action:** Use `parser.error()` from `argparse` instead to provide clean, user-friendly error messages with usage instructions. Pass the parser to validation functions to enable this gracefully without breaking internal API calls.
