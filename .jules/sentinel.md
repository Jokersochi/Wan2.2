## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2024-11-06 - Prevent temporary file resource leak and PermissionErrors
**Vulnerability:** `tempfile.NamedTemporaryFile(delete=False)` was used without guaranteed cleanup in a `try...finally` block, leading to CWE-459 (file leaks) if an error occurred during subsequent operations. Additionally, holding the file open via `NamedTemporaryFile` can cause Windows `PermissionError` when external libraries (like `PIL`) attempt to write to it.
**Learning:** External integrations and manual error handling loops often fail to reach manual `os.remove` calls when unexpected exceptions arise. Cross-platform file locking behaviors differ significantly.
**Prevention:** Always prefer `fd, path = tempfile.mkstemp()`, immediately call `os.close(fd)` to prevent lock conflicts, and wrap all subsequent usage in a `try...finally` block to strictly enforce file deletion via `os.remove()`.
