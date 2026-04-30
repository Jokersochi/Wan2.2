## 2024-05-24 - [Fix torch.load() Insecure Deserialization Vulnerability]
**Vulnerability:** Found `torch.load()` being used to load model checkpoint weights without `weights_only=True` parameter.
**Learning:** PyTorch models heavily rely on `torch.load()` which uses the unsafe Python `pickle` module by default to deserialize objects. This can lead to arbitrary code execution if a maliciously crafted checkpoint is loaded.
**Prevention:** Always use `weights_only=True` when calling `torch.load()` unless you specifically need to load more complex Python objects, and you completely trust the source of the file. PyTorch >2.4.0 supports this.
