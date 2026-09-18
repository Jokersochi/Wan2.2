## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-09-18 - CLI Error Messaging UX
**Learning:** Raw assert statements in CLI validation scripts expose Python tracebacks to users, creating a confusing and intimidating developer experience for non-technical users running ML scripts.
**Action:** Replace assert validations with argparse.ArgumentParser.error() (or fallback to ValueError) to provide clean, actionable error messages that include usage instructions without stack traces.
