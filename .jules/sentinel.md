## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed temporary file leak in API wrapper
**Vulnerability:** The code used `tempfile.NamedTemporaryFile(delete=False)` without a `try...finally` block, leaving temporary files on the filesystem if an exception occurred during processing or API requests.
**Learning:** Even within API retry loops, temporary files created with `delete=False` must be explicitly managed, as intermediate failures (e.g. image saving or parsing) bypass cleanup.
**Prevention:** Always extract the file path immediately upon creation and wrap subsequent operations in a `try...finally` block that invokes `os.remove()`.
