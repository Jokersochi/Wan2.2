## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed insecure temporary file leak
**Vulnerability:** `tempfile.NamedTemporaryFile` with `delete=False` was used without guaranteed cleanup on error.
**Learning:** The cleanup `os.remove(fname)` would be bypassed if an exception occurred before reaching it, leading to file leaks (CWE-459).
**Prevention:** Use `tempfile.mkstemp()`, immediately close the descriptor, and wrap subsequent operations in a `try...finally` block with `os.remove(path)` in the `finally` clause.
