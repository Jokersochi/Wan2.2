## 2025-05-24 - [Replaced assert-based validation with ValueError in generate.py]
**Vulnerability:** The codebase relies on `assert` statements in `generate.py` for input validation and state checking (e.g., verifying `args.ckpt_dir`, `args.task`, etc.).
**Learning:** `assert` statements are stripped when Python runs with optimization (`-O` or `-OO`). This removes all these checks during production, potentially allowing invalid states that could lead to crashes, unexpected behaviors, or other unhandled vulnerabilities.
**Prevention:** Always use explicit conditional statements (e.g., `if not condition: raise ValueError("...")`) for any critical input validation or security logic, rather than relying on `assert`.
