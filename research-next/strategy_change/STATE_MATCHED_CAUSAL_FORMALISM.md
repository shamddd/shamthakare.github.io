# STATE-MATCHED CAUSAL IDENTIFICATION FORMALISM

**Date**: August 16, 2026  

---

## 1. LIMITATIONS OF VISIBLE TEXT PREFIX STEERING

> **Causal Flaw in $do(\tau_{1:k} = z)$**: Forcing identical text tokens under $\pi_{\text{base}}$ and $\pi_{\text{RL}}$ does **NOT** equalize the underlying model state, hidden representations, token probabilities, or calibration. Thus, text-prefix steering alone fails to establish causal within-strategy policy change.

---

## 2. EXTERNALLY CONTROLLED STATE MATCHING ($s_k$)

To achieve rigorous causal identification, we construct synthetic graph/algorithmic environments where the **environment state $s_k$** is externally controlled and observed.

For any intermediate state $s_k$ requiring error recovery:
* Equalize: Environment state $s_k$, valid action set $\mathcal{A}(s_k)$, observation $o_k$, execution history, and verifier.
* **State-Contingent Policy Divergence**:
  $$\Delta_{\text{state}}(s_k) = D_{\text{TV}}\left(\pi_{\text{RL}}(\cdot|s_k), \pi_{\text{base}}(\cdot|s_k)\right)$$
* **Recovery Advantage**:
  $$A_{\text{recovery}}(s_k) = P_{\text{RL}}(\text{Success} | s_k) - P_{\text{base}}(\text{Success} | s_k)$$

### Key Hypothesis:
We test whether $\Delta_{\text{state}}(s_k)$ is **selectively elevated at recovery-critical states $s_k$**, and whether this policy divergence causally drives $A_{\text{recovery}}(s_k) > 0$ on unseen graph topologies.
