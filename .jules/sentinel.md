## 2025-02-18 - Insecure Deserialization via torch.load
**Vulnerability:** The codebase was loading PyTorch models using `torch.load` without `weights_only=True`, which is an insecure deserialization vulnerability that could allow arbitrary code execution when loading an untrusted model checkpoint.
**Learning:** PyTorch models loaded without `weights_only=True` can deserialize executable code in the pickle format. This vulnerability existed due to legacy PyTorch practices where `weights_only` wasn't enabled by default.
**Prevention:** Always use `weights_only=True` when loading model weights using `torch.load` unless executing arbitrary code is specifically intended, or use safetensors as a more secure model distribution format.
