## 2025-02-28 - Clean up command-line validation
**Learning:** Using raw `assert` statements to validate arguments in CLI python scripts can cause jarring stack traces for users and limits the UX. Instead, `parser.error("msg")` natively uses `argparse` to format a clean error message and gracefully exit the program with standard error status.
**Action:** When validating CLI inputs constructed with `argparse`, prefer passing the parser down to validation logic so it can raise `parser.error` over raw assertions.
