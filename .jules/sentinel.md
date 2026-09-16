## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed tempfile resource leak in DashScopePromptExpander
**Vulnerability:** A temporary file was created using `tempfile.NamedTemporaryFile(delete=False)` and its removal `os.remove()` was placed at the end of the method body. If an unhandled exception occurred during processing, the file would remain on disk, potentially causing disk exhaustion over time.
**Learning:** Temporary files created without auto-deletion must always be handled within a `try...finally` block.
**Prevention:** Always pair `NamedTemporaryFile(delete=False)` with a `try...finally` block to ensure cleanup via `os.remove()`, even if the program throws exceptions.
