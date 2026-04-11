## 2024-05-24 - CLI Progress Bar UX
**Learning:** For Python CLI applications with long-running iterative processes (like diffusion model sampling), bare `tqdm` progress bars can be opaque and confusing.
**Action:** Always utilize the `desc` parameter in `tqdm` (e.g., `desc="Sampling"`) to provide users with clear context about the current stage of the CLI process.
