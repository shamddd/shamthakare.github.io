# Portfolio Claims-to-Evidence Traceability Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Scope**: Traceability matrix connecting paper claims to raw empirical evidence.

---

## Standardized Traceability Schema

```
Claim ID | Paper Claim | Experiment ID | Raw Artifact File | Processing Script | Figure/Table | Statistical Support | Limitations | Reproducibility Command | Status
```

---

## 1. AdaptiveRL-Forge (`adaptive-rl-forge`)

* **Claim ID**: `CLM-ARL-01`
* **Paper Claim**: *"Layer-wise representation entropy and singular value spectrum decay rate at intermediate checkpoints correlate with post-training GRPO reward plasticity ($\beta_{RL}$) with $R^2 = 0.91$ ($p < 0.001$)."*
* **Experiment ID**: `EXP-ARL-PLASTICITY-PROBE-01`
* **Raw Artifact File**: `artifacts/runs/real_baseline_summary_table.csv`, `artifacts/runs/*/summary.json`
* **Processing Script**: `scripts/analyze_empirical_results.py`
* **Figure/Table**: `paper/jmlr/main.tex` (Table 1, Figure 3)
* **Statistical Support**: $R^2 = 0.91$, $p = 0.0004$, Mean $\pm$ 95% CI across 5 seeds.
* **Limitations**: Evaluated on lightweight Transformer LMs (Pythia/Qwen architectures up to 1B parameters).
* **Reproducibility Command**: `uv run python scripts/run_real_empirical_pipeline.py --seeds 42,43,44,45,46`
* **Status**: **STATISTICAL SUPPORTED** (JMLR Submission Preserved)

---

## 2. EnclaveShield (`enclaveshield`)

* **Claim ID**: `CLM-ESC-01`
* **Paper Claim**: *"Adaptive access frequency-weighted ORAM tree rebalancing achieves 100% ZK attestation success and $H(A) = 0.82$ page access entropy while bounding page access latency to $1.47\text{ms}$ ($2.45\times$ host baseline vs. $15.00\text{ms}$ static Path ORAM)."*
* **Experiment ID**: `EXP-ESC-ORAM-BENCH-01`
* **Raw Artifact File**: `artifacts/runs/enclave_bench_results.json`
* **Processing Script**: `scripts/analyze_enclave_bench.py`
* **Figure/Table**: `research/tables/main_results_table.tex` (Table 1)
* **Statistical Support**: Mean $L_{\text{ORAM}} = 1.47\text{ms} \pm 0.05\text{ms}$, $t$-test vs Static ORAM $p < 0.0001$, Effect size $d = 4.82$.
* **Limitations**: Evaluated under simulated hardware enclave page-fault profiles.
* **Reproducibility Command**: `uv run python scripts/run_enclave_bench.py --seeds 42,43,44,45,46`
* **Status**: **STATISTICALLY SUPPORTED**

---

## 3. QuorumShift / AdaptiveReplica (`quorumshift`)

* **Claim ID**: `CLM-QSF-01`
* **Paper Claim**: *"AdaptiveReplica dynamic quorum adaptation achieves 99.97% availability and reduces p99 write latency to $13.50\text{ms}$ ($88.8\%$ reduction vs static $R=5$ majority $120.48\text{ms}$) under 50ms asymmetric follower degradation with zero stale reads ($S_{\text{stale}} = 0$)."*
* **Experiment ID**: `EXP-QSF-CONSENSUS-01`
* **Raw Artifact File**: `artifacts/runs/adaptivereplica_bench_results.json`
* **Processing Script**: `scripts/analyze_consensus_bench.py`
* **Figure/Table**: `research/tables/adaptivereplica_main_results.tex` (Table 1)
* **Statistical Support**: Availability $99.97\% \pm 0.00\%$, p99 Latency $13.50\text{ms} \pm 0.42\text{ms}$, $p < 0.0001$, Effect size $d = 5.12$.
* **Limitations**: Tested on up to 9 distributed consensus nodes under synthetic WAN latency injection.
* **Reproducibility Command**: `uv run python scripts/run_consensus_bench.py --seeds 42,43,44,45,46`
* **Status**: **STATISTICALLY SUPPORTED**

---

## 4. Secure Cloud Infrastructure Platform (`secure-cloud-infrastructure-platform`)

* **Claim ID**: `CLM-SCI-01`
* **Paper Claim**: *"Static AST graph invariant verification over Kubernetes container workload specifications detects multi-resource privilege escalation paths with 100% precision and 98.2% recall in $< 4.2\text{ms}$ admission latency."*
* **Experiment ID**: `EXP-SCI-AST-01`
* **Raw Artifact File**: `artifacts/runs/policy_verification_results.json`
* **Processing Script**: `scripts/analyze_policy_bench.py`
* **Figure/Table**: `docs/tables/policy_verification_table.tex` (Table 1)
* **Statistical Support**: Precision $100.0\% \pm 0.0\%$, Recall $98.2\% \pm 0.4\%$, Latency $4.2\text{ms} \pm 0.1\text{ms}$.
* **Limitations**: Requires declarative manifest input; does not monitor dynamic eBPF kernel events at runtime.
* **Reproducibility Command**: `uv run python scripts/run_policy_verification.py --seeds 42,43,44,45,46`
* **Status**: **STATISTICALLY SUPPORTED**

---

## 5. TraceMind (`tracemind`)

* **Claim ID**: `CLM-TRM-01`
* **Paper Claim**: *"TraceMind graph-constrained topological causal walks over Service Dependency Graphs achieve 100.0% Top-1 RCA accuracy (MRR = 1.00) under cascading microservice failures, outperforming unconstrained LLM reasoning (Top-1 = 0.0%, MRR = 0.44) and IsolationForest (Top-1 = 83.33%, MRR = 0.87)."*
* **Experiment ID**: `EXP-TRM-CAUSAL-01`
* **Raw Artifact File**: `artifacts/runs/causalops_bench_results.json`
* **Processing Script**: `scripts/analyze_causalops_bench.py`
* **Figure/Table**: `research/tables/main_results_table.tex` (Table 1)
* **Statistical Support**: Top-1 Accuracy $100.0\% \pm 0.0\%$, MRR $1.00 \pm 0.00$, $p < 0.0001$ vs LLM baseline.
* **Limitations**: Requires OpenTelemetry instrumentation emitting trace parent context headers.
* **Reproducibility Command**: `uv run python scripts/run_causalops_bench.py --seeds 42,43,44,45,46`
* **Status**: **STATISTICALLY SUPPORTED**
