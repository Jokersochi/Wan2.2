## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix temporary file leakage in prompt extend
**Vulnerability:** Insecure handling of `tempfile.NamedTemporaryFile(delete=False)` where the subsequent `os.remove()` call was placed outside a `finally` block. This could lead to temporary file leakage (resource exhaustion DoS) if an unhandled exception occurred before the cleanup.
**Learning:** External API interactions and complex logic flows enclosed between temporary file creation and manual deletion create high risk for resource exhaustion if unhandled exceptions break the execution path.
**Prevention:** Always wrap manual temporary file cleanup logic inside a `try...finally` block immediately after file creation to guarantee removal under all execution paths.
