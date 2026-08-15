## 2024-05-24 - Do not use assert for API response validation
**Vulnerability:** API response validation checks were performed using `assert` statements (`assert response.status_code == HTTPStatus.OK`).
**Learning:** Python `assert` statements are ignored when the code is executed with optimization flags (e.g., `-O`). This causes runtime security checks and API response validations to be completely bypassed in production environments.
**Prevention:** Always use explicit `if` statements and raise specific exceptions (like `RuntimeError` or `ValueError`) for critical state logic and API validations to ensure they are enforced regardless of optimization flags.
