## 2025-03-05 - Add informative progress bars using tqdm desc parameter
**Learning:** For long-running CLI tasks like video generation sampling, users may stare at a plain progress bar without understanding what stage of the process they are in.
**Action:** Always add contextual feedback to `tqdm` instances using the `desc="..."` parameter (e.g. `desc="Sampling steps"`) to provide clear visual cues and significantly improve the CLI user experience.
