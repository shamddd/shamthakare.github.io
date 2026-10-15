# Scientific Claim Audit Log

**Author**: Sham Satish Thakare  
**Target Article**: *When Confidence Proxies Confound Reasoning Complexity*  
**Paper Basis**: IEEE TAI Submission ID `TAI-2026-Aug-A-01878`  
**Audit Status**: **100% PASSED**  

---

## Complete Claims Audit Matrix

| ID | Public Claim in Article | Evidence Source | Exact Location | Verified Value | Wording Safety Verification |
|---|---|---|---|---|---|
| **C1** | *"Token predictive entropy correlates strongly with sequence length ($r = +0.486$)."* | Table I in IEEE TAI PDF & `figure-data.json` | Table I, Row 2 (`rLen`) | $r = +0.486, 95\%\text{ CI } [+0.318, +0.627]$ | **VERIFIED YES** — Exact sample correlation on GSM8K ($N=100$). |
| **C2** | *"Controlling for completion length via partial correlation collapses the association between token entropy and error from $r = -0.214$ to $r_{\text{partial}} = -0.092$ ($p = 0.365$)."* | Table I in IEEE TAI PDF & `figure-data.json` | Table I, Row 2 (`Partial r (p)`) | $r_{\text{partial}} = -0.092, p = 0.365$ | **VERIFIED YES** — Statistically nonsignificant after controlling for length. |
| **C3** | *"Monte Carlo dropout forward passes on zero-dropout architectures produce deterministic outputs with zero variance ($\text{Var}(\log P) = 0.0$)."* | Section II in IEEE TAI PDF | Section II, Paragraph 2 | $\text{Var}(\log P) = 0.0000000000$, $\cos(\Delta\theta) = 1.000000$ | **VERIFIED YES** — Proved via compute graph audit on `Qwen2.5-0.5B-Instruct`. |
| **C4** | *"Token entropy misidentifies correct multi-step reasoning traces as more uncertain than short incorrect errors in 42.1% of paired comparisons."* | Section III in IEEE TAI PDF | Section III, Bullet 3 | 42.1% | **VERIFIED YES** — Evaluated on GSM8K Correct-but-Complex Stress Test. |
| **C5** | *"Self-Consistency ($K=4$) remains robust to length bias ($r = +0.114$, $r_{\text{partial}} = -0.569$, $p = 8.1\times 10^{-10}$, $\text{AUROC} = 0.812$)."* | Table I in IEEE TAI PDF | Table I, Row 1 | $\text{AUROC} = 0.812, r_{\text{partial}} = -0.569$ | **VERIFIED YES** — Statistically significant offline error predictor. |
| **C6** | *"In a preregistered 5-way controlled benchmark across 3 independent seeds, Consistency-Aware GRPO (CA-GRPO) achieved 80.00% Pass@1, identical to Standard GRPO (80.00%) and Permuted Control (80.00%) with Cohen's $d = 0.00$."* | Table II in IEEE TAI PDF | Table II, Rows 1, 4, 5 | Pass@1 $= 80.00\% \pm 0.00\%$, Cohen's $d = 0.00$ | **VERIFIED YES** — Exact 5-way benchmark results across $N=3$ training seeds. |
| **C7** | *"Compute-Matched GRPO ($K=8$) achieved 78.33% Pass@1, while Random Weight Control achieved 75.00% Pass@1."* | Table II in IEEE TAI PDF | Table II, Rows 2, 3 | $78.33\% \pm 2.89\%$ (K=8), $75.00\% \pm 5.00\%$ (Random) | **VERIFIED YES** — Exact baseline values from Table II. |
| **C8** | *"The paper status is currently submitted to IEEE Transactions on Artificial Intelligence."* | ScholarOne Submission Logs & `MANUAL_ACTION_REQUIRED.md` | Submission ID `TAI-2026-Aug-A-01878` | Submitted (IEEE TAI, Aug 2026) | **VERIFIED YES** — Correctly labeled as SUBMITTED, not published. |

---

## Audit Certification

Every numerical statement, correlation coefficient, $p$-value, AUROC score, and Pass@1 metric presented in the flagship research article has been cross-checked against the canonical LaTeX manuscript, PDF text, and `figure-data.json` logs. Zero numbers were fabricated or estimated.
