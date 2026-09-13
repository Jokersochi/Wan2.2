## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2026-09-13 - Improve CLI UX by replacing raw assertions
**Learning:** For CLI tools that parse arguments, raising raw Python assertions when validation fails creates a poor user experience by dumping a stack trace. Instead, using argparse's `parser.error()` produces cleaner, contextual error messages with usage hints.
**Action:** When validating command-line arguments in CLI applications, explicitly pass the parser to validation functions and use `parser.error()` rather than native `assert` statements.
