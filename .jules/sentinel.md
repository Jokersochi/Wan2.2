## 2025-02-23 - Insecure Deserialization in torch.load
**Vulnerability:** Found multiple instances of `torch.load()` without `weights_only=True`, which can allow arbitrary code execution when loading untrusted checkpoints.
**Learning:** Always explicitly enforce `weights_only=True` in all `torch.load()` calls across the repository to prevent insecure deserialization vulnerabilities, especially when handling untrusted model checkpoints (e.g., LoRA weights or VAE models).
**Prevention:** Lint or automatically check new `torch.load` calls to require `weights_only=True`.
