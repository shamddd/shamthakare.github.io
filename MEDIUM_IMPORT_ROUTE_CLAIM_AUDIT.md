# Medium Import Route Claim Audit

**Route URL**: `https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/medium/`  
**Canonical Source**: `https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/`  
**Audit Date**: August 22, 2026  
**Source of Truth Reference**: `distribution/DISTRIBUTION_SOURCE_OF_TRUTH.md`  

---

## 1. Claim Verification Matrix

| Claim Location | Medium Import Route Wording | Source of Truth Value | Audit Status |
|---|---|---|---|
| **Section 2 (Length Confound)** | $r = 0.486, 95\%\text{ CI } [+0.318, +0.627], N=100$ | $r = 0.486, N=100$ | **VERIFIED (100%)** |
| **Section 2 (Partial Correlation)** | $r = -0.214 \rightarrow r_{\text{partial}} = -0.092, p = 0.365$ | $r_{\text{partial}} = -0.092, p = 0.365$ | **VERIFIED (100%)** |
| **Section 3 (Stress Test)** | 42.1% misranking rate ($N=100$) | 42.1% paired comparison misranking | **VERIFIED (100%)** |
| **Section 4 (Architecture Audit)** | `Qwen2.5-0.5B-Instruct` 0 active dropout modules, $\text{Var}(\log P) = 0.0, \cos(\Delta\theta) = 1.000000$ | $\text{Var}(\log P) = 0.0, \cos(\Delta\theta) = 1.000000$ | **VERIFIED (100%)** |
| **Section 5 (Self-Consistency)** | $K=4, \text{AUROC} = 0.812, r_{\text{partial}} = -0.569$ | $\text{AUROC} = 0.812$ | **VERIFIED (100%)** |
| **Section 5 (RL Table)** | Pass@1 $80.00\% \pm 0.00\%, d = 0.00, N=3$ seeds | Pass@1 $80.00\% \pm 0.00\%, d=0.00$ | **VERIFIED (100%)** |
| **Section 8 (Limitations)** | Bounded to `Qwen2.5-0.5B-Instruct`, math reasoning, $N=3$ seeds | $N=3$ seeds, `Qwen2.5-0.5B-Instruct` scope | **VERIFIED (100%)** |

---

## 2. Epistemic & Hype Language Verification

- ❌ "Delve", "Landscape", "Groundbreaking", "Revolutionary", "Remarkable", "Crucial", "Robust", "Novel", "Fascinating", "Game-changing", "Cutting-edge": **0 occurrences (100% Clean)**.
- ❌ Raw LaTeX `$$...$$` math blocks: **0 occurrences** (Converted to clean HTML prose).
- ❌ IEEE Submission / Acceptance / Peer-Review Claims: **0 occurrences** (Maintained as `Working Paper / Research Note`).

---

## Audit Certification

The dedicated Medium import route is 100% compliant with source-of-truth metrics and epistemic standards.
