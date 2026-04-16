## 2024-04-16 - Add tqdm descriptions for CLI clarity
**Learning:** Adding `desc="..."` to `tqdm` loops in long-running CLI tools (like video generation and retargeting loops) significantly improves user experience by clarifying exactly what operation is being processed. This is a reusable UX pattern for CLI-based AI scripts.
**Action:** Always verify `tqdm` usages in command-line iterations have contextual descriptions attached.
