# COMPREHENSIVE DEPLOYMENT COST MODEL: DECOMPOSITION & PARAMETERIZATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. TOTAL COST DECOMPOSITION

For intervention class $a \in \{A_0, A_1, A_2, A_3\}$ servicing $Q$ independent deployment queries drawn from target distribution $D$:

$$C_{\text{total}}(a, Q) = C_{\text{train}}(a) + Q \cdot C_{\text{inference}}(a)$$

Do **NOT** collapse training FLOPs and inference FLOPs into a single static sum; retain their explicit parametric dependence on deployment query volume $Q$.

---

## 2. DETAILED FLOP & OVERHEAD DECOMPOSITION

### A. Training Cost Component $C_{\text{train}}(a)$

$$C_{\text{train}}(a) = \text{Steps} \times B_{\text{batch}} \times L_{\text{rollout}} \times \Big( 6 \cdot |\Theta_{\text{active}}(a)| + 2 \cdot |\Theta_{\text{frozen}}(a)| \Big)$$

* **$A_0$ (Base Greedy)**: $C_{\text{train}}(A_0) = 0 \text{ FLOPs}$.
* **$A_1$ (Best-of-$N$)**: $C_{\text{train}}(A_1) = 0 \text{ FLOPs}$.
* **$A_2$ (LoRA-RLVR Baseline)**: Trains adapter parameters $|\Theta_{\text{active}}| = |\Theta_{\text{LoRA}}| \ll |\Theta|$.
  $$C_{\text{train}}(A_2) \approx \text{Steps} \times B \times L \times \Big( 6 \cdot |\Theta_{\text{LoRA}}| + 2 \cdot |\Theta_{\text{base}}| \Big)$$
* **$A_3$ (Full-Parameter RLVR)**: Trains 100% of parameters $|\Theta_{\text{active}}| = |\Theta|$.
  $$C_{\text{train}}(A_3) = \text{Steps} \times B \times L \times \Big( 6 \cdot |\Theta| \Big)$$

### B. Per-Query Inference Cost Component $C_{\text{inference}}(a)$

For each query instance $x \sim D$:

* **$A_0$ (Base Greedy)**:
  $$C_{\text{inference}}(A_0) = 2 \cdot |\Theta| \cdot L_{\text{gen}}$$
* **$A_1$ (Best-of-$N$ with Verifier)**:
  $$C_{\text{inference}}(A_1, N) = N \cdot \Big( 2 \cdot |\Theta| \cdot L_{\text{gen}} \Big) + N \cdot \Big( 2 \cdot |\Theta_{\text{verifier}}| \cdot L_{\text{verifier}} \Big) + C_{\text{aggregation}}$$
  *(Best-of-$N$ receives zero free verification; verifier forward passes are strictly charged).*
* **$A_2$ (LoRA-RLVR)**:
  $$C_{\text{inference}}(A_2) = 2 \cdot \Big( |\Theta| + |\Theta_{\text{LoRA}}| \Big) \cdot L_{\text{gen}} \approx 2 \cdot |\Theta| \cdot L_{\text{gen}}$$
* **$A_3$ (Full RLVR)**:
  $$C_{\text{inference}}(A_3) = 2 \cdot |\Theta| \cdot L_{\text{gen}}$$

---

## 3. EFFECTIVE MODEL LIFETIME $L$ AND DRIFT BOUNDARY

In real-world production deployments, policies are replaced after $L$ queries due to:
1. Model checkpoint updates & software releases.
2. Distribution drift on target query prompts.
3. Verifier schema modifications.

Therefore, the maximum usable deployment query horizon is bounded:
$$Q \le L$$
Amortization calculations for $Q > L$ are mathematically invalid in real-world deployment contexts.
