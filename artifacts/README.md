# StateShift Empirical Scientific Artifacts

This directory contains the frozen, immutable empirical datasets, rollout outcome ledgers, trajectory vectors, natural error logs, and provenance manifests supporting the StateShift paper (*Submitted to Artificial Intelligence, Elsevier, manuscript ARTINT-D-26-01491*).

---

## Directory Overview

### 1. `endpoint/` (Study A Controlled Endpoint)
* `controlled_endpoint_outcomes.csv`: Raw outcome ledger for $N=454, K=16, 29,056$ primary rollouts comparing base ($t=0$) and step-256 checkpoints.
* `strict_decontamination_subset.csv`: Strict decontamination subgroup results ($N_{\text{Strict}}=388, \Gamma_{256,\text{Strict}} = +0.1160$).
* `endpoint_summary_numbers.csv`: Canonical endpoint statistical summary.

### 2. `trajectory/` (Nine-Checkpoint Empirical Trajectory)
* `nine_checkpoint_trajectory.csv`: Full 9-point interaction vector $\mathbf{\Gamma} = [0.0000, 0.0333, 0.0337, 0.0774, 0.0748, 0.0598, 0.0976, 0.0950, 0.1176]$.
* `intermediate_rollouts.jsonl`: Raw rollout records for intermediate checkpoints ($t \in \{32, 96, 160, 224\}$).
* `intermediate_checkpoint_cell_means.csv`: Intermediate cell means ($\mu_{R,t}, \mu_{C,t}$).
* `adjacent_differences.csv`: Checkpoint-to-checkpoint adjacent differences $\Delta \Gamma_t$.

### 3. `natural_recovery/` (Study B Unprompted Natural Post-Error Recovery)
* `natural_error_episodes.csv`: 582 verifier-confirmed natural reasoning error episodes across 3,200 rollouts ($\text{NEI}=18.19\%$).
* `natural_recovery_episodes.csv`: 180 qualifying autonomous recovery episodes ($\text{NRR}=30.93\%$).

### 4. `provenance/` (Model Provenance & Cryptographic Hashes)
* `checkpoint_provenance.csv`: Hugging Face repository IDs and verified commit SHAs for all 9 checkpoints.
* `verified_sha256_manifest.csv`: Cryptographic SHA-256 checksums for empirical outcome files.
* `confirmatory_problem_registry.json`: Decontaminated problem registry definitions ($N=454$).
