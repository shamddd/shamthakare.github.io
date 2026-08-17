# STATISTICAL INFERENCE LOCK & DESIGN SENSITIVITY RECONCILIATION

**Experimental Structure**: Paired Control ($S_C$) / Recovery ($S_R$) Trajectory Evaluation  
**Authoritative Sample Size ($N_{usable}$)**: `365` independent mathematical reasoning problems  

---

## 1. Power / MDES Claim Forensic Reconciliation

> [!IMPORTANT]
> **Statistical Model Correction & MDES Downgrade**:
> The earlier statement of *"MDES = 10% at 80% power"* treated the $N=365$ problem pairs as simple independent Bernoulli observations. Because the actual experimental design involves paired state evaluations, repeated model checkpoints, and stochastic rollouts nested within problems, treating observations as simple independent Bernoulli trials underestimates standard errors.
> 
> Therefore, formal power language is **explicitly removed from the prospective protocol**. The $N=365$ sample size calculation is formally classified as a **"generic design-sensitivity illustration"**, describing the descriptive sensitivity of the problem pool rather than a guaranteed power threshold.

---

## 2. Immutable Primary Inference Lock

1. **Primary Inferential Metric**: **$\Gamma_T$**  
   Defined as the overall average target transition recovery difference between Control ($S_C$) and Recovery ($S_R$) trajectories across all decontaminated state pairs:
   $$\Gamma_T = \frac{1}{N} \sum_{i=1}^{N} \left( \text{TargetSuccess}(S_{C,i}) - \text{TargetSuccess}(S_{R,i}) \right)$$

2. **Statistical Unit of Analysis**: **Independent problem / paired registry entry** ($N=365$).

3. **Uncertainty Estimation & Resampling**:
   - Primary confidence intervals and hypothesis tests MUST use **Problem-Blocked Bootstrap Resampling** ($B=10,000$ iterations).
   - Whole problem pairs $(S_{C,i}, S_{R,i})$ are sampled with replacement, preserving within-problem correlation and rollout nesting.

4. **Secondary Descriptive Trajectories**:
   - Checkpoint-wise trajectory curves $\Gamma_t$ for individual training steps $t$ are evaluated **descriptively**.
   - No multiple-testing adjustments across 8 individual checkpoint-wise hypothesis tests are conducted. Primary inference rests solely on $\Gamma_T$.

---
