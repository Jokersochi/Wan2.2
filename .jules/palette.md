## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
## 2024-11-11 - CLI Argument Validation UX
**Learning:** Using raw `assert` statements for validating CLI inputs produces intimidating and unhelpful `AssertionError` tracebacks for end-users.
**Action:** Replace `assert` statements used for argument validation with `parser.error()` and use `argparse.ArgumentDefaultsHelpFormatter` to automatically display default values in the help message. This ensures standard CLI error messages and usage instructions.
