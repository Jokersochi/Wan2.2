## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2024-10-31 - Automatic Default Values in Python CLI

**Learning:** Users of complex generative AI CLI tools (like Wan2.2) often struggle to remember the default values for numerous configuration parameters (like checkpoint paths, model types, or sampling steps). Without explicitly declaring `formatter_class=argparse.ArgumentDefaultsHelpFormatter`, they must either guess the default behavior or consult the source code when they run `--help`.

**Action:** Whenever implementing or reviewing Python CLI scripts that use `argparse` with multiple configurable arguments, proactively include `formatter_class=argparse.ArgumentDefaultsHelpFormatter` in the `ArgumentParser` instantiation. This immediately reduces cognitive load and improves accessibility by making the help output self-documenting regarding default state.
