## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - Fix Tempfile Leak in API Integration
**Vulnerability:** Temporary files created with `delete=False` were not cleaned up if an exception occurred during external API calls, leading to potential disk space exhaustion (DoS).
**Learning:** External API calls are prone to unhandled exceptions (e.g., `KeyboardInterrupt`). When combined with persistent temporary files, this leads to silent resource leaks.
**Prevention:** Always wrap temporary file processing logic in a `try...finally` block that invokes `os.remove()` to guarantee file cleanup.
