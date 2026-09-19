## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## $(date +%Y-%m-%d) - Replaced unhandled asserts in CLI parsing with clean argparse errors
**Learning:** Python CLI tools, unlike web UIs, suffer extremely poor UX when using plain `assert` statements during arguments parsing, as users see raw stack traces instead of actionable messages. Using `parser.error()` resolves this by printing cleanly without crashing.
**Action:** Always check argument validation methods for raw assertions, and replace them with argparse usage errors wrapped in a helper function that falls back safely.
