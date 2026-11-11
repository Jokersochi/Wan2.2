## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix temporary file resource leak in DashScopePromptExpander
**Vulnerability:** The `extend_with_img` function created a temporary image file with `delete=False` and only removed it at the end of the function. If an exception occurred during the request or formatting loop that broke out of the function entirely, the temporary file would not be cleaned up, leading to a resource leak (local DoS). Additionally, file I/O within the `with` block could cause PermissionError on some operating systems.
**Learning:** Always use a `try...finally` block to guarantee the cleanup of temporary files regardless of exceptions. When using `NamedTemporaryFile(delete=False)`, extract the filename first, perform operations outside the `with` block, and ensure `os.remove` is invoked in the `finally` clause.
**Prevention:** Enforce secure coding practices by consistently pairing temporary file creation with deterministic `try...finally` cleanup routines.
