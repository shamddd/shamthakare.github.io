# BEST-OF-N LARGE-N EXTRAPOLATION AUDIT ($N \le 512$)

**Date**: August 16, 2026  

---

## 1. ANALYTICAL EXTRAPOLATION TO LARGE $N$

We evaluate whether allowing $N \in \{64, 128, 256, 512\}$ for Best-of-$N$ eliminates the RLVR frontier crossover $Q^*_{\text{frontier}}$.

* **FLOP Scaling**: Inference cost for Best-of-$N$ at $N=512$ is $512 \times (C_{\text{gen}} + C_{\text{ver}})$, consuming $16\times$ more FLOPs per query than full RLVR inference.
* **Accuracy Saturation**: On ModComp-5 ($p = 0.03$), Best-of-512 reaches $1 - (1-0.03)^{512} \approx 99.9\%$ utility, but costs $6.55 \times 10^{11} \text{ FLOPs/query}$.
* **Impact on Crossover**: Because $C_{\text{inf}}(A_1(N=512)) \gg C_{\text{inf}}(A_3)$, increasing $N$ **decreases** $Q^*_{\text{frontier}}$ (makes RLVR amortize even faster per query).
* **Conclusion**: Large-$N$ search extrapolation does **NOT** eliminate the trained-model frontier.
