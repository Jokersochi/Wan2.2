## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix temp file leak in DashScopePromptExpander
**Vulnerability:** `NamedTemporaryFile(delete=False)` was used without a `try...finally` block. If an exception occurred during the external API call, the temporary file would not be deleted, leading to a file descriptor and disk space leak (potential Denial of Service).
**Learning:** Resource management must always account for exceptional control flow, particularly around external service calls.
**Prevention:** Always wrap code blocks manipulating temporary files (especially `delete=False`) in `try...finally` statements that guarantee file removal via `os.remove()`.
