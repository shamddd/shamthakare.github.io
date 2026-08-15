# COLLISION AUDIT: ROBERTS ET AL. (2026, arXiv:2604.01411)

**Date**: August 16, 2026  
**Auditor**: Lead Scientific Novelty Auditor  

---

## 1. COMPREHENSIVE EXTRACTION OF ROBERTS ET AL. (2026)

* **Reference**: Roberts et al., *"Test-Time Scaling Makes Overtraining Compute-Optimal"*, arXiv:2604.01411 (2026).
* **Core Contribution**: Jointly optimizes training tokens, model size, and inference-time search samples under end-to-end compute budgets. Demonstrates that including downstream test-time inference compute changes the compute-optimal pre-training / fine-tuning duration (overtraining becomes compute-optimal to reduce serving costs).
* **Relevance & Collision Boundary**:
  - Proves that joint training-inference FLOP optimization is **already occupied prior art in 2026**.
  - Establishes that over-training models to minimize inference search cost is a known phenomenon.

*Conclusion*: Broad claims that "training decisions should change when downstream inference costs are included" are **OCCUPIED BY ROBERTS ET AL. (2026)**.
