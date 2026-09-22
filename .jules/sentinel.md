## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed temporary file leakage vulnerability
**Vulnerability:** The temporary file created for `extend_with_img` was not properly cleaned up in a `try...finally` block. Unhandled exceptions during the API call could result in resource exhaustion.
**Learning:** File operations with `delete=False` must always guarantee cleanup using a `try...finally` block.
**Prevention:** Use `try...finally` wrapped around the entire operational block when utilizing `NamedTemporaryFile(delete=False)`.
