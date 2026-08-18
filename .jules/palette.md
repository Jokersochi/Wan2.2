## 2024-05-24 - CLI Error Handling
**Learning:** Raw assert statements for argument validation result in confusing stack traces. Using `parser.error()` provides a clean, usage-aware error message with a standard exit code.
**Action:** Always use `parser.error()` for manual argument validation in argparse applications.
