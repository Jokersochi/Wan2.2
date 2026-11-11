## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.
## 2025-02-28 - Fix Temporary File Leakage in Prompt Extend
**Vulnerability:** Potential file leakage (CWE-404) in `DashScopePromptExpander.extend_with_img` where `tempfile.NamedTemporaryFile(delete=False)` was not robustly cleaned up if exceptions occurred before `os.remove`.
**Learning:** Using `delete=False` with `NamedTemporaryFile` requires rigorous manual cleanup guarantees (e.g. `try...finally`), as standard context managers (`with` blocks) do not delete the file automatically upon exit if `delete=False` is set.
**Prevention:** Always pair `NamedTemporaryFile(delete=False)` with a robust `try...finally` block that invokes `os.remove` if the file exists, ensuring cleanup even during unexpected control flow (e.g. `KeyboardInterrupt`, API failures).
