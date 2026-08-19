# PHASE 2B — STATISTICAL MULTIPLICITY CORRECTION PLAN

**Milestone**: Multiplicity Control across Intermediate Checkpoints  

---

## 1. Multiple Comparison Control Plan

When evaluating intermediate checkpoints $t \in \{64, 128, 192\}$, simultaneous family-wise error rate (FWER) or false discovery rate (FDR) control is enforced:

1. **Bonferroni-Adjusted Alpha**: $\alpha_{adj} = \frac{0.05}{3} = \mathbf{0.0167}$.
2. **Benjamini-Hochberg (FDR)**: Control FDR at $q = 0.05$ across intermediate contrasts.
3. **Simultaneous Confidence Bands**: Construct 95% simultaneous problem-blocked bootstrap confidence bands using joint percentile calibration across $B=10,000$ bootstrap draws.

*Signed by Statistical Methodologist & Lead Reviewer*
