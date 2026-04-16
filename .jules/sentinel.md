## 2024-05-15 - [Insecure Deserialization via torch.load]
**Vulnerability:** Found multiple instances of `torch.load` loading model weights without `weights_only=True`, allowing arbitrary code execution if a malicious checkpoint is loaded.
**Learning:** The application's architecture frequently loads checkpoints (VAE, T5, CLIP, LoRA) dynamically. Omitting `weights_only=True` exposes users to critical insecure deserialization vulnerabilities, especially given the current AI threat landscape involving malicious model weights.
**Prevention:** Explicitly enforce `weights_only=True` on all `torch.load()` calls unless deserializing arbitrary objects is strictly necessary. Use safer serialization formats like `safetensors` when possible.
