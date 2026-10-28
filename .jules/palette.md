## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-10-28 - CLI Argument Defaults Auto-Display
**Learning:** For Python CLI tools, users often struggle to remember default values for arguments. While adding descriptions to `tqdm` is good for feedback, adding `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` is a zero-dependency, high-impact micro-UX win that automatically documents defaults without cluttering help strings.
**Action:** Always check `argparse` implementations in CLI tools for the presence of `ArgumentDefaultsHelpFormatter` and add it if missing to reduce user cognitive load.
