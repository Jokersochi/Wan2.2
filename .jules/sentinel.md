## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed insecure temporary file handling in API processing pipeline
**Vulnerability:** The temporary file created via `tempfile.NamedTemporaryFile(delete=False)` was removed with a plain `os.remove(fname)` at the end of the `extend_with_img` function. If an exception occurred during the `dashscope` API call or subsequent processing that was not caught (or if a `KeyboardInterrupt` occurred), the function would exit without executing `os.remove(fname)`, causing temporary files to leak on the filesystem (DoS risk over time).
**Learning:** When using `delete=False` with temporary files, manual cleanup using `os.remove` is inherently unsafe unless enclosed within a `try...finally` block.
**Prevention:** Always pair temporary file creation (when `delete=False`) with a `try...finally` structure that ensures `os.remove()` is called regardless of any preceding execution errors.
