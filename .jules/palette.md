## 2025-02-18 - Improved CLI Error Messaging
**Learning:** Raw `assert` statements in argument validation logic produce unhelpful Python stack traces for end users.
**Action:** Replaced `assert` with `parser.error()` fallback to `ValueError` for cleaner, more intuitive command-line error messages.
## 2025-02-18 - Avoid Variable Scope Issues when Relocating Code
**Learning:** When moving validation logic out of an application loop (like `generate()`) into a dedicated argument parsing/validation function, it is critical to trace the local variable dependencies of the relocated code.
**Action:** Always ensure any configurations (like `cfg`) or environment variables evaluated in the original check are also instantiated in the new scope before the relocated validation executes.
