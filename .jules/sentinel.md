## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix temporary file leakage in prompt extension
**Vulnerability:** The `DashScopePromptExpander.extend_with_img` method created temporary files using `tempfile.NamedTemporaryFile(delete=False)` and relied on deleting them after a network API call, without an enclosing `try...finally` block. If the API call triggered an unhandled exception, the temporary file would be leaked, leading to disk exhaustion and potential DoS vectors over time.
**Learning:** File cleanup operations, especially for temporary files created during network requests or complex processing, must be strictly guaranteed regardless of execution flow.
**Prevention:** Always wrap temporary file processing logic in a `try...finally` block to guarantee that `os.remove()` is called, even if exceptions are raised during execution.
