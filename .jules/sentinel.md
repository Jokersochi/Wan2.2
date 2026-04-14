## 2024-04-14 - Secure Model Loading
**Vulnerability:** Loading PyTorch checkpoints using `torch.load` without `weights_only=True` allows arbitrary code execution via unsafe deserialization (pickle).
**Learning:** PyTorch models loaded from untrusted sources (like LoRA weights or VAEs) pose a significant security risk if the unpickler is not restricted.
**Prevention:** Always enforce `weights_only=True` in all `torch.load()` calls across the repository to restrict deserialization to safe tensors and prevent RCE.
