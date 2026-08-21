# Medium Image QA Report

**Directory**: `assets/research/rlvr-reasoning/medium/`  
**Date**: August 22, 2026  

---

## High-Resolution Image Manifest & QA Verification

| Image File | Resolution | Background | Target Alt Text | Caption | QA Status |
|---|---|---|---|---|---|
| `hero-concept.png` | 1600 × 1600 px | Solid White | "Conceptual diagram showing longer reasoning associated with higher token entropy..." | Reasoning Complexity Confound Overview | **PASS** |
| `correlation-length-entropy.png` | 1600 × 1600 px | Solid White | "Scatter or summary plot showing positive association between completion length and token predictive entropy..." | Token predictive entropy was positively associated with completion length... | **PASS** |
| `stress-test-failure.png` | 1600 × 1600 px | Solid White | "Correct-but-complex stress test diagram comparing short incorrect derivation against long correct derivation..." | Correct-but-complex stress test. In 42.1% of evaluated paired comparisons... | **PASS** |
| `zero-dropout-audit.png` | 1600 × 1600 px | Solid White | "Architecture audit showing zero active dropout modules in the evaluated Qwen2.5-0.5B-Instruct configuration..." | In the evaluated Qwen2.5-0.5B-Instruct configuration, nominal MC-dropout produced no predictive variance... | **PASS** |
| `rl-control-results.png` | 1600 × 1600 px | Solid White | "Bar chart comparing Pass@1 across five controlled GRPO conditions over three training seeds..." | Across N = 3 evaluated training seeds, CA-GRPO and standard GRPO had the same observed mean Group Pass@1... | **PASS** |

---

## Image QA Criteria Checklist

- ✅ **Resolution**: Minimum 1600px wide (1600 × 1600 crisp resolution).
- ✅ **Theme Compatibility**: Flattened on solid white background for Medium's white theme.
- ✅ **Mobile Readability**: Generous padding, large legible typography at 375px width.
- ✅ **Branding & Claims**: Zero fake journal logos, zero un-supported claims, zero local `/Users/...` file paths.
