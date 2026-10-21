## 2026-10-21 - Insecure temporary file handling (CWE-459)
**Vulnerability:** Incomplete cleanup and unsafe re-opening of `tempfile.NamedTemporaryFile(delete=False)` in image processing.
**Learning:** Even though `os.remove` was at the end of the method, if the wrapped process (like an external API call or parsing) raised an exception, the file was permanently left on disk, creating a resource leak and Denial of Service vector.
**Prevention:** Always use `fd, path = tempfile.mkstemp()` with an immediate `os.close(fd)` for files passed to external tools by name, and guarantee cleanup by placing `os.remove(path)` inside a `finally` block.
