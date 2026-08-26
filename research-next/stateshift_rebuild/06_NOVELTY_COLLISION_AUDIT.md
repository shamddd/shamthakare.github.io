# NOVELTY COLLISION AUDIT & PRIOR ART FALSIFICATION

**Project**: StateShift Scientific Rebuild  
**Author**: Sham Satish Thakare  

---

## 1. Prior-Art Collision Matrix

| StateShift Claim | Closest Prior Work | Same Question? | Same Intervention? | Same Endpoint? | Same Finding? | Novelty Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. RL post-training changes error recovery** | Huang et al. (2024), DeepSeek-AI (2025) | PARTIAL | NO | NO | NO | **`MODERATE NOVELTY`** |
| **2. Recovery depends on intermediate reasoning context** | Kamoi et al. (2024) | NO | PARTIAL | NO | NO | **`MODERATE NOVELTY`** |
| **3. Recovery contrast ($\Gamma_t$) emerges progressively across RL checkpoints** | Shao et al. (2024), Schaeffer et al. (2023) | NO | NO | NO | NO | **`STRONG NOVELTY`** |
| **4. Recovery is distinct from general accuracy improvement** | Standard RLVR Literature (Cobbe, Shao) | YES | NO | NO | NO | **`MODERATE NOVELTY`** (Requires formal null model decomposition) |
| **5. Natural error recovery rate ($\text{NRR}=30.93\%$)** | DeepSeek-AI (2025) | PARTIAL | NO | PARTIAL | NO | **`INCREMENTAL`** (DeepSeek-R1 already observed spontaneous re-reading) |
| **6. Trajectory consistency under order-restricted PAVA** | Generic Statistical Literature | NO | NO | YES | NO | **`METHODOLOGICAL NOVELTY`** |

---

## 2. Falsification Analysis of Novelty Claims

### Claim 1: "Post-training changes error recovery"
* **Prior Art**: Huang et al. (2024) showed that prompting-based intrinsic self-correction fails without external feedback. DeepSeek-R1 (2025) showed that RLVR induces spontaneous re-reading.
* **Falsification Verdict**: The basic idea that RL models alter error responses is **partially known**. However, measuring state-conditioned counterfactual recovery ($R$ vs $C$) across RL training steps remains **unexplored**.

### Claim 2: "Recovery contrast ($\Gamma_t$) is distinct from general accuracy gains"
* **Prior Art**: Standard RLVR literature (Shao et al., 2024) measures only aggregate accuracy ($\text{Acc}_t$).
* **Falsification Verdict**: **Crucial Vulnerability**. If $\Gamma_t$ simply tracks $\text{Acc}_t$ linearly, then StateShift is merely a noisy proxy for accuracy improvement. To establish **`STRONG NOVELTY`**, StateShift MUST decompose $\Gamma_t$ into:

$$\Gamma_t = \text{General Accuracy Gain} + \text{Context-Specific Recovery Gain}$$

If post-training produces a *recovery-specific capability beyond ordinary accuracy gains*, the paper establishes a fundamental, novel result.

---

## 3. Summary of Truly Novel Contributions

1. **Difference-in-Differences State Contrast ($\Gamma_t$)**: Counterfactual prefix matching ($R$ vs $C$) isolates state-dependent recovery from general prompt robustness. (**`STRONG NOVELTY`**)
2. **Order-Restricted Trajectory Analysis**: Evaluating non-decreasing trajectory consistency across RL post-training checkpoints using PAVA. (**`STRONG NOVELTY`**)
3. **Decomposition of General Capability vs. Recovery Capability**: (Proposed for Rebuild) Demonstrating whether recovery is a distinct learning dynamic. (**`HIGH SCIENTIFIC VALUE`**)

*Signed by Scientific Integrity Auditor & Lead Reviewer*
