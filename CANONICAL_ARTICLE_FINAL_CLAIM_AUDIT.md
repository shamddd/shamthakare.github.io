# Canonical Research Article Final Claim & Language Audit

**Article Title**: *When Confidence Proxies Confound Reasoning Complexity*  
**Canonical URL**: `https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/`  
**Article Version**: `v1.0.1` (Patched August 22, 2026)  
**Audit Date**: August 22, 2026  
**Source of Truth Reference**: `distribution/DISTRIBUTION_SOURCE_OF_TRUTH.md`  

---

## 1. Audit Certification Summary

| Audit Dimension | Requirement | Audit Result | Status |
|---|---|---|---|
| **Numerical Claims** | 100% match raw source of truth ($r=0.486, r_{\text{partial}}=-0.092, p=0.365$, $\text{Var}(\log P)=0.0, 42.1\%, \text{AUROC}=0.812$, Pass@1 $80.00\% \pm 0.00\%, d=0.00$) | 100% Match | **PASS (100%)** |
| **Causal Language** | Replaced over-strong claims with epistemically safer formulations | Zero un-justified causal claims | **PASS** |
| **Model Scope** | Explicitly bounded to `Qwen2.5-0.5B-Instruct` | Fully Bounded | **PASS** |
| **Seed Scope** | Bounded to $N = 3$ independent training seeds | Fully Bounded | **PASS** |
| **Publication Status** | Maintained as `Working Paper / Research Note` | Certified | **PASS** |
| **Figure Captions** | Free of causal assertions ("causes", "proves") | 100% Clean | **PASS** |

---

## 2. Quantitative Claims Verification Matrix

| Section / Element | Canonical HTML Wording | Source of Truth Log | Verification Status |
|---|---|---|---|
| **Section 5 (Length Confound)** | $r = 0.486, 95\%\text{ CI } [+0.318, +0.627], N=100$ | $r = 0.486, N=100$ | **VERIFIED (100%)** |
| **Section 5 (Partial Correlation)** | $r = -0.214 \rightarrow r_{\text{partial}} = -0.092, p = 0.365$ | $r_{\text{partial}} = -0.092, p = 0.365$ | **VERIFIED (100%)** |
| **Section 6 (AUROC Benchmark)** | Self-Consistency $K=4 \rightarrow \text{AUROC} = 0.812$ | $\text{AUROC} = 0.812$ | **VERIFIED (100%)** |
| **Section 7 (Architecture Audit)** | `Qwen2.5-0.5B-Instruct` 0 active dropout modules, $\text{Var}(\log P) = 0.0, \cos(\Delta\theta) = 1.000000$ | $\text{Var}(\log P) = 0.0, \cos(\Delta\theta) = 1.000000$ | **VERIFIED (100%)** |
| **Section 8 (Stress Test)** | 42.1% paired comparison misranking | 42.1% ($N=100$) | **VERIFIED (100%)** |
| **Section 9 (Controlled RL)** | Pass@1 $80.00\% \pm 0.00\%, d = 0.00, N=3$ seeds | Pass@1 $80.00\% \pm 0.00\%, d=0.00$ | **VERIFIED (100%)** |

---

## 3. Epistemic Wording Verification Matrix

- **Opening Causal Claim**: Updated to *"This raises the possibility that naive uncertainty weighting may downweight valid multi-step trajectories for reasons partly related to sequence length rather than correctness."*
- **Section 2 ("Why This Matters")**: Updated to *"If a length-confounded confidence proxy is used to scale policy-gradient advantages, longer trajectories may systematically receive different weights for reasons unrelated to correctness. Whether this produces a persistent preference for shorter reasoning requires separate evaluation."*
- **Figure 1 Caption**: Updated to *"Longer multi-step reasoning was associated with higher token entropy ($r = 0.486$) in the evaluated sample, illustrating how sequence length can confound interpretation of entropy as an uncertainty signal."*
- **Stress Test Interpretation**: Updated to *"In this stress test ($N = 100$ prompt clusters), the estimator misidentified correct multi-step reasoning traces as more uncertain than short incorrect errors in 42.1% of paired comparisons. If used directly as a multiplicative policy-gradient weight, such a signal can assign lower weights to some correct longer trajectories for reasons not aligned with correctness."*

---

## Final Certification

The canonical research article `v1.0.1` is 100% compliant with scientific language standards, model scope boundaries, and source-of-truth verification.
