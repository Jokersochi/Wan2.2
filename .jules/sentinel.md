## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-05-24 - Missing Cleanup of Temporary Files
**Vulnerability:** A DoS risk was found in `wan/utils/prompt_extend.py` where a temporary file was created using `tempfile.NamedTemporaryFile(delete=False)` without being wrapped in a `try...finally` block. If the subsequent logic (like an external API call) raises an exception, the script terminates or handles the error without deleting the file, eventually exhausting disk space.
**Learning:** This codebase handles external file IO often during prompt formatting, image processing, or merging operations. Standard practice must guarantee file cleanup regardless of success or failure.
**Prevention:** Always wrap logic immediately following explicit file creation or manipulation with temporary files into a `try...finally` block that verifies existence and deletes the file using `os.remove()`.
