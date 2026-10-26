## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2024-10-26 - Fix temporary file leak (CWE-459) in PromptExpander
**Vulnerability:** Insecure temporary file creation and cleanup using `tempfile.NamedTemporaryFile` with `delete=False` followed by `os.remove` at the end of the method execution.
**Learning:** If an exception occurs (e.g., during the external API call), the method exits early and `os.remove` is never executed, leaving the temporary file on disk. Repeated occurrences can lead to a disk exhaustion attack (Denial of Service).
**Prevention:** Use `fd, path = tempfile.mkstemp()`, immediately close the file descriptor `os.close(fd)`, and wrap all subsequent file operations in a `try...finally` block. Perform the cleanup `os.remove(path)` within the `finally` block to guarantee removal regardless of exceptions.
