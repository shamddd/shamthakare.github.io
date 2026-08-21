# Canonical Research Article Version History

**Article Title**: *When Confidence Proxies Confound Reasoning Complexity*  
**Canonical URL**: `https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/`  

---

## Version Changelog

### v1.0.1 — August 22, 2026 (Scientific Language & Epistemic Precision Update)

- **Type**: Communication & Epistemic Precision Patch (No numerical results modified).
- **Previous Version**: `v1.0` (Frozen August 21, 2026)
- **New Version**: `v1.0.1` (August 22, 2026)
- **Modifications**:
  1. **Opening Causal Claim**: Replaced over-strong claim (*"inadvertently suppresses valid, multi-step exploration"*) with epistemically safer formulation (*"This raises the possibility that naive uncertainty weighting may downweight valid multi-step trajectories for reasons partly related to sequence length rather than correctness."*).
  2. **Section 2 ("Why This Matters")**: Replaced causal hypothesis (*"induces length penalty distortion, pushing the policy toward concise, brittle shortcuts"*) with precise boundary statement (*"If a length-confounded confidence proxy is used to scale policy-gradient advantages, longer trajectories may systematically receive different weights for reasons unrelated to correctness. Whether this produces a persistent preference for shorter reasoning requires separate evaluation."*).
  3. **Figure 1 Caption**: Replaced *"causes naive estimators to misidentify valid derivations as uncertain"* with *"Longer multi-step reasoning was associated with higher token entropy ($r = 0.486$) in the evaluated sample, illustrating how sequence length can confound interpretation of entropy as an uncertainty signal."*
  4. **Stress Test Interpretation (Section 8)**: Clarified downstream effect statement to emphasize observed misranking (42.1%) rather than downstream training degradation.
  5. **Section Numbering**: Standardized sequential 1–12 numbering across TOC and body headings.
  6. **Top Metadata Display**: Redesigned metadata component for clean visual separation of Article Version, Updated Date, Paper Revision, and GitHub Commit link.

---

### v1.0 — August 21, 2026 (Initial Public Release)

- **Type**: Initial Public Release
- **Paper Revision**: August 16, 2026
- **Research Code Commit**: `cc2bec46d5f2421873fe8adfb83b622ad6e10861`
- **Benchmark Data**: Untouched GSM8K ($N = 100$), Preregistered 5-Way RL Benchmark ($N = 3$ seeds).
