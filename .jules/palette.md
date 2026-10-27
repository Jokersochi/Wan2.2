## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI help text UX by showing default argument values
**Learning:** Python CLI applications often have many arguments with default values, but `argparse.ArgumentParser` does not show these defaults in `--help` output by default. This forces users to either guess the default behavior or read the source code, which is a poor user experience.
**Action:** Always add `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` instances in CLI scripts. This automatically appends "(default: <value>)" to the help text of each argument, making the CLI much more intuitive and user-friendly without requiring manual documentation updates.
