# POST-B0 SCIENTIFIC INTERPRETATION REPORT

## 1. WHY M0 BEATS M1 (BEHAVIORAL vs HEADROOM)
In small sample sizes (N=12), adding 5 headroom features increases parameter dimensionality in Ridge regression, slightly increasing variance without adding sufficient new signal beyond Pass@1 and Pass@64.

## 2. WHY INTERNAL DIAGNOSTICS ADD NO INCREMENTAL VALUE
1. **Collinearity with Scale/Performance**: Effective rank and linear probe AUROC heavily correlate with base accuracy (R^2 = 0.58-0.62).
2. **Absence of Residual Structure**: Internal features show near-zero correlation with the prediction errors of behavioral baselines (BH).
3. **Dominance of Headroom and Support**: Pretraining failure rate and task difficulty determine policy gradient headroom; internal representation geometry adds no non-redundant predictive information.
