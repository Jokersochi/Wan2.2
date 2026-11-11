## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fixed temporary file leak in DashScopePromptExpander
**Vulnerability:** The code created a temporary file with `delete=False` but failed to use a `try...finally` block, which could cause a file leak if an exception was raised during API calls.
**Learning:** Always use `try...finally` when managing temporary files manually, particularly in APIs that can fail and raise exceptions.
**Prevention:** Ensure explicit `try...finally` is used alongside manual temporary file creation or switch to auto-deleting mechanisms when possible.
