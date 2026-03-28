## 2026-03-28 - [Insecure Deserialization in Model Loading]
**Vulnerability:** Insecure deserialization of untrusted data via `torch.load()` without `weights_only=True`.
**Learning:** Model checkpoints (.pth, .pt) in PyTorch use pickle under the hood, which allows arbitrary code execution. Loading state dicts from external sources (like HF/Modelscope) without this flag exposes the machine to RCE.
**Prevention:** Always enforce `weights_only=True` when using `torch.load()` for loading weights/state_dicts. This restricts unpickling to standard tensor objects and primitives.
