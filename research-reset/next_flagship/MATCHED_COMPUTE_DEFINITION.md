# MATHEMATICAL FORMULATION: MATCHED COMPUTE & INTERVENTION CAPACITY FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. FORMAL DEFINITION OF INTERVENTION CAPACITY $A_k$

We consider an ordered set of intervention capacity levels $A_0, A_1, A_2, A_3, A_4, A_5$:

| Level | Intervention Class | Accessible Parameter Space $|\theta_{\text{train}}|$ | Policy Class Constraint |
| :--- | :--- | :--- | :--- |
| **$A_0$** | Base Generation | $0$ | $\pi_0(y \mid x)$ |
| **$A_1$** | Best-of-$N$ Verifier Selection | $0$ | $y^* = \arg\max_{y_i \in \text{Samples}(N)} R(x, y_i)$ |
| **$A_2$** | Prompt / Prefix Steering | $0$ (context tokens only) | $\pi_0(y \mid x, \text{prompt})$ |
| **$A_3$** | Learned Soft Prefix / Adapter | $k \sim 10^4\text{--}10^6$ ($< 0.1\%$ params) | $\pi_{\phi}(y \mid x)$ where $\phi$ is prefix/LoRA |
| **$A_4$** | Parameter-Efficient RLVR | $k \sim 10^6\text{--}10^7$ ($< 1\%$ params) | $\text{GRPO}(\pi_{\phi})$ |
| **$A_5$** | Full-Parameter RLVR | $|\Theta|$ (100% params) | $\text{GRPO}(\pi_{\Theta})$ |

---

## 2. TOTAL MATCHED COMPUTE COST $C_{\text{total}}(Q)$

Previous literature frequently compares cheap Best-of-$N$ to expensive full RL without cost normalization, or ignores inference query scaling $Q$.

For a deployment setting servicing $Q$ query instances, the total compute cost (in FLOPs or GPU-seconds) for intervention $A_k$ is:

$$C_{\text{total}}(A_k, Q) = C_{\text{train}}(A_k) + Q \cdot C_{\text{inference}}(A_k)$$

where:
1. **Training Compute $C_{\text{train}}(A_k)$**:
   $$C_{\text{train}}(A_k) = \text{Steps} \times \text{BatchSize} \times \text{RolloutLen} \times \left(6 \cdot |\Theta_{\text{active}}| + 2 \cdot |\Theta_{\text{frozen}}|\right)$$
   For $A_0, A_1, A_2$, $C_{\text{train}} = 0$.
   For $A_3, A_4$ (Prefix/LoRA), $C_{\text{train}} \ll C_{\text{train}}(A_5)$.

2. **Inference Compute $C_{\text{inference}}(A_k)$**:
   $$C_{\text{inference}}(A_1, N) = N \times L \times 2 |\Theta| + N \cdot C_{\text{verifier}}$$
   $$C_{\text{inference}}(A_5) = 1 \times L \times 2 |\Theta|$$

---

## 3. AMORTIZED COMPUTE EQUIVALENCE & AMORTIZATION THRESHOLD $Q^*$

For any pair of interventions $A_i$ (e.g. $A_1$ Best-of-$N$) and $A_j$ (e.g. $A_5$ Full RLVR), there exists an **Amortization Horizon Query Count $Q^*$**:

$$C_{\text{total}}(A_i, Q^*) = C_{\text{total}}(A_j, Q^*)$$
$$Q^* = \frac{C_{\text{train}}(A_j) - C_{\text{train}}(A_i)}{C_{\text{inference}}(A_i) - C_{\text{inference}}(A_j)} = \frac{C_{\text{train}}(A_5)}{(N - 1) \cdot C_{\text{inference}}(A_0)}$$

* **For $Q < Q^*$** (Low query volume): Inference-time Best-of-$N$ ($A_1$) is strictly cheaper in total FLOPs than training full RL ($A_5$).
* **For $Q > Q^*$** (High query volume): One-time training cost $C_{\text{train}}(A_5)$ is amortized, making full RL cheaper per query.

---

## 4. MARGINAL INTERVENTION RETURN (MIR) & PARETO FRONTIER

We define **Marginal Intervention Return (MIR)** between intervention capacity levels $A_i \to A_j$ under matched total compute $C$:

$$\text{MIR}(A_i \to A_j \mid C, D_{\text{OOD}}) = \frac{U(A_j, C; D_{\text{OOD}}) - U(A_i, C; D_{\text{OOD}})}{C_{\text{train}}(A_j) - C_{\text{train}}(A_i)}$$

where $U(A_k, C; D_{\text{OOD}})$ is the Out-of-Distribution generalization accuracy achieved by intervention $A_k$ under total budget $C$.

An intervention capacity level $A_j$ is **Pareto-Dominant** if and only if:
$$U(A_j, C; D_{\text{OOD}}) > \max_{k < j} U(A_k, C; D_{\text{OOD}}) \quad \text{at matched total budget } C$$
