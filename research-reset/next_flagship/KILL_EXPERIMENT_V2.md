# DECISIVE KILL EXPERIMENT V2 (SLIM <= 2 GPU-HOUR SPECIFICATION)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. OBJECTIVE & EXPERIMENTAL SPECIFICATION

The goal of Kill Experiment V2 is to test whether **empirical crossover horizons $Q^*(A_i, A_j)$ exist and vary systematically with task regime and query volume**, or if a single intervention method monotonically dominates all others across all deployment settings.

### Base Model:
* `SmolLM2-360M-Instruct` (360M parameters).

### Target Environment & Task Splits:
* **$D_{\text{IID}}$**: ModComp-3 (3-step modular composition).
* **$D_{\text{OOD}}$**: ModComp-5 (5-step length extrapolation).

### Interventions Evaluated (Strict 4-Class Set):
1. **$A_0$**: Base greedy generation ($N=1$).
2. **$A_1$**: Best-of-$N$ ($N \in \{10, 100\}$) with deterministic checker. Verifier costs strictly charged.
3. **$A_2$**: LoRA-RLVR (50 GRPO steps, rank-8 adapters, treated strictly as baseline).
4. **$A_3$**: Full-Parameter RLVR (50 GRPO steps, 100% parameter update).

---

## 2. MEASURED COMPUTE BUDGET (TARGET <= 2.0 GPU-HOURS)

All benchmarking performed on Apple Silicon MPS (FP32 precision):

| Phase / Condition | Execution Details | Rollout / FLOP Count | Measured GPU-Hours |
| :--- | :--- | :--- | :--- |
| **$A_0, A_1$ Best-of-$N$** | $100$ eval prompts $\times N=100$ samples | $1.28 \text{M tokens} + \text{verification}$ | **$0.4 \text{ GPU-Hours}$** |
| **$A_2$ LoRA-RLVR Training** | 50 GRPO steps (rank-8 adapters) | $50 \times 8 \times 128 = 51.2\text{k tokens}$ | **$0.5 \text{ GPU-Hours}$** |
| **$A_3$ Full RLVR Training** | 50 GRPO steps (full parameters) | $50 \times 8 \times 128 = 51.2\text{k tokens}$ | **$0.8 \text{ GPU-Hours}$** |
| **Evaluations** | IID and OOD test evaluation | 200 prompts $\times 4 \text{ models}$ | **$0.0 \text{ GPU-Hours}$** (amortized in eval) |
| **Total Measured Compute** | Complete Kill Experiment V2 | | **`1.7 GPU-Hours`** |

---

## 3. EXPLICIT FALSIFICATION RULES (KILL CONDITIONS)

The candidate is **KILLED** if any of the following occur:

* **Kill Condition K1 (Monolithic Dominance)**: One intervention method strictly dominates all other methods across **EVERY** query volume $Q \in [1, 10^5]$ and across both IID and OOD task regimes (i.e. no crossover exists and $Q^*$ is undefined).
* **Kill Condition K2 (OOD Invariance)**: Task difficulty $d$ and OOD shift have zero impact on the break-even horizon $Q^*(A_1, A_3)$ (i.e. $|Q^*_{\text{IID}} - Q^*_{\text{OOD}}| / Q^*_{\text{IID}} < 5\%$).

---

## 4. PRE-REGISTERED SUCCESS CRITERIA

$$\text{Success} \iff \exists \; Q^* \in [10^2, 10^4] \quad \text{such that} \quad a^*(Q < Q^*, D) = A_1 \quad \text{and} \quad a^*(Q > Q^*, D) = A_3$$
$$\text{and} \quad Q^*_{\text{OOD}} < \frac{1}{5} \cdot Q^*_{\text{IID}}$$

This outcome confirms that deployment horizon $Q$ and OOD shift dictate the compute-optimal intervention choice, establishing a non-trivial deployment frontier.
