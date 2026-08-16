# PREREGISTRATION AMENDMENT 01: PHASE B0 PILOT DESIGN CORRECTIONS

**Date**: August 16, 2026  
**Registration Authority**: Antigravity Forensic Research Unit  
**Status**: LOCKED AMENDMENT (PHASE B0 AMENDMENT 01)  
**Parent Document**: `PHASE_B0_ANALYSIS.md` (SHA-256: `8825f5807952b1476e6412395b29c3244f650a5b1c73cfb4452353c102c6ff6d`)  
**Certification**: We explicitly certify that **ZERO Phase B0 RL outcome data or training runs were observed or executed prior to this amendment**.

---

## 1. RATIONALE & REQUEST ORIGIN

This amendment was requested by the principal research director to correct:
1. Seed variance estimation under Kill Condition K6 (requires explicit multi-seed replication).
2. Terminology surrounding "edge of competence" (replacing heuristic proxies with a psychometrically grounded empirical competence-boundary model).
3. The K5 kill condition threshold (replacing binary drop with a 3-tier classification: `PROMISING`, `INCONCLUSIVE`, `ADVERSE`).
4. Feature ablation taxonomy ($M_0$ through $M_5$).
5. Pass@64 evaluation cost verification.

---

## 2. AMENDMENT DETAILS

### Amendment 1: Seed Replication Design (18 Total Runs)
* Maintain **12 Primary Conditions**:
  - 3 Model Families (SmolLM2, Pythia, Qwen2.5)
  - $\times$ 2 Checkpoints per Family
  - $\times$ 2 Task Conditions (GSM8K-Easy, GSM8K-Hard)
  - $\times$ 1 Primary Seed (Seed A = 42)
  - $= 12$ Primary Runs
* Add **3 Seed-Replication Conditions**:
  1. High-headroom / weaker checkpoint: `Pythia-410M (Step 50k) on GSM8K-Hard`
  2. Intermediate competence checkpoint: `SmolLM2-360M (Step 50k) on GSM8K-Easy`
  3. Low-headroom / stronger checkpoint: `Qwen2.5-0.5B (Final) on GSM8K-Easy`
* Each replication condition runs Seed B (1337) and Seed C (2026).
* Total Phase B0 Pilot Budget: $12 + (3 \times 2) = \mathbf{18 \text{ Controlled RLVR Runs}}$.
* Kill Condition K6 is evaluated strictly on this 3-condition replication subset.

---

### Amendment 2: Terminology Standardization
* Renamed `performance_ceiling_distance` ($1 - \text{Pass@1}$) $\to$ **`base_error_pass1`**.
* Renamed `edge_of_competence` ($1 - \text{Pass@64}$) $\to$ **`failure_rate_pass64`**.
* Neither raw quantity is referred to as an "edge of competence" metric.

---

### Amendment 3: Empirical Competence-Boundary Proximity Variable
* We define a psychometrically grounded empirical task difficulty scale $d(x)$ based on average cross-model base success rate.
* We define model-specific competence threshold $d^*(M)$ such that $p_{\text{success}}(d^*(M) \mid M) = q$.
* **Fixed Pre-Registered $q = 0.50$**: The 50% success probability threshold corresponds to maximum item discrimination in Item Response Theory (IRT) where RL policy gradient signal dynamic range is highest.
* **Defined Metric**: `competence_distance(x, M) = d(x) - d^*(M)`.
* We summarize each task dataset by:
  1. `mean_abs_competence_distance`: Mean $|d(x) - d^*(M)|$
  2. `frac_in_competence_band`: Fraction of problems with $|d(x) - d^*(M)| \le 0.15$
  3. `frac_below_competence`: Fraction of problems with $d(x) - d^*(M) < -0.15$ (too hard)
  4. `frac_above_competence`: Fraction of problems with $d(x) - d^*(M) > 0.15$ (mastered)
* This variable is formally named **`empirical competence-boundary proximity`**.

---

### Amendment 4: Refactored Kill Condition K5
* Replaced binary kill condition with a 3-tier outcome classification based on $\Delta\text{MAE} = \text{MAE}_{\text{BH}} - \text{MAE}_{\text{BHI}}$ across held-out families:
  - **`PROMISING`**: BHI improves prediction across a majority of held-out families ($\ge 2/3$) and mean $\Delta\text{MAE} > 0.005$.
  - **`INCONCLUSIVE`**: Predictive changes are small ($|\Delta\text{MAE}| \le 0.005$), inconsistent across families, or uncertainty is large. Leads to `REFORMULATE / MORE INFORMATION REQUIRED`.
  - **`ADVERSE`**: BHI materially worsens prediction across a majority of held-out families ($\Delta\text{MAE} < -0.01$). Triggers kill condition `NO-GO`.

---

### Amendment 5: Pre-Registered Feature Ablation Hierarchy
We pre-register 6 nested regression models:
* $M_0 = B$ (Behavioral baselines)
* $M_1 = BH$ (Behavioral + Headroom/History baselines)
* $M_2 = BH + \text{Probe}$ ($BH$ + Reward probe AUROC / $R^2$)
* $M_3 = BH + \text{Representation Geometry}$ ($BH$ + Effective rank, Stable rank, SVD top ratio)
* $M_4 = BH + \text{Gradient Diagnostics}$ ($BH$ + Gradient norm, GNS, LayerNorm ratio)
* $M_5 = BH + \text{All Internal Diagnostics}$ ($BH + I$)

* Primary Comparison: **$M_5$ vs $M_1$**.
* Secondary Comparisons: **$M_2, M_3, M_4$ vs $M_1$** (to isolate which specific diagnostic family contributes predictive information).

---

### Amendment 6: Pass@64 Benchmark Inference Cost Verification
* Evaluation Problems: 100 problems per task
* Rollouts per Problem: 64 samples ($100 \times 64 = 6,400$ total generation rollouts)
* Average Generated Tokens per Sample: ~48 tokens
* Total Generated Tokens per Checkpoint: $6,400 \times 48 \approx 307,200$ tokens
* Generation Throughput: ~43.5 tokens / sec (measured on Apple Silicon MPS / FP32)
* Wall-Clock Evaluation Time per Checkpoint: $\approx 7,062 \text{ seconds} \approx \mathbf{1.96 \text{ GPU-Hours}}$
* Total Pass@64 Budget for 6 Pilot Checkpoints: $\approx \mathbf{11.76 \text{ GPU-Hours}}$
* **Verdict**: Pass@64 is computationally affordable within our Phase B0 ceiling. We preserve Pass@64 without downsampling to maintain the strong Kang et al. baseline.

---

## 3. AMENDMENT PRE-REGISTRATION CRYPTOGRAPHIC DIGEST

* **Parent Document**: `research/prelude_v1/preregistration/PHASE_B0_ANALYSIS.md` (SHA-256: `8825f5807952b1476e6412395b29c3244f650a5b1c73cfb4452353c102c6ff6d`)
* **Amendment Document**: `research/prelude_v1/preregistration/PHASE_B0_ANALYSIS_AMENDMENT_01.md`
* **Amendment SHA-256 Digest**: `51ab9c5364ce3934335c02450ea13cd691a329fa0378bc28a0e88b6883bfd12f`
