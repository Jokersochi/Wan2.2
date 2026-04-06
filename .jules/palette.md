## 2024-05-24 - CLI Contextual Feedback
**Learning:** Adding descriptive text (`desc="..."`) to `tqdm` progress bars in CLI tools significantly improves the user experience during long-running processes like video generation sampling by providing contextual feedback.
**Action:** Always include a `desc` parameter when initializing `tqdm` loops for potentially slow iterations.
