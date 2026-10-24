## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fix tempfile leak in prompt_extend
**Vulnerability:** The code used `tempfile.NamedTemporaryFile(delete=False)` but did not guarantee its removal if an exception occurred during subsequent MultiModalConversation processing.
**Learning:** Temporary files required for external APIs or cross-process calls must be managed carefully. If they cannot use a context manager (e.g. `delete=False` is needed), their lifecycle must be explicitly managed with a `try...finally` block.
**Prevention:** Use `fd, path = tempfile.mkstemp()` and `os.close(fd)` for safer low-level file descriptor handling, and always wrap subsequent operations in a `try...finally` block where the `finally` block executes `os.remove(path)` to prevent CWE-459.
