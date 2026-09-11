## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fix Temporary File Leak in PromptExpander
**Vulnerability:** Use of `tempfile.NamedTemporaryFile(delete=False)` without a wrapping `try...finally` block can cause file leakage if exceptions are raised before `os.remove()` is called, leading to DoS via disk space exhaustion.
**Learning:** When managing temporary files manually, file cleanup logic must be guaranteed to run regardless of the execution path.
**Prevention:** Always wrap the logic immediately following temporary file creation in a `try...finally` block that handles the file deletion.
