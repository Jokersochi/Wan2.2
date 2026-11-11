## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2024-09-07 - Temporary File Resource Exhaustion (DoS)
**Vulnerability:** A temporary file created with `delete=False` was being deleted at the end of a function, but without a `finally` block, leaving it vulnerable to being leaked if an exception occurred midway.
**Learning:** When API calls or other complex logic fail, they can skip cleanup steps at the end of the function, leading to disk exhaustion over time (DoS).
**Prevention:** Always wrap logic immediately following `tempfile.NamedTemporaryFile(delete=False)` in a `try...finally` block that securely removes the file.
