## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2024-11-09 - Insecure Temporary File Creation Fix
**Vulnerability:** Insecure temporary file creation in `/tmp` using random names (CWE-377, CWE-459).
**Learning:** Using `tempfile.NamedTemporaryFile()` for file paths passed to external libraries (like `imageio`) causes `PermissionError` on Windows because the file remains open.
**Prevention:** Always use `fd, path = tempfile.mkstemp()`, immediately call `os.close(fd)`, and explicitly clean up the file using `os.remove(path)` inside a `try...finally` block to prevent file leaks (CWE-459).
