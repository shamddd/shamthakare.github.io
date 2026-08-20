# Repository Consolidation Plan

**Author**: Sham Satish Thakare  
**Purpose**: Architectural plan for consolidating existing codebase repositories into the 4 Primary Research Programs without breaking publication reproducibility for submitted manuscripts.

---

## Repository Mapping & Action Grid

| Existing Repository | Primary Target Program | Keep | Merge | Archive | Rename | Scientific Rationale & New Boundary |
|---|---|---|---|---|---|---|
| `ear_grpo_reasoning` | **Program 1** | **YES** | No | No | No | **FROZEN FOR SUBMISSION**. Maintains 100% exact reproducibility for the submitted IEEE TAI manuscript. No structural edits to existing code or results. |
| `adaptive-rl-forge` | **Program 1** | **YES** | Yes | No | No | **EXTEND AS PRIMARY CODEBASE FOR PROGRAM 1**. Receives new calibration evaluation modules (`compute_expected_calibration_error`) and Brier-GRPO calibration loss functions. |
| `agentguard-final` | **Program 2** | **YES** | Yes | No | No | **EXTEND AS PRIMARY CODEBASE FOR PROGRAM 2**. Integrates `medirush` agent policy guardrails into a single long-horizon agent reliability benchmark (`AgentGuard-LongHorizon`). |
| `medirush` | **Program 2** | No | **YES** | Yes | No | **MERGE INTO AGENTGUARD-FINAL**. Domain-specific healthcare tools merged into `agentguard-final/benchmarks/medirush/`. Repository archived as preserved publication prep. |
| `quorumshift` | **Program 3** | **YES** | No | No | No | **EXTEND AS PRIMARY CODEBASE FOR PROGRAM 3**. Contains C++20 Raft joint-consensus engine. Extended to evaluate uncertainty-aware reliability envelopes for learned controllers. |
| `tracemind` | **Program 4** | **YES** | Yes | No | No | **EXTEND AS PRIMARY CODEBASE FOR PROGRAM 4**. OpenTelemetry service dependency graph parser extended with ZK audit proof hooks from `enclaveshield`. |
| `enclaveshield` | **Program 4** | No | **YES** | Yes | No | **MERGE ZK MODULES INTO TRACEMIND**. ZK quote verifier and Path ORAM attestation modules merged into `tracemind/security/zk/`. Repository archived as preserved research artifact. |

---

## Detailed Consolidation Directives

1. **Submission Reproducibility Preservation**:
   - `ear_grpo_reasoning` is under active review at IEEE TAI. **Zero changes** will be made to its commit history, results files, or manuscript sources.
   - `adaptive-rl-forge` is under active review at JMLR. New calibration extensions are added in separate submodules (`adaptive_rl_forge/eval/evaluator.py`, `adaptive_rl_forge/rl/grpo_trainer.py`) without modifying pre-existing diagnostic probe functions.

2. **Codebase Unification**:
   - Program 1 codebase: `adaptive-rl-forge` (Python / PyTorch)
   - Program 2 codebase: `agentguard-final` (Python / Agent Benchmark Harness)
   - Program 3 codebase: `quorumshift` (C++20 / Raft Systems Engine)
   - Program 4 codebase: `tracemind` (Python / C++ ZK Observability Engine)

3. **No Salami Publication Guarantee**:
   - Each of the 4 unified codebases supports exactly **ONE primary research manuscript**, eliminating code fragmentation across minor papers.
