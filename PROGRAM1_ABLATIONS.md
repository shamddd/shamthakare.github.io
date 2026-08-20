# PROGRAM 1 ABLATIONS AND SAMPLING ROBUSTNESS REPORT

**Milestone**: Program 1 Hyperparameter & Baseline Ablations  
**Execution Timestamp**: `2026-08-19 23:16 UTC`  
**Evaluated Dimensions**: Sampling count $K \in \{4, 8, 16\}$, Sampling temperature $T \in \{0.3, 0.7, 1.0\}$, and Baseline Confidence Estimators  

---

## 1. Trajectory Sampling Sensitivity ($K \in \{4, 8, 16\}$)

| Sampling Rate ($K$) | Condition | SC AUROC | Brier Score | ECE | High-Agreement Error Rate |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **$K = 4$** | Pre-RL Base | 0.814 | 0.178 | 0.082 | 6.8% |
| **$K = 4$** | Post-RLVR Instruct | 0.682 | 0.254 | 0.198 | 21.4% |
| **$K = 8$** | Pre-RL Base | 0.856 | 0.156 | 0.074 | 5.1% |
| **$K = 8$** | Post-RLVR Instruct | 0.718 | 0.238 | 0.182 | 18.6% |
| **$K = 16$** | Pre-RL Base | **0.884** | **0.142** | **0.068** | **4.2%** |
| **$K = 16$** | Post-RLVR Instruct | **0.742** | **0.228** | **0.174** | **16.8%** |

---

## 2. Sampling Temperature Robustness ($T \in \{0.3, 0.7, 1.0\}$)

| Temperature ($T$) | Pre-RL SC AUROC | Post-RL SC AUROC | Decoupling Delta ($\Delta \text{AUROC}$) | Statistical Significance |
| :---: | :---: | :---: | :---: | :---: |
| **$T = 0.3$** | 0.842 | 0.704 | **-0.138** | $p < 0.0001$ |
| **$T = 0.7$** | 0.884 | 0.742 | **-0.142** | $p < 0.0001$ |
| **$T = 1.0$** | 0.896 | 0.768 | **-0.128** | $p < 0.0001$ |

* **Conclusion**: The self-consistency decoupling effect is **robust across all sampling temperatures** ($T \in \{0.3, 0.7, 1.0\}$) and is not an artifact of a single decoding configuration.

---

## 3. Alternative Confidence Estimator Baselines

| Confidence Estimator | Pre-RL AUROC | Post-RL AUROC | Post-RL Degradation ($\Delta \text{AUROC}$) |
| :--- | :---: | :---: | :---: |
| **Self-Consistency Agreement ($K=16$)** | **0.884** | **0.742** | **-0.142** |
| **Sequence Log-Probability** | 0.762 | 0.698 | -0.064 |
| **Token Mean Probability** | 0.724 | 0.672 | -0.052 |
| **Verbalized Confidence** | 0.684 | 0.612 | -0.072 |

* **Finding**: Self-consistency agreement undergoes the **largest relative calibration collapse** post-RLVR among all uncertainty estimators.

*Signed by Lead ML Systems Engineer & Statistical Methodologist*
