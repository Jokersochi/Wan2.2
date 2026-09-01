## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2024-09-01 - Temporary File Leak (DoS Risk)
**Vulnerability:** Unmanaged temporary files created with `delete=False` could cause disk exhaustion (Denial of Service) if execution is interrupted before cleanup.
**Learning:** Relying on sequential cleanup without a `finally` block is insecure, especially in API wrappers that can raise exceptions.
**Prevention:** Always wrap temporary file usage in a `try...finally` block that guarantees cleanup (e.g., `os.remove()`).
