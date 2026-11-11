## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-02-28 - [Sentinel] Fix Insecure Temporary File Handling in prompt_extend
**Vulnerability:** A temporary file generated using `tempfile.NamedTemporaryFile` in `DashScopePromptExpander.extend_with_img` was deleted with `os.remove()` without being wrapped in a `finally` block, creating a potential resource leak vulnerability if exceptions occur.
**Learning:** File cleanup logic that occurs outside of a context manager must always be strictly protected by `try...finally` blocks, particularly when wrapping network requests or complex parsing logic that frequently raises exceptions.
**Prevention:** When dealing with temporary files, immediately extract the filename and wrap all usage and subsequent API calls within a `try` block that corresponds with a guaranteed `finally: os.remove(fname)` branch.
