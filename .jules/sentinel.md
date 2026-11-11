## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-01-01 - Fix Insecure Temporary File Creation and Cleanup (CWE-459)
**Vulnerability:** `tempfile.NamedTemporaryFile(delete=False)` was used and then manually deleted at the end of the function, which could result in a temporary file leak if an unhandled exception occurred before `os.remove(fname)`.
**Learning:** Functions that perform network calls or complex logic can fail unexpectedly. Relying on manual deletion at the end of a block without `finally` leaves temporary files leaked on disk.
**Prevention:** Use `tempfile.mkstemp()`, immediately `os.close(fd)`, and wrap all subsequent operations in a `try...finally` block with `os.remove(path)` in the `finally` clause.
