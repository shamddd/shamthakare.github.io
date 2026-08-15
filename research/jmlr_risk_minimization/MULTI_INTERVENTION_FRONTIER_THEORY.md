# MULTI-INTERVENTION LOWER ENVELOPE THEORY

**Date**: August 16, 2026  

---

## 1. LOWER ENVELOPE COMPUTATION

For action space $\mathcal{A} = \{A_0, A_1, A_2, A_3\}$:
$$J^*(Q) = \min_{a \in \mathcal{A}} \left[ C_{	ext{train}}(a) + Q \cdot C_{	ext{infer}}(a) ight]$$

Since each $J_a(Q)$ is affine in $Q$, $J^*(Q)$ is a **concave piecewise linear lower envelope**.
Intervention $a_k$ is optimal in interval $[Q_{k-1}^*, Q_k^*]$. An intervention with higher $C_{	ext{train}}$ and higher $C_{	ext{infer}}$ is strictly dominated and never appears on the lower envelope.
