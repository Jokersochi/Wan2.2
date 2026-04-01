## 2024-05-24 - Added descriptive text to tqdm progress bars
**Learning:** In CLI-based generative tools, long-running iterations like diffusion sampling can feel unresponsive without context. Adding descriptive text to `tqdm` progress bars (e.g., `desc="Sampling steps"`) significantly improves the user experience by providing clear contextual feedback on what process is currently running.
**Action:** Always include a `desc` argument when using `tqdm` for long-running processes in CLI applications to ensure users understand what the progress bar represents.
