# PREEXECUTION ANALYSIS PLAN LOCK

**Date**: August 16, 2026  

---

## 1. ENDPOINTS & METRICS

* **E1 (Matching Coverage)**: Fraction of recovery states receiving valid control matches ($S_C$).
* **E2 (Covariate Balance)**: Standardized mean differences before vs after matching across 7 structural covariates.
* **E3 (Provenance Completeness)**: Fraction of rollouts with 100% complete JSONL primitive records.
* **E4 (Deterministic Reconstruction)**: 100% re-derivation of paper metrics from raw JSONL rollouts.
* **E5 (Matched Policy Contrast)**: $D_{	ext{recovery}} = \mathbb{E}_{S_R}[V_{	ext{Instruct}} - V_{	ext{Base}}] - \mathbb{E}_{S_C}[V_{	ext{Instruct}} - V_{	ext{Base}}]$.
* **E6 (Sensitivity)**: Contrast stability under tight caliper ($\le 0.15$) vs standard caliper ($\le 0.25$).

No hypothesis testing or stopping rules depend on the sign or magnitude of $D_{	ext{recovery}}$.
