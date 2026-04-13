## 2025-02-23 - Prevent insecure deserialization in torch.load
**Vulnerability:** torch.load() without weights_only=True can execute arbitrary code during unpickling of untrusted models.
**Learning:** Using weights_only=True explicitly is critical for safe handling of external model checkpoints (e.g. LoRA, VAE).
**Prevention:** Always ensure weights_only=True is passed to all torch.load() calls.
