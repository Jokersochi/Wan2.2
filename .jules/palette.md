## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-05-18 - Improve CLI UX by displaying default values
**Learning:** For Python CLI tools using `argparse`, a very simple and high-impact UX improvement is to set `formatter_class=argparse.ArgumentDefaultsHelpFormatter`. This automatically appends the default values to the `--help` string, reducing cognitive load on users so they don't have to guess or check the source code to find the defaults.
**Action:** When working on CLI scripts, check if `argparse.ArgumentParser` is used without a formatter class, and add it to immediately improve the help output context.
