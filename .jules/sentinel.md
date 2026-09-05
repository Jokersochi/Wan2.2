## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed temporary file leak DoS vulnerability
**Vulnerability:** A temporary file was created with `delete=False` and the `os.remove` call was not wrapped in a `try...finally` block. If an exception occurred during the API call or string processing, the file would not be deleted, leading to disk exhaustion and a potential Denial of Service (DoS) attack.
**Learning:** File cleanup logic must be guaranteed to execute regardless of successful execution or exception.
**Prevention:** Always wrap temporary file usage in a `try...finally` block that invokes `os.remove()` to ensure cleanup.
