# recovery_eval

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![IEEE BigData 2026](https://img.shields.io/badge/IEEE%20BigData%202026-Submitted%20(BigD497)-orange.svg)](PUBLICATION_STATUS.md)

A provenance-aware, state-matched evaluation framework for studying recovery behavior in language-model reasoning.

---

## Research Paper

**Title:** `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Venue:** IEEE International Conference on Big Data (IEEE BigData 2026)  
**Submission ID:** `BigD497`  
**Associated Session:** 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026), Session #2  
**Status:** Submitted / Under review (Awaiting conference decision)  

---

## What `recovery_eval` Does

Standard benchmark evaluation measures aggregate end-to-end accuracy, which can conflate baseline generation fluency with true error recovery. `recovery_eval` provides a data-centric evaluation methodology to isolate state-specific reasoning performance:

* **Verifier-Defined Recovery States**: Identifies intermediate reasoning prefix errors using a deterministic verifier.
* **Structurally Matched Control States**: Prospective matching pairs recovery states with valid reference controls across continuous structural covariates (depth, remaining solution length, token length) under exact categorical matching constraints.
* **Append-Only Evidence Governance**: Maintains an append-only event ledger with cryptographic hashing to prevent data leakage and item re-selection.
* **Primitive Neural Rollout Provenance**: Logs input token IDs, output BPE token continuations, local weight manifests, and deterministic verifier execution outputs.
* **Independent Analysis Reconstruction**: Enables 100% analytical reconstruction directly from sealed raw evidence files.
* **Checkpoint-Interface Diagnostics**: Enables reproducible comparison between model checkpoints and prompt-interface configurations without confounding baseline fluency gains.

---

## Empirical Demonstration

We applied `recovery_eval` to evaluate error recovery across released checkpoint-interface configurations:

* **Scope**: 400 genuine neural continuations generated across 20 prospectively isolated GSM8K test problems ($N=20$).
* **Models**: `Qwen/Qwen2.5-Math-1.5B` (Base, commit `4a83ca6e`) and `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct, commit `aafeb0fc`).
* **Observed Continuation Success**:
  * Recovery States ($s_R$): Base $= 0.1500$, Instruct $= 0.5800$ (Difference: $+0.4300$)
  * Control States ($s_C$): Base $= 0.3800$, Instruct $= 0.9200$ (Difference: $+0.5400$)
* **Matched Recovery-Specific Contrast**: $D_{\text{recovery}} = \mathbf{-0.1100}$
* **95% Descriptive Bootstrap Interval**: $\mathbf{[-0.240, +0.030]}$ (10,000 resamples)

> **Empirical Finding**: Under the evaluated state-matched protocol, we did not observe evidence of a recovery-specific advantage for the Instruct checkpoint over the Base checkpoint. Aggregate continuation success gains (+0.4300 on recovery vs +0.5400 on control) reflect overall baseline fluency improvements rather than a specialized error-recovery mechanism.

---

## Research Integrity

This project maintains strict research integrity and scientific transparency:

* **Historical Retraction Transparency**: Prior exploratory research stages (Stage 8 / Stage 9) relied on simulated synthetic testbed data. Following a forensic audit, those simulation claims were formally retracted and replaced by genuine neural execution.
* **Auditability**: Historical retraction documentation is preserved in `research-next/strategy_change/stage9d3/` for archival provenance.
* **Genuine Neural Continuations**: All active empirical results in the IEEE BigData submission derive exclusively from PyTorch `model.generate()` tensor outputs generated on Apple Silicon MPS (`mps:0`).
* **Sealed Evidence**: Raw evidence (`RAW_NEURAL_ROLLOUTS.jsonl`, SHA-256 `51b5a157d9e4...`) and submission packages are hash-sealed and version-controlled.

---

## Reproducibility

### Execution Specifications
* **Models**: `Qwen/Qwen2.5-Math-1.5B` & `Qwen/Qwen2.5-Math-1.5B-Instruct`
* **Hardware**: Apple Silicon MPS (`mps:0`), FP16 precision
* **Sampling Parameters**: Temperature $t=0.0$ (greedy decoding), `top_p=1.0`, `max_new_tokens=512`
* **Rollout Design**: 400 continuations (20 problems $\times$ 2 states $\times$ 2 policies $\times$ 5 rollout seeds)
* **Matching Thresholds**: Normalized weighted-L1 distance $d \le 0.25$ (standard) and $d \le 0.10$ (tight); 20/20 pairs satisfied both thresholds ($d_{\text{mean}} = 0.0360$).

### Quick Start & Verification Commands

1. **Run Unit & Integrity Tests**:
   ```bash
   pytest -q research-next/ieee_bigdata_2026/tests/
   ```

2. **Verify Python Package Import**:
   ```bash
   python -c "import recovery_eval; print(recovery_eval.__version__)"
   ```

3. **Execute CLI Interface**:
   ```bash
   recovery-eval --help
   recovery-eval audit --raw-evidence RAW_NEURAL_ROLLOUTS.jsonl
   ```

---

## Repository Structure

```text
recovery_eval/
├── PUBLICATION_STATUS.md                  # Current IEEE BigData submission status
├── README.md                              # Main research project overview
├── CITATION.cff                           # CFF citation metadata
├── CITATION.bib                           # BibTeX citation entry
├── recovery_eval/                         # Core Python package codebase
├── research-next/ieee_bigdata_2026/       # Active IEEE BigData 2026 research workflow
│   ├── 00_audit/                          # Governance & canary audit scripts
│   ├── 01_literature/                     # Literature analysis & reference audit
│   ├── 02_novelty/                        # Methodological contrast analysis
│   ├── 03_protocol/                       # Prospective matching protocol
│   ├── 05_framework/                      # Evidence ledger & verifier logic
│   ├── 07_execution/                      # Neural rollout execution scripts
│   ├── 08_analysis/                       # Statistical bootstrap & contrast analysis
│   ├── 09_genuine_execution_v1/           # Sealed raw evidence & certificates
│   ├── manuscript/                        # IEEEtran TeX source & figure generation
│   └── tests/                             # Test suite for evaluation reproducibility
├── submission_bigdata2026_main_v3/        # CyberChair submission bundle & manifests
└── tests/                                 # Package unit tests
```

---

## Manuscript Availability

The submitted manuscript is currently under review at **IEEE BigData 2026**.

* **Status**: Manuscript available upon request while under review.

---

## Citation

If you use the `recovery_eval` framework or codebase in your research, please cite:

```bibtex
@unpublished{thakare2026recoveryeval,
  author = {Thakare, Sham Satish},
  title = {recovery\_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning},
  year = {2026},
  note = {Submitted to IEEE BigData 2026, Submission ID BigD497}
}
```

---

## License

This project is licensed under the [MIT License](LICENSE).
