# STAGE 9C COMPUTE PLAN & HARD KILL CALLBACK SPEC

**Date**: August 16, 2026  

---

## 1. COMPUTE BUDGET & KILL CALLBACK

* **5 Fresh Seeds $	imes$ 5 Treatment Arms**: 25 training runs $	imes 0.025	ext{h} = 0.625$ MPS Accelerator-Hours.
* **Evaluation (Untouched Math Subset)**: $0.175$ MPS Accelerator-Hours.
* **Projected Total**: **0.800 MPS Accelerator-Hours**.
* **Hard Ceiling**: **2.500 MPS Accelerator-Hours**.
* **Kill Callback**: Active process-level `SIGTERM`/`SIGKILL` callback if cumulative execution exceeds 2.500h.
