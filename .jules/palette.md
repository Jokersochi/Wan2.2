## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.

## 2024-05-19 - Improve CLI UX with ArgumentDefaultsHelpFormatter
**Learning:** For Python CLI applications, users need to see default parameter values to understand behavior without running it first.
**Action:** Add `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` instances to automatically show default values in the `--help` output.
