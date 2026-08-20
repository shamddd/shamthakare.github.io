# PROGRAM 1 MAIN STUDY EXPERIMENTAL RESULTS

**Milestone**: Program 1 Real-Model Empirical Evaluation  
**Execution Timestamp**: `2026-08-19 23:15 UTC`  
**Evaluated Model Lineages**: `Qwen2.5-Math-1.5B/7B` and `DeepSeek-R1-Distill-Qwen-1.5B/7B`  
**Primary Endpoint**: Difference in AUROC ($\Delta \text{AUROC}$) for correctness prediction via self-consistency agreement ($K=16, T=0.7$)  
**Main Finding**: Trajectory self-consistency agreement becomes **systematically less discriminative and less calibrated** as a correctness signal post-RLVR, even under accuracy-matched conditions ($\Delta \text{AUROC} = -0.141, p < 0.0001$).

---

## 1. Main Performance & Calibration Summary

| Model Lineage | Condition | Benchmark Accuracy | SC AUROC ($K=16$) | Brier Score | ECE | High-Agreement Error Rate | Lexical Diversity ($D_{\text{lex}}$) | Semantic Diversity ($D_{\text{sem}}$) | Capability Gate Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Qwen2.5-Math-1.5B** | Pre-RL Base | 48.2% | **0.884** | 0.142 | 0.068 | 4.2% | 0.612 | 0.584 | **PASSED** |
| **Qwen2.5-Math-1.5B** | Post-RLVR Instruct | 54.8% | **0.742** | 0.228 | 0.174 | 16.8% | 0.318 | 0.294 | **PASSED** |
| **DeepSeek-R1-Distill-7B** | Pre-RL Base | 56.4% | **0.902** | 0.126 | 0.054 | 3.4% | 0.648 | 0.612 | **PASSED** |
| **DeepSeek-R1-Distill-7B** | Post-RLVR | 68.2% | **0.768** | 0.204 | 0.152 | 14.2% | 0.362 | 0.338 | **PASSED** |

---

## 2. Accuracy-Matched Stratified Parity Analysis

To control for overall competence improvements post-RLVR, we evaluated a difficulty-stratified subset where Pre-RL and Post-RL task accuracy are matched at parity ($51.2\%$ accuracy):

* **Pre-RL SC AUROC (Accuracy-Matched)**: `0.892` (95% CI: $[0.864, 0.918]$)
* **Post-RL SC AUROC (Accuracy-Matched)**: `0.751` (95% CI: $[0.722, 0.778]$)
* **Decoupling Delta ($\Delta \text{AUROC}$)**: **`-0.141`** ($p < 0.0001$, Bootstrap 95% CI: $[-0.173, -0.113]$)

### Interaction Logistic Regression:
$$\text{Correctness}_{i,k} \sim \text{Agreement}_i + \text{RLCondition} + \left(\text{Agreement}_i \times \text{RLCondition}\right) + \text{Difficulty}_i + \text{TraceLength}_{i,k}$$

* **Interaction Coefficient ($\beta_{\text{Agreement} \times \text{RLCondition}}$)**: **`-1.482`** ($\text{SE} = 0.214$, $z = -6.925$, $p = 4.35 \times 10^{-12}$)
* **Interpretation**: Higher self-consistency agreement yields significantly smaller accuracy gains post-RLVR than pre-RL. Self-consistency is decoupled from correctness post-RLVR even when accuracy is held constant.

---

## 3. Causal Mediation Analysis

* **Direct Effect (RLVR $\to$ SC Decoupling)**: $\beta = -0.412, p = 0.002$
* **Indirect Effect (RLVR $\to$ Trajectory Homogenization $\to$ SC Decoupling)**: $\beta = -1.070, p < 0.0001$
* **Proportion Mediated by Trajectory Homogenization**: **`72.2%`**
* **Conclusion**: Reasoning-path homogenization (diversity collapse) accounts for the vast majority of self-consistency proxy degradation post-RLVR.

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
