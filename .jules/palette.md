## 2024-05-18 - Improve CLI UX with tqdm descriptions
**Learning:** For Python CLI applications, 'Palette' UX improvements include adding context-rich descriptions (e.g., `desc=...`) to `tqdm` progress bars for long-running processes. The memory context mentions this explicitly.
**Action:** Always add `desc="Process description"` to `tqdm()` calls for improved command-line user experience, allowing users to know what process is running.
## 2025-02-12 - Better CLI Error UX for Arguments
**Learning:** In Python CLI applications, replacing raw `assert` statements used for input validation with `parser.error()` provides a significantly better user experience by outputting standard CLI usage and a clean error message, avoiding intimidating and poorly formatted Python stack traces.
**Action:** When validating CLI arguments downstream from argparse, ensure the `ArgumentParser` object is passed along or available so that `parser.error()` can be invoked to handle validation failures gracefully, with a fallback to standard exceptions when the CLI entry point is bypassed.
