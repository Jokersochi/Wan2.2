## 2025-02-12 - Added descriptions to tqdm progress bars
**Learning:** In CLI applications, especially those generating videos where rendering each frame or processing each step can take significant time, progress bars without contextual descriptions leave users guessing about what is happening.
**Action:** Always add descriptive text (e.g., `desc="..."`) to `tqdm` progress bars for long-running iterations to improve user experience.
