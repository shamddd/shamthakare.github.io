# RESEARCH QUESTION SELECTION & CANDIDATE EVALUATION

**Project**: StateShift Scientific Rebuild  
**Author**: Sham Satish Thakare  

---

## 1. Candidate Research Questions Scorecard

| Evaluation Criterion (1-5 Scale) | Candidate A (Decomposition) | Candidate B (Predictability) | Candidate C (RL Regimes) | Candidate D (Generalization) | Candidate E (Mechanistic) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Novelty** | **5** | 3 | 4 | 4 | 4 |
| **2. Scientific Importance** | **5** | 3 | 4 | 4 | 4 |
| **3. Falsifiability** | **5** | 4 | 4 | 4 | 3 |
| **4. Causal Interpretability** | **4** | 2 | 4 | 4 | 3 |
| **5. Feasibility** | **5** | 4 | 2 | 4 | 2 |
| **6. Compute Requirement** | **5** (Zero/Low) | 4 | 2 | 3 | 3 |
| **7. Dataset Availability** | **5** | 5 | 4 | 4 | 4 |
| **8. Model Availability** | **5** | 5 | 3 | 4 | 3 |
| **9. Baseline Availability** | **5** | 4 | 3 | 4 | 2 |
| **10. Generalization Potential**| **5** | 3 | 4 | 5 | 3 |
| **11. Statistical Identifiability**| **5** | 4 | 4 | 4 | 3 |
| **12. Robustness to Null Outcome**| **5** | 3 | 4 | 4 | 3 |
| **TOTAL SCORE (out of 60)** | **58 / 60** | **44 / 60** | **45 / 60** | **50 / 60** | **37 / 60** |

---

## 2. Ranking & Primary Research Question Selection

### Ranking:
1. **RANK 1: Candidate A (Decomposition & Capability Specificity)** — Score 58/60
2. **RANK 2: Candidate D (Cross-Model & Cross-Domain Generalization)** — Score 50/60
3. **RANK 3: Candidate C (RL Training Regimes Comparison)** — Score 45/60
4. **RANK 4: Candidate B (Trajectory Predictability)** — Score 44/60
5. **RANK 5: Candidate E (Internal Representation Dynamics)** — Score 37/60

---

## 3. Primary Selected Research Question

We select a **Unified Hybrid of Candidate A & Candidate D**:

$$\mathbf{Primary\ RQ:\ Does\ RL\ post\text{-}training\ produce\ a\ recovery\text{-}specific\ capability\ beyond\ ordinary\ accuracy\ gains,}$$
$$\mathbf{and\ does\ this\ state\text{-}conditioned\ recovery\ generalize\ across\ model\ families\ and\ reasoning\ domains?}$$

### Mathematical Definition of Primary Estimand ($\Gamma_t^{\text{spec}}$):

Let $\text{Acc}_t$ be the aggregate benchmark accuracy at step $t$. We decompose $\Gamma_t$ into:

$$\Gamma_t = \beta \cdot (\text{Acc}_t - \text{Acc}_0) + \Gamma_t^{\text{spec}}$$

where $\Gamma_t^{\text{spec}}$ represents the **recovery-specific capability gain** net of general accuracy improvement.

*Signed by Principal Investigator & Lead Statistician*
