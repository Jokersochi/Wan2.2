## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed insecure temporary file handling (CWE-459)
**Vulnerability:** The code used `tempfile.NamedTemporaryFile(delete=False)` to save temporary images. If an exception occurred during the DashScope API call or subsequent processing, `os.remove(fname)` was bypassed, leaving the temporary file on disk permanently (Resource Leak).
**Learning:** `delete=False` in `NamedTemporaryFile` requires explicit cleanup, but unhandled exceptions can skip cleanup logic unless placed inside a `finally` block.
**Prevention:** Always use `tempfile.mkstemp` and explicitly close the file descriptor, then wrap all operations involving the file path in a `try...finally` block with `os.remove(path)` in the `finally` clause to guarantee cleanup on success or failure.
