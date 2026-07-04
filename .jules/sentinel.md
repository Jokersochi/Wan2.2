## 2024-05-20 - Insecure Deserialization in PyTorch
**Vulnerability:** `torch.load()` was used without `weights_only=True` to load model weights.
**Learning:** PyTorch's default `torch.load()` can execute arbitrary code during deserialization if `weights_only=True` is not specified, posing a critical security risk when loading untrusted checkpoints.
**Prevention:** Always enforce `weights_only=True` in all `torch.load()` calls across the repository to restrict the unpickler from executing arbitrary code.
