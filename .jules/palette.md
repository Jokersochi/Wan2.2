## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-24 - CLI Error Handling Improvements
**Learning:** In CLI-based repositories without graphical interfaces, raw `assert` statements provide poor user experience by throwing stack traces.
**Action:** Replace `assert` statements with `parser.error()` in argument validation to treat user errors as standard CLI usage errors, improving clarity.
