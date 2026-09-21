## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-18 - Fix temp file handling for Windows compatibility and security cleanup
**Vulnerability:** Temporary file handle leakage and Windows PermissionError
**Learning:** Using `delete=False` in `NamedTemporaryFile` and writing to it within the same `with` block causes simultaneous file handle access, which throws `PermissionError` on Windows. Unhandled exceptions or external interruptions before the explicit `os.remove` also cause file leaks.
**Prevention:** Always assign the file path to a variable, move writing operations outside the `with` block, and wrap subsequent logic in a `try...finally` block to guarantee cleanup on exceptions.
