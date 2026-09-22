## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI UX with parser.error
**Learning:** For Python CLI apps, replacing raw assert statements with argparse.ArgumentParser.error() improves command-line usability by providing clean error messages instead of jarring tracebacks.
**Action:** Use parser.error() instead of assert for argument validation.
