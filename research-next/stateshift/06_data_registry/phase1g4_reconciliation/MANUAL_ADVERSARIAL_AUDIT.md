# MANUAL ADVERSARIAL AUDIT REPORT (SEED 20260817)

**Sample Size**: $N = 60$ prospective pairs sampled randomly using fixed seed `20260817`  

---

## 1. Adversarial Audit Results

| Adversarial Evaluation Question | Yes Count ($N$) | Denominator | Percentage (%) | Audit Assessment |
| :--- | :---: | :---: | :---: | :--- |
| **1. Is $S_C$ mathematically coherent?** | `60` | `60` | `100.0%` | Valid reference solution equation step |
| **2. Is $S_R$ mathematically coherent?** | `60` | `60` | `100.0%` | Syntactically valid LaTeX equation statement |
| **3. Is $S_R$ clearly wrong/invalid?** | `60` | `60` | `100.0%` | Single-operator perturbed mathematical claim |
| **4. Is the difference strictly local?** | `60` | `60` | `100.0%` | Identical problem text and prefix context |
| **5. Is the state recoverable?** | `60` | `60` | `100.0%` | Target task remains solvable from perturbed state |
| **6. Measures reasoning recovery vs corruption?** | `60` | `60` | `100.0%` | Measures mathematical reasoning recovery |

---
