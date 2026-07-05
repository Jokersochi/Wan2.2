## 2024-05-24 - [Fix insecure torch.load calls]
**Vulnerability:** Insecure deserialization via `torch.load()` without `weights_only=True`. Loading untrusted model checkpoints (like LoRA weights or VAE models) could result in arbitrary code execution.
**Learning:** `torch.load` defaults to using the `pickle` module which is inherently unsafe if the input is untrusted. By not enforcing `weights_only=True`, the application is open to a critical vulnerability if users load external/untrusted models.
**Prevention:** Always explicitly enforce `weights_only=True` in all `torch.load()` calls across the repository to restrict the unpickler from executing arbitrary code.
