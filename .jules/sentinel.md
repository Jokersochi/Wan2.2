## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - [Sentinel] Fixed temporary file leak (CWE-459) in DashScopePromptExpander
**Vulnerability:** `tempfile.NamedTemporaryFile(delete=False)` was used for an image path to pass to an API call, and cleanup (`os.remove`) was delayed until the end of the API call process, which could raise an Exception before cleanup was reached.
**Learning:** External API errors or process interruptions would leave `.png` files permanently in `/tmp`, consuming disk space over time.
**Prevention:** Use `tempfile.mkstemp` instead, immediately close the file descriptor, and wrap subsequent operations in a `try...finally` block that handles the cleanup.
