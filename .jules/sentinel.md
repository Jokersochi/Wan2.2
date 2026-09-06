## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed insecure temporary file cleanup
**Vulnerability:** A `tempfile.NamedTemporaryFile` was created with `delete=False`, and `os.remove` was called at the end of the method. If an exception occurred during the API call or string formatting that was not caught or propagated (e.g. `KeyboardInterrupt` or unexpected error outside the try block), the file would remain on disk, potentially leading to disk exhaustion and Denial of Service (DoS).
**Learning:** Temporary files that disable auto-deletion must be explicitly cleaned up in a `finally` block to ensure execution regardless of exceptions in the intervening logic.
**Prevention:** Always wrap the logic following the creation of a persistent temporary file in a `try...finally` block that invokes `os.remove()` to guarantee cleanup.
