## 2024-05-24 - CLI Progress Bar Context
**Learning:** For long-running CLI tasks like video generation sampling, a generic progress bar can leave users wondering what phase the application is currently in. Adding descriptive text to `tqdm` progress bars improves user feedback significantly.
**Action:** Always include a `desc="..."` parameter when initializing `tqdm` loops in CLI applications, especially for operations that take more than a few seconds.
