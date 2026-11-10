## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
## 2025-02-18 - ArgumentDefaultsHelpFormatter
**Learning:** Argument parsing UX can be quickly improved without touching every argument by simply adding `formatter_class=argparse.ArgumentDefaultsHelpFormatter`.
**Action:** Default parameter values are automatically shown in the CLI help message, making it easier for users to understand what the defaults are without guessing.
