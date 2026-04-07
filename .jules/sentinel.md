## 2025-04-07 - Insecure Deserialization in PyTorch Model Loading
**Vulnerability:** Found multiple instances of `torch.load` loading model weights without the `weights_only=True` parameter.
**Learning:** PyTorch's default `torch.load` uses Python's `pickle` module, which is inherently insecure and allows arbitrary code execution if a maliciously crafted pickle file is loaded.
**Prevention:** Always use `weights_only=True` when loading state dictionaries or model weights via `torch.load()` to ensure only safe tensor data is deserialized.
