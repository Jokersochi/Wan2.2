## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed insecure temporary file handling and potential leak
**Vulnerability:** In `wan/utils/prompt_extend.py`, `tempfile.NamedTemporaryFile` was used to create an image file path passed to an external library, and cleanup was handled manually with `os.remove`. This posed a CWE-459 (Incomplete Cleanup) risk because if an exception occurred prior to `os.remove`, the file would leak.
**Learning:** Manual file cleanup is prone to failure in exception paths. `NamedTemporaryFile` can also have cross-platform issues when the file needs to be read/written by another process while still open.
**Prevention:** Use `fd, path = tempfile.mkstemp()`, immediately close the descriptor with `os.close(fd)`, and wrap all subsequent operations using the path in a `try...finally` block that strictly calls `os.remove()` in the `finally` clause.
