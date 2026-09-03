## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix temporary file leakage in prompt extend
**Vulnerability:** The code used `tempfile.NamedTemporaryFile(delete=False)` to save temporary image files before sending them to the Dashscope API, but it didn't use a `finally` block for cleanup. If an exception occurred during request preparation or execution, the temporary file remained on disk indefinitely, leading to a denial-of-service (DoS) risk through disk exhaustion.
**Learning:** When handling temporary files in API wrappers or processing pipelines (e.g., using `tempfile.NamedTemporaryFile(delete=False)`), always wrap the subsequent logic in a `try...finally` block that invokes `os.remove()` to guarantee file cleanup.
**Prevention:** Use `try...finally` to ensure `os.remove()` is called, checking if the file exists first if necessary.
