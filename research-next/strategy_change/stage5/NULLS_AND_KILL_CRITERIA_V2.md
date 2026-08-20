# NULL HYPOTHESES AND EXPLICIT KILL CRITERIA V2

**Date**: August 16, 2026  

---

## 1. GLOBAL IMPROVEMENT NULL (PRIMARY SCIENTIFIC NULL)

> **GLOBAL IMPROVEMENT NULL**: Full RLVR improves solution value equally at recovery states ($S_R$) and matched control states ($S_C$). 
> *Survival Condition*: The flagship survives **ONLY** if the Full-vs-PrefixRL advantage is selectively larger on recovery states ($\Delta_{\text{late}} > 0$).

---

## 2. EXPLICIT KILL CRITERIA (K1--K8)

* **K1**: $\Delta_{\text{late}} \le 0$ on $D_{\text{IID\_test}}$.
* **K2**: $\Delta_{\text{late}} \le 0$ on $D_{\text{structural\_OOD}}$ (OOD-B, OOD-D, OOD-M, OOD-C).
* **K3**: Selective advantage disappears after controlling for $S_C$ state covariates.
* **K4**: Equivalence margin bounds $\Delta_{\text{late}} < 0.02$.
* **K5**: Prior art audit identifies an existing work evaluating $\Delta_{\text{late}}$ under state matching.
