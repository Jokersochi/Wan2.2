## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - Insecure Temporary File Handling in prompt_extend
**Vulnerability:** Use of `tempfile.NamedTemporaryFile` and passing `delete=False` without wrapping the cleanup in a `try/finally` block.
**Learning:** `NamedTemporaryFile` locks the file on Windows and the lack of a `try/finally` block leads to file leaks (CWE-459) if an exception occurs before `os.remove(fname)`.
**Prevention:** Use `tempfile.mkstemp()`, immediately close the file descriptor `os.close(fd)`, and wrap file operations in a `try...finally` block that removes the file in `finally:`.
