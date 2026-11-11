## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fix Temporary File Leak in API Wrapper
**Vulnerability:** Temporary files created with `delete=False` were subject to leakage (DoS risk) if an exception was raised before reaching `os.remove()`.
**Learning:** Temporary files that outlive a context manager block must have their lifecycle carefully managed via rigorous error handling.
**Prevention:** Always wrap temporary file creation and dependent logic in a `try...finally` block. Ensure the file path is assigned to a tracking variable immediately upon creation, so the `finally` block can reliably clean it up.
