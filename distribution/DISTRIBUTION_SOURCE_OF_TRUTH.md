# Distribution Source of Truth

**Author**: Sham Satish Thakare  
**Target Paper**: *Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training*  
**Research Essay**: *When Confidence Proxies Confound Reasoning Complexity*  
**Last Verified Date**: August 22, 2026  

---

## Allowed Scientific Claims & Exact Verified Metrics

1. **Research Question**:
   - *What happens when uncertainty estimators respond to reasoning sequence length rather than genuine error during RLVR post-training?*

2. **Verified Result 1 (Sequence Length Confounding)**:
   - On GSM8K ($N = 100$ prompt clusters, 98 degrees of freedom), token predictive entropy was positively correlated with completion length:
     $$r = 0.486, \quad 95\%\text{ CI } [+0.318, +0.627]$$

3. **Verified Result 2 (Partial Correlation Collapse)**:
   - After controlling for sequence completion length via partial correlation, the association between token entropy and correctness decreased from $r = -0.214$ to:
     $$r_{\text{partial}} = -0.092, \quad p = 0.365 \quad \text{(not statistically significant)}$$

4. **Verified Result 3 (Zero-Dropout Architecture Probing)**:
   - On `Qwen2.5-0.5B-Instruct` (0 active `nn.Dropout` modules), nominal MC-dropout passes yielded deterministic repeated passes:
     $$\text{Var}(\log P) = 0.0000000000, \quad \cos(\Delta\theta) = 1.000000$$

5. **Verified Result 4 (Correct-but-Complex Stress Test)**:
   - In paired trace comparisons ($N = 100$ prompt clusters), token predictive entropy misidentified long correct derivations as more uncertain than short incorrect derivations in **42.1% of test cases**.

6. **Verified Result 5 (Self-Consistency Diagnostic Benchmark)**:
   - Self-consistency consensus ($K = 4$ rollouts) achieved offline error discrimination:
     $$\text{AUROC} = 0.812, \quad r = +0.114, \quad r_{\text{partial}} = -0.569, \quad p = 8.1 \times 10^{-10}$$

7. **Verified Result 6 (Preregistered 5-Way Controlled RL Benchmark across $N = 3$ Seeds)**:
   - Across $N = 3$ independent training seeds (42, 1337, 2026):
     - Standard outcome-supervised GRPO: $80.00\% \pm 0.00\%$
     - Proposed CA-GRPO: $80.00\% \pm 0.00\%$
     - Permuted Consistency Control (Negative Control): $80.00\% \pm 0.00\%$
     - Observed effect size: **Cohen's $d = 0.00$**

8. **Scope & Model Boundaries**:
   - These experiments evaluate `Qwen2.5-0.5B-Instruct`; they do not establish whether the same behavior holds at larger model scales or across other model families.

---

## Disallowed Language

- ❌ "Groundbreaking", "Revolutionary", "Breakthrough", "State-of-the-art", "Harvard-level", "World-class".
- ❌ Implying peer review, acceptance, active journal submission status, or institutional endorsement.
- ❌ Reporting Pass@1 without stating $N=3$ training seeds.
