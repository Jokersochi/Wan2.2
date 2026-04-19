## 2024-10-25 - Insecure Deserialization via torch.load
**Vulnerability:** Calling `torch.load()` without `weights_only=True` allows the underlying pickle implementation to execute arbitrary code during model deserialization.
**Learning:** PyTorch defaults to full pickle deserialization for legacy compatibility, which creates critical RCE vulnerabilities when loading untrusted weights like community LoRAs or checkpoints.
**Prevention:** Always enforce `weights_only=True` in all `torch.load()` calls to restrict deserialization to safe data structures (tensors, dicts, lists) and prevent arbitrary code execution.
