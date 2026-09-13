## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fix temporary file leakage in prompt extension
**Vulnerability:** The `DashScopePromptExpander.extend_with_img` method creates a temporary image file but does not guarantee its deletion if an unhandled exception or crash occurs before the `os.remove()` call, leading to disk exhaustion.
**Learning:** Temporary files created dynamically without a context manager must be strictly cleaned up in a `finally` block to prevent resource leaks.
**Prevention:** Always wrap temporary file handling and subsequent API/processing calls in a `try...finally` block that invokes `os.remove()` (with an existence check) when dealing with external API calls that may fail unpredictably.
