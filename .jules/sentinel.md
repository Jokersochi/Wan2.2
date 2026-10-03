## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2026-10-03 - [Sentinel] Fixed insecure assert usage in generate.py
**Vulnerability:** The code used `assert` statements to validate input arguments and configuration parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, bypassing crucial validation.
**Learning:** Command line argument and input validation should always use explicit control flow and exceptions to guarantee execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError`) instead of `assert` to handle validation in production code environments.
