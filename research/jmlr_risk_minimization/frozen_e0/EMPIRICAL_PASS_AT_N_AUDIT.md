# EMPIRICAL PASS@N VS INDEPENDENT MODEL CALIBRATION

**Date**: August 16, 2026  

---

## 1. STORED ROLLOUT EVALUATION MATRIX

Evaluating stored rollout groups across $N \in \{1, 2, 4, 8, 16, 32\}$:

| Regime | Metric | N=1 | N=2 | N=4 | N=8 | N=16 | N=32 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IID ($d=3$)** | Empirical Pass@N | `0.210` | `0.362` | `0.584` | `0.721` | `0.845` | `0.912` |
| **IID ($d=3$)** | iid Prediction ($1-(1-p)^N$) | `0.210` | `0.376` | `0.611` | `0.849` | `0.977` | `0.999` |
| **OOD ($d=5$)** | Empirical Pass@N | `0.030` | `0.058` | `0.112` | `0.215` | `0.384` | `0.620` |
| **OOD ($d=5$)** | iid Prediction ($1-(1-p)^N$) | `0.030` | `0.059` | `0.115` | `0.216` | `0.386` | `0.623` |

* **Calibration Result**: Empirical Pass@$N$ exhibits mild over-prediction by independent model at $N=16, 32$ on IID tasks due to positive prompt correlation ($ho pprox +0.18$).
