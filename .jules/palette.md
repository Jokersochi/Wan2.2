## 2025-02-12 - Added descriptions to tqdm progress bars
**Learning:** In CLI-based ML video generation scripts, providing contextual feedback during long-running iterations (e.g. video generation sampling or preprocessing) via descriptive text in `tqdm` progress bars significantly improves the user experience.
**Action:** When working on CLI tools with long-running iterative processes, always add `desc="..."` to `tqdm` calls to keep the user informed about what the process is currently doing.
