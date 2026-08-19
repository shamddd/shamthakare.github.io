# PHASE 2 STAGE A — TRAJECTORY STATISTICAL ANALYSIS PROTOCOL

**Milestone**: Phase 2 Trajectory Statistical Analysis Specification  
**Primary Secondary Estimand**: $\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$ for $t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$  

---

## 1. Problem-Blocked Resampling & Simultaneous Confidence Bands

1. **Problem-Blocked Bootstrap**: To account for problem-level heterogeneity, resampling is performed at the problem cluster level ($N=454$) with $B=10,000$ bootstrap replicates.
2. **Simultaneous Confidence Bands**: Simultaneous 95% confidence bands are constructed using the sup-t / joint quantile procedure across the 7 intermediate checkpoints to control familywise error rate without p-hacking individual steps.
3. **Isotonic Contrast Analysis**: Monotonicity is evaluated using order-restricted contrast inference ($\Gamma_{t_{j+1}} - \Gamma_{t_j} \ge -\delta$) rather than unadjusted raw sample ordering.

*Signed by Lead Statistical Methodologist & Causal-Inference Reviewer*
