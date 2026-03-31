## 2025-03-31 - Add descriptive text to tqdm progress bars
**Learning:** Adding descriptive text (`desc="..."`) to `tqdm` progress bars significantly improves the user experience during long-running iterations like video generation sampling by providing contextual feedback.
**Action:** Always add `desc` to `tqdm` calls for long-running CLI tasks.
