## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
## 2025-01-20 - Friendly CLI Errors & Auto-Defaults
**Learning:** Raw `assert` statements inside application execution logic throw intimidating `AssertionError` tracebacks when users provide invalid arguments or environments. Additionally, CLI users often guess default values without checking source code when they aren't printed in the `--help` menu.
**Action:** Replace runtime `assert` validations with `argparse.ArgumentParser.error()` for clean, user-friendly error messages that print usage instructions. Always add `formatter_class=argparse.ArgumentDefaultsHelpFormatter` to `argparse.ArgumentParser` so `--help` clearly communicates default behaviors.
