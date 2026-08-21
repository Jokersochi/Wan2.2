## 2024-08-21 - Replace assert with argparse error in CLI
**Learning:** Raw assert statements for user input validation (like CLI arguments) result in ugly stack traces that confuse users. Using argparse's `parser.error()` correctly communicates input errors and displays usage instructions, improving the CLI developer UX significantly.
**Action:** Replace `assert` statements used for validation with `parser.error()` when dealing with command-line arguments in CLI applications.
