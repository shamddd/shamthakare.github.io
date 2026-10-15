# Figure Provenance Log

**Author**: Sham Satish Thakare  
**Target Article**: *When Confidence Proxies Confound Reasoning Complexity*  
**Canonical Data Source**: [`data/rlvr-reasoning/figure-data.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/shamthakare.github.io/data/rlvr-reasoning/figure-data.json)  
**Paper Reference**: IEEE TAI Submission ID `TAI-2026-Aug-A-01878`  
**Last Verified Date**: August 21, 2026  

---

## Provenance Registry

| Figure ID | Asset File | Source Data / Location | Source Experiment / Run | Key Metric / Value | Sample Size ($N$) | Statistical / Uncertainty Method | Last Verified |
|---|---|---|---|---|---|---|---|
| **FIG 1** | `hero-concept.svg` | `figure-data.json` / `table_1_proxies` | Diagnostic Benchmark Run | Token Entropy $r = +0.486$ vs Length | $N=100$ prompt clusters | Pearson $r$, 95% CI | 2026-08-20 |
| **FIG 2** | `assumption-vs-reality.svg` | Section III of IEEE TAI paper | GSM8K Stress Benchmark | 42.1% Misidentification Rate | $N=100$ prompts | Paired comparison ratio | 2026-08-20 |
| **FIG 3** | `zero-dropout-audit.svg` | Section II of IEEE TAI paper | Compute Graph Audit | $\text{Var}(\log P) = 0.0000000000$, $\cos(\Delta\theta)=1.000000$ | Exact model graph (`Qwen2.5-0.5B`) | Direct tensor variance & cosine similarity | 2026-08-20 |
| **FIG 4** | `experiment-pipeline.svg` | Section IV of IEEE TAI paper | Preregistered RL Protocol | $K=4 / K=8$ rollouts, 256-token budget | $N=3$ independent seeds | Standard deviation across seeds | 2026-08-20 |
| **FIG 5** | `correlation-length-entropy.svg` | `figure-data.json` / `table_1_proxies` | GSM8K Correlation Run | Partial $r = -0.092$ ($p = 0.365$) | $N=100$ prompt clusters (98 df) | Partial correlation controlling for length | 2026-08-20 |
| **FIG 6** | `auroc-benchmark.svg` | `figure-data.json` / `table_1_proxies` | Diagnostic Benchmark | Self-Consistency AUROC = 0.812 vs Token Entropy 0.618 | $N=100$ prompt clusters | Area Under ROC Curve | 2026-08-20 |
| **FIG 7** | `rl-control-results.svg` | `figure-data.json` / `table_2_rl_controls` | Preregistered 5-Way Controlled RL Benchmark | Standard GRPO 80.00% vs CA-GRPO 80.00% | $N=3$ independent seeds | Mean Pass@1 (%) ± SD, Cohen's $d = 0.00$ | 2026-08-20 |
| **FIG 8** | `stress-test-failure.svg` | Section III of IEEE TAI paper | Correct-but-Complex Derivation Test | 42.1% misranking of long correct vs short incorrect | $N=100$ prompt clusters | Paired trace misclassification ratio | 2026-08-20 |
| **FIG 9** | `limitations-boundary.svg` | Section V of IEEE TAI paper | Scope Audit | Model size (< 7B), domains (GSM8K/SVAMP) | Verified scope boundary | Qualitative & empirical scope mapping | 2026-08-20 |

---

## Regeneration Command

To re-generate all figure assets programmatically from the canonical JSON data:

```bash
python3 /Users/shamthakare/.gemini/antigravity/scratch/shamthakare.github.io/scripts/generate_figures.py
```
