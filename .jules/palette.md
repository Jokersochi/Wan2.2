## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
