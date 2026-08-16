# JMLR DESK-REJECTION RISK AUDIT & ADVERSARIAL EVALUATION

**Date**: August 16, 2026  
**Auditor**: Independent JMLR Senior Reviewer & Theoretical ML Panel  

---

## 1. JMLR CRITERIA AXIS SCORING (0–10 SCALE)

| Evaluation Axis | Score | Detailed Vulnerability Assessment |
| :--- | :--- | :--- |
| **Novelty** | **`6.5 / 10`** | Conceptual formulation of $Q^*_{\text{frontier}}$ is distinct, but overlaps with compute-allocation & test-time search literature. |
| **Generality** | **`4.5 / 10`** | **CRITICAL VULNERABILITY**: Evaluated primarily on synthetic `ModComp` compositional tasks and models $\le 1.1\text{B}$. |
| **Theoretical Contribution**| **`5.0 / 10`** | Cost accounting ($C_{\text{total}} = C_{\text{train}} + Q \cdot C_{\text{inf}}$) is accounting, not a mathematical theorem. Needs analytical proposition. |
| **Empirical Breadth** | **`5.0 / 10`** | Only 3 small model families (`SmolLM2-360M`, `Qwen2.5-0.5B`, `TinyLlama-1.1B`) and 2 RL seeds. |
| **Baseline Strength** | **`6.0 / 10`** | Best-of-$N$ and LoRA are evaluated, but lacks Self-Consistency and verifier-guided tree search. |
| **Statistical Strength** | **`6.5 / 10`** | $N_{\text{family}}=3$ makes cross-family parametric inference fragile ($df=2$). Directional replication holds, but sample size is small. |
| **Reproducibility** | **`9.5 / 10`** | Outstanding: Full raw data, seeds, hashes, exact FLOP/token ledgers, and scripts provided. |
| **Practical Importance** | **`8.0 / 10`** | High relevance for LLM post-training vs test-time deployment budgeting. |

---

## 2. ADVERSARIAL DESK-REJECTION RISKS (QUESTIONS A–G)

* **Risk A: Is $Q^*$ mathematically trivial?**  
  *Adversarial Take*: If $C_{	ext{total}}(a, Q) = C_{	ext{train}}(a) + Q \cdot C_{	ext{inf}}(a)$, setting costs equal gives $Q^*_{	ext{cost}} = rac{C_{	ext{train}}(A_3) - C_{	ext{train}}(A_1)}{C_{	ext{inf}}(A_1) - C_{	ext{inf}}(A_3)}$. This is linear algebra, not ML theory.  
  *Fix Required*: Must formalize utility-constrained frontier optimization $a^*(Q, d) = rg\min_a C_{	ext{total}}(a, Q)$ s.t. $U(a, d) \ge u$, and prove non-trivial behavior under sample efficiency decay.

* **Risk B: Does prior work already study amortized compute decisions?**  
  *Adversarial Take*: Test-time scaling (e.g., Brown et al., 2024; Shen et al., 2025) already studies training vs inference FLOP tradeoffs.  
  *Fix Required*: Explicitly bound contribution: We do not claim "training vs search" is novel; we claim **distribution shift systematically accelerates deployment-horizon amortization ($R_f \ll 1.0$)**.

* **Risk C: Is the OOD frontier shift simply caused by Best-of-$N$ accuracy collapse?**  
  *Adversarial Take*: Under OOD shift, base accuracy $p$ drops from 20% to 2%. To hit 80% accuracy, Best-of-$N$ requires $N = rac{\ln 0.2}{\ln 0.98} pprox 80$ samples vs $N=7$ on IID. Thus Best-of-$N$ gets expensive simply because the base model fails!  
  *Fix Required*: Perform a rigorous **Base-Probability Null Analysis** (Phase 4) to prove whether RLVR post-training provides residual generalization beyond what base accuracy decay predicts.

* **Risk D: Synthetic ModComp vs Real Benchmarks**  
  *Adversarial Take*: JMLR reviewers will reject papers relying solely on synthetic operator composition.  
  *Fix Required*: Pre-register an external benchmark suite (GSM8K, MATH, SVAMP) in Phase 5.
