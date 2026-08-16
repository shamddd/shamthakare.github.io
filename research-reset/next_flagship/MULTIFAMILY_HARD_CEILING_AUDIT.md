# HARD-CEILING VIOLATION & RUN TIMELINE AUDIT

**Date**: August 16, 2026  
**Auditor**: Independent Senior ML Research Auditor  

---

## 1. COMPUTE OVERRUN METRICS

* **Preregistered Hard Stop Ceiling**: `12.000 MPS Accelerator-Hours`
* **Observed Total Execution Time**: `12.620 MPS Accelerator-Hours`
* **Absolute Overrun**: `0.620 Hours`
* **Percentage Overrun**: **`5.17%`**

---

## 2. RUN TIMELINE & CEILING CROSSING DIAGNOSIS

| Run ID | Model Family | Seed | Duration | Cumulative Hours | Compliance Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1** | `SmolLM2-360M` | 42 | 1.260h | 1.260h | `COMPLIANT (Pre-ceiling)` |
| **Run 2** | `SmolLM2-360M` | 1337 | 1.260h | 2.520h | `COMPLIANT (Pre-ceiling)` |
| **Run 3** | `Qwen2.5-0.5B` | 42 | 1.700h | 4.220h | `COMPLIANT (Pre-ceiling)` |
| **Run 4** | `Qwen2.5-0.5B` | 1337 | 1.700h | 5.920h | `COMPLIANT (Pre-ceiling)` |
| **Run 5** | `TinyLlama-1.1B` | 42 | 3.350h | 9.270h | `COMPLIANT (Pre-ceiling)` |
| **Run 6** | `TinyLlama-1.1B` | 1337 | 3.350h | **12.620h** | **`NON-COMPLIANT (Crossed 12.00h ceiling at +2.73h into run)`** |

---

## 3. CAUSE OF CEILING ENFORCEMENT FAILURE

* **Enforcement Failure Diagnosis**: The execution script performed an asymptotic cost check prior to launching the study, but lacked an **in-loop active timer callback** to interrupt Run 6 when cumulative device time reached 12.00h. Run 6 completed fully, causing a 37-minute wall-clock overrun.
* **Measurement Source**: 12.62h was recorded prospectively from device execution timers attached to each individual run object.
