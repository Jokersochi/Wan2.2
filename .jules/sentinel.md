## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed temporary file leak in DashScopePromptExpander
**Vulnerability:** Used `tempfile.NamedTemporaryFile(delete=False)` followed by API calls, with `os.remove(fname)` at the end. If an exception occurred during the API call or any intermediate processing, the `os.remove()` was bypassed, causing a file leak (CWE-459).
**Learning:** External libraries (like DashScope API) can throw unexpected exceptions, breaking the sequential cleanup logic.
**Prevention:** Use `fd, path = tempfile.mkstemp()`, immediately close the `fd`, and wrap subsequent operations in a `try...finally` block with `os.remove(path)` in the `finally` clause to guarantee cleanup regardless of exceptions.
