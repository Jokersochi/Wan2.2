## 2024-05-28 - [Insecure Deserialization via torch.load]
**Vulnerability:** The application used `torch.load()` without the `weights_only=True` parameter to load model checkpoints and LoRA state dictionaries. Since `torch.load()` relies on `pickle` by default, an attacker could supply a maliciously crafted checkpoint file, resulting in arbitrary code execution during deserialization.
**Learning:** PyTorch's default `torch.load()` behavior is inherently unsafe for untrusted models because of its reliance on `pickle`. Developers must explicitly opt into the safe mode.
**Prevention:** Always use `weights_only=True` when loading state dictionaries or model weights with `torch.load()`.
