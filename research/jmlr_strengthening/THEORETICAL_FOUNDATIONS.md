# THEORETICAL FOUNDATIONS & PROPOSITION DERIVATIONS

**Date**: August 16, 2026  
**Auditor**: Theoretical Machine Learning Auditor  

---

## 1. FORMAL PROBLEM STATEMENT

Let $a \in \{A_0, A_1(N), A_2, A_3\}$ be an intervention strategy, $d \in \mathbb{N}$ denote compositional reasoning complexity, and $Q \in \mathbb{N}^+$ be downstream query volume.

Total deployment compute:
$$C_{\text{total}}(a, Q) = C_{\text{train}}(a) + Q \cdot C_{\text{inf}}(a)$$

Target utility constraint: $U(a, d) \ge u$.

---

## 2. PROPOSITION 1: BEST-OF-$N$ COMPUTE SCALING UNDER BASE ACCURACY DECAY

Let $p(d) = P(\text{success} \mid A_0, d)$ be the single-sample success probability of the base model at complexity $d$. Assuming independent Bernoulli trials for Best-of-$N$ candidates:
$$U(A_1(N), d) = 1 - (1 - p(d))^N$$

To achieve target accuracy $u \in (0, 1)$, the required sample count $N^*(p, u)$ is:
$$N^*(p, u) = \frac{\ln(1 - u)}{\ln(1 - p(d))}$$

The inference FLOP cost per query for $A_1(N^*)$ with verifier cost $C_{\text{ver}}$ is:
$$C_{\text{inf}}(A_1(N^*)) = \frac{\ln(1 - u)}{\ln(1 - p(d))} \cdot (C_{\text{gen}} + C_{\text{ver}})$$

---

## 3. PROPOSITION 2: AMORTIZATION CROSSOVER SHIFT UNDER OOD DECAY

Let $A_3$ be full RLVR post-training with post-adaptation accuracy $p_{\text{RL}}(d) \ge u$ and training cost $C_{\text{train}}(A_3)$. The break-even query horizon $Q^*_{\text{frontier}}$ where $A_3$ becomes strictly more compute-efficient than $A_1(N^*)$ is:

$$Q^*_{\text{frontier}}(d) = \frac{C_{\text{train}}(A_3)}{\left[ \frac{\ln(1 - u)}{\ln(1 - p(d))} \cdot (C_{\text{gen}} + C_{\text{ver}}) \right] - C_{\text{gen}}}$$

### COROLLARY 1.1 (OOD Horizon Contraction Ratio $R_f$):
If compositional distribution shift increases complexity from $d_{\text{IID}}$ to $d_{\text{OOD}}$ such that $p(d_{\text{OOD}}) < p(d_{\text{IID}})$, while RLVR retains generalization efficiency $p_{\text{RL}}(d_{\text{OOD}}) \ge u$, the crossover ratio satisfies:

$$R_f = \frac{Q^*_{\text{frontier}}(d_{\text{OOD}})}{Q^*_{\text{frontier}}(d_{\text{IID}})} = \frac{\ln(1 - p(d_{\text{IID}}))}{\ln(1 - p(d_{\text{OOD}}))} \cdot \left[ \frac{\ln(1 - u) (C_{\text{gen}} + C_{\text{ver}}) - C_{\text{gen}} \ln(1 - p(d_{\text{IID}}))}{\ln(1 - u) (C_{\text{gen}} + C_{\text{ver}}) - C_{\text{gen}} \ln(1 - p(d_{\text{OOD}}))} \right] < 1.0$$

*Proof Summary*: Because $\ln(1 - p(d_{\text{OOD}})) < \ln(1 - p(d_{\text{IID}})) < 0$, the denominator grows faster than the numerator, proving analytically that $R_f < 1.0$ under base accuracy decay.
