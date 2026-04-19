## 2024-05-27 - Insecure Deserialization via torch.load

**Vulnerability:** Found multiple instances of `torch.load()` being called without `weights_only=True` to load model checkpoints (T5, CLIP, VAE, LoRA).
**Learning:** PyTorch's `torch.load()` uses Python's `pickle` by default, which can execute arbitrary code during unpickling. This is a critical security risk when loading untrusted models, particularly LoRAs downloaded from external sources.
**Prevention:** Always use `weights_only=True` with `torch.load()` when loading model state dictionaries. This restricts the unpickler to only load safe types like tensors and primitive structures.
