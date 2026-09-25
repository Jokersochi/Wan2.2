## 2025-02-28 - [Sentinel] Fixed insecure assert usage in DashScopePromptExpander
**Vulnerability:** The code used `assert` statements to validate HTTP response status codes and task parameters. When Python is executed with the `-O` optimization flag, these statements are ignored, potentially bypassing crucial logic or error handling for external API interactions.
**Learning:** External API validation should always use explicit control flow and exceptions to guarantee reliable error state execution.
**Prevention:** Use explicit `if` statements coupled with context-appropriate standard exceptions (like `ValueError` or `RuntimeError`) instead of `assert` to handle validation in production code environments.

## 2025-03-01 - [Sentinel] Fixed insecure assert usage in CLI argument validation
**Vulnerability:** The `generate.py` script used `assert` statements to validate critical command-line arguments and distributed execution parameters. When Python is executed with the `-O` optimization flag, these `assert` statements are stripped from the bytecode, entirely bypassing argument validation and allowing the program to execute with invalid or missing inputs, which can lead to unpredictable behavior, resource exhaustion, or runtime crashes.
**Learning:** Argument parsing and environment validation logic must never rely on `assert`. In CLI applications, `assert` should only be used for internal invariants, not for validating user input or external configuration.
**Prevention:** Use the `argparse.ArgumentParser.error()` method to gracefully handle invalid arguments during parsing. For runtime or environment checks, use explicit `if` statements that raise `ValueError` or `RuntimeError` to ensure validation logic remains active even in optimized execution environments.
