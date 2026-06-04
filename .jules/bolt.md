
## 2026-06-04 - [Memoization of Global Accuracy and Speed]
**Learning:** `mnStatsStreak` and `mnStatsAccuracy` were performing redundant normalizations of review logs (`mnNormalizeReviewLogs`) inside every render, taking a toll on rendering performance especially since logs grow over time. Moreover, inline `reduce` computations for accuracy and latency within JSX evaluated on every render.
**Action:** Reorder memoization to compute the normalized log once and reuse it across multiple stat functions. Extract and memoize heavy array reduction operations (like speed and accuracy calculations) so they only recalculate when logs actually update.
