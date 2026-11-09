## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
## 2025-02-24 - CLI Error Formatting
**Learning:** Using raw assertions for argument validation in CLI tools results in intimidating AssertionError stack tracebacks, which creates a poor UX for non-technical users. Additionally, manual documentation of defaults in help strings is error-prone.
**Action:** Always use `parser.error()` for CLI argument validation to provide clean, actionable error messages, and utilize `argparse.ArgumentDefaultsHelpFormatter` to automatically surface default values in help commands.
