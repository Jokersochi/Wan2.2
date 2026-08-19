## 2024-08-19 - Do not use assert for API response validation in Python
**Vulnerability:** Found `assert response.status_code == HTTPStatus.OK` being used to check Dashscope API responses in `wan/utils/prompt_extend.py`.
**Learning:** Python `assert` statements are stripped out when the code is executed with optimization flags (`-O`). Using them for runtime validation, API response checks, or critical state logic is a vulnerability as the checks will silently pass in optimized environments, leading to unhandled errors or data leakage.
**Prevention:** Always use explicit `if` statements and raise specific exceptions (e.g., `RuntimeError`, `ValueError`) for runtime validation to ensure these checks are enforced in production regardless of optimization flags.
