## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-03-09 - Fix temporary file leak in prompt extension
**Vulnerability:** Insecure handling of temporary files created with `delete=False` without a `finally` block, leading to disk exhaustion or DoS if exceptions (like memory limits, interrupt signals, or unexpected API errors) disrupt execution flow before manual removal.
**Learning:** Temporary files in long-running ML processes, especially when handling user inputs (images), are highly susceptible to leaking on errors.
**Prevention:** Always wrap temporary file operations involving `delete=False` in a `try...finally` block that invokes `os.remove()`.
