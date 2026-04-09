## 2024-05-18 - [Add descriptive text to CLI progress bars]
**Learning:** For CLI-based tools, particularly those involving long-running machine learning generation loops, empty progress bars provide insufficient system status visibility. By explicitly leveraging `tqdm(..., desc="...")`, we can instantly transform an ambiguous counter into a clear indicator of system state, significantly improving UX.
**Action:** Always verify if instances of `tqdm()` in long-running loops utilize the `desc` argument to provide contextual feedback to the user.
