## 2024-04-10 - Add descriptions to CLI progress bars
**Learning:** For command-line-driven AI video generation tools where iterations are extremely long (e.g., diffusion sampling), raw `tqdm` progress bars without descriptions leave users uncertain about the current execution phase.
**Action:** Always add explicit contextual feedback (e.g., `desc="Sampling"`) to `tqdm` instantiations in core loops (like `wan/text2video.py` and `wan/animate.py`) to improve CLI user experience and state visibility.
