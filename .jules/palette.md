## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-17 - Better CLI Error Handling
**Learning:** Raw assert statements in CLI argument validation trigger stack traces which are intimidating and unhelpful to end users.
**Action:** Replaced assert checks in `_validate_args` with `parser.error()`, displaying cleaner CLI usage instructions alongside the specific validation error. Included a fallback `ValueError` for programmatically driven function calls.
