# EXPERIMENTAL DESIGN: TASK DIFFICULTY & COMPOSITIONAL OOD EVALUATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. PRE-DEFINED TASK DIFFICULTY METRICS ($d$)

Rather than arbitrary empirical bins, task difficulty $d$ is parameterised by controlled synthetic execution steps in a modular composition environment (**ModComp**):

* **$d = 2$ (Easy / High Base Accuracy)**: 2-step modular operations $f(x) = ((x \cdot a_1 + b_1) \pmod p \cdot a_2 + b_2) \pmod p$. Base Pass@1 $\approx 45\%$.
* **$d = 3$ (Edge-of-Competence)**: 3-step modular operations. Base Pass@1 $\approx 15\%$, Base Pass@64 $\approx 60\%$.
* **$d = 4$ (Hard)**: 4-step modular operations. Base Pass@1 $\approx 2\%$, Base Pass@64 $\approx 20\%$.

---

## 2. IID VS COMPOSITIONAL OOD EVALUATION SPLITS

1. **In-Distribution Evaluation ($D_{\text{IID}}$)**:
   - Evaluated on held-out 3-step ModComp operations using the same operator set $\{+, \cdot, \pmod p\}$ and modulus $p=101$ present during training.
2. **Compositional Out-of-Distribution Evaluation ($D_{\text{OOD}}$)**:
   - **Length Extrapolation ($D_{\text{OOD, length}}$)**: Evaluated on 5-step operations ($d=5$) when training occurred only on $d \le 3$.
   - **Operator Recombination ($D_{\text{OOD, operator}}$)**: Evaluated on novel operator compositions (e.g. incorporating bitwise XOR $\oplus$) absent in training rollouts.

---

## 3. SCIENTIFIC INTERACTION HYPOTHESIS

$$\text{Hypothesis}: \quad Q^*_{\text{OOD}}(A_1, A_3) \ll Q^*_{\text{IID}}(A_1, A_3)$$

On IID tasks, Best-of-$N$ ($A_1$) can sample pre-existing base pathways effectively, delaying RLVR amortization to high query volumes ($Q^*_{\text{IID}} \sim 10^5$). On Compositional OOD tasks, base policy sampling efficiency collapses ($\beta \to 0$), causing the Best-of-$N$ search cost to explode and shifting the RLVR amortization horizon to very low query volumes ($Q^*_{\text{OOD}} \sim 10^2$).

*Note: Improvements on $D_{\text{OOD}}$ are designated strictly as **OOD Generalization Improvements**, never as "new capabilities".*
