## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-14 - Improve CLI Validation Errors
**Learning:** In CLI applications, Python `assert` statements provide poor user experience by throwing raw tracebacks. Users benefit greatly from clear error messages alongside usage instructions.
**Action:** Replace `assert` validations in CLI argument parsers with `parser.error()`, while maintaining API compatibility by falling back to standard exceptions like `ValueError` when the parser is not provided.
