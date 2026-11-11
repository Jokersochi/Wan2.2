## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-14 - Fix Tempfile Resource Leak in MultiModalConversation
**Vulnerability:** A temporary file containing visual data in `wan/utils/prompt_extend.py` was created without proper exception handling to guarantee its deletion.
**Learning:** External API call wrappers commonly handle file cleanup sequentially after the API call finishes. Unhandled exceptions (like `KeyboardInterrupt` or unexpected dashscope errors) can bypass sequential execution, leaving unmanaged sensitive artifacts on disk.
**Prevention:** Always wrap temporary file descriptors, their writes, and associated long-running logic within a `try...finally:` block where `os.remove` is unconditionally executed.
