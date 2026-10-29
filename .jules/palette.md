## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Display CLI defaults in help messages
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` instances to automatically display default values.
**Action:** Always add `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` calls for improved command-line user experience.
