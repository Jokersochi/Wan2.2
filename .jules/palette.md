## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2024-05-18 - Improve CLI UX with parser.error
**Learning:** For Python CLI applications using `argparse`, 'Palette' UX improvements include replacing raw `assert` statements used for argument validation with `parser.error()` to provide clean, usage-aware error messages (and standard exit codes) instead of intimidating stack traces.
**Action:** Always prefer `parser.error("message")` over `assert condition, "message"` when performing manual argument validation in scripts to ensure users see helpful CLI errors rather than Python tracebacks.
