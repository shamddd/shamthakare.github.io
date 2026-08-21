# Blog vs Paper Boundary Audit

**Author**: Sham Satish Thakare  
**Article**: *When Confidence Proxies Confound Reasoning Complexity*  
**Last Audit Date**: August 21, 2026  

---

## Claim & Evidence Boundary Verification

| Blog Claim | Paper Support | Raw-Data Support | Interpretation Only? | Wording Safety Audit | Safe? |
|---|---|---|---|---|---|
| *"Token predictive entropy was positively correlated with completion length ($r = 0.486, 95\%\text{ CI } [+0.318, +0.627]$)."* | Table I in IEEE TAI paper | `figure-data.json` / GSM8K $N=100$ | No (Direct empirical metric) | Quantitative wording without subjective adjectives ("strongly"). | **SAFE** |
| *"Controlling for completion length via partial correlation collapsed the association between token entropy and correctness to $r_{\text{partial}} = -0.092$ ($p = 0.365$)."* | Table I in IEEE TAI paper | `figure-data.json` / 98 df | No (Direct partial correlation) | Exact numerical output, non-significant $p$-value stated. | **SAFE** |
| *"In the evaluated zero-dropout architecture (`Qwen2.5-0.5B-Instruct`), nominal MC-dropout sampling produced deterministic repeated passes ($\text{Var}(\log P) = 0.0000000000$)."* | Section II in IEEE TAI paper | Model graph inspection & tensor log | No (Direct compute graph audit) | Scoped strictly to `Qwen2.5-0.5B-Instruct` zero-dropout configuration. | **SAFE** |
| *"Token entropy misidentified correct multi-step reasoning traces as more uncertain than short incorrect errors in 42.1% of paired comparisons."* | Section III in IEEE TAI paper | GSM8K Stress Test ($N=100$) | No (Paired comparison count) | Exact observed ratio in correct-but-complex stress benchmark. | **SAFE** |
| *"Self-Consistency consensus ($K=4$) was robust to length bias ($r = +0.114$, $r_{\text{partial}} = -0.569, p = 8.1\times 10^{-10}$, $\text{AUROC} = 0.812$)."* | Table I in IEEE TAI paper | `figure-data.json` | No (Direct diagnostic metric) | Exact AUROC and partial correlation reported. | **SAFE** |
| *"Across the three evaluated seeds ($N=3$), CA-GRPO and standard outcome-supervised GRPO produced the same observed mean Group Pass@1 ($80.00\% \pm 0.00\%$) with an observed effect size of Cohen's $d = 0.00$."* | Table II in IEEE TAI paper | `figure-data.json` / $N=3$ seeds | No (Direct Pass@1 measurement) | States observed equality across 3 seeds without asserting statistical proof of universal equivalence. | **SAFE** |

---

## Explicit Boundaries (What the Study Does NOT Establish)

The public article explicitly includes a **"What We Found / What We Didn't Find"** panel stating:
1. **Model Scope**: Findings are evaluated on `Qwen/Qwen2.5-0.5B-Instruct` and do not test models $>7\text{B}$ parameters.
2. **Domain Scope**: Evaluated on mathematical reasoning (GSM8K, SVAMP) and does not extend to open-ended code generation or medical diagnosis.
3. **Method Boundary**: Tests trajectory-level multiplicative advantage scaling and does not rule out step-level Process Reward Models (PRMs).
4. **Seed Limit**: The controlled RL benchmark uses $N = 3$ independent training seeds; observed equality ($80.00\%$) reflects this evaluated sample size and does not constitute a formal statistical proof of universal non-inferiority.
