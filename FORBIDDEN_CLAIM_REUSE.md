# Forbidden Claim Reuse & Intellectual Property Firewall

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Immutable firewall specifying forbidden claims, permissible infrastructure reuse, and required disclosure protocols to prevent self-plagiarism across all 4 Primary Research Programs.

---

## 1. Already Claimed (Forbidden Scientific Claims)

The following claims belong strictly to the 3 submitted manuscripts and **MUST NEVER BE PRESENTED AS NEW DISCOVERIES**:

### From Manuscript 1 (`PUB-001` - IEEE TAI Submission)
* ❌ Claiming that token predictive entropy, mean NLL, or logit margin measure reasoning uncertainty independently of derivation length ($r = +0.486$).
* ❌ Claiming that online sample-level consensus-weighted GRPO (CA-GRPO) improves Pass@1 reasoning accuracy over standard outcome-supervised GRPO (falsified; $\Delta = 0.00\%$).
* ❌ Claiming that modern zero-dropout causal LLMs (Qwen2.5) support active MC-dropout hidden-state probing ($\text{Var}=0.0$).

### From Manuscript 2 (`PUB-002` - IEEE BigData 2026 / MLBD 2026 `BigD497`)
* ❌ Claiming that post-trained instruction checkpoints (`Qwen2.5-Math-1.5B-Instruct`) possess a specialized error-recovery advantage over base models ($D_{\text{recovery}} = -0.1100$).
* ❌ Claiming the verifier-defined state-matched recovery evaluation protocol (`recovery_eval`) as a new methodological contribution.

### From Manuscript 3 (`PUB-003` - TMLR / NeurIPS Workshop Submission)
* ❌ Claiming the formal deployment-amortized intervention cost model $C_{\text{total}}(a, Q) = C_{\text{train}}(a) + Q \cdot C_{\text{inference}}(a)$ as a new equation.
* 
* ❌ Claiming the empirical finding that OOD length extrapolation reduces the break-even query horizon ($R_f < 1.0$, $R_f \approx 0.0618$).

---

## 2. May Reuse (Infrastructure & Shared Software)

The following software components and general utilities may be reused across new research programs without restricting novelty:
* ✅ PyTorch GRPO policy gradient training loops (`adaptive_rl_forge/rl/grpo_trainer.py`).
* ✅ Exact-match mathematical answer verifiers and reward extractors (`ExactMatchRewardVerifier`).
* ✅ OpenTelemetry trace parsers and dependency graph construction utilities (`TraceMind`).
* ✅ C++20 Raft consensus engine infrastructure (`quorumshift`).
* ✅ ZK quote verification and Path ORAM node rebalancing primitives (`enclaveshield`).
* ✅ Standard public datasets (GSM8K, MATH, SVAMP) provided problem indices are documented.

---

## 3. May Reuse Only With Explicit Disclosure

* ⚠️ Specific dataset subsets used in prior submissions (e.g., GSM8K indices 0–99 used in `PUB-001`, indices 500–549 used in `PUB-002`). New experiments must document index boundaries.
* ⚠️ Fine-tuned model checkpoints generated during prior submission pipelines.
* ⚠️ Performance baselines directly cited from `PUB-001`, `PUB-002`, or `PUB-003`.

---

## 4. Must NOT Present As New

* 🚫 Existing hypotheses tested in `PUB-001`, `PUB-002`, or `PUB-003`.
* 🚫 Existing numerical benchmark results or figures from submitted papers.
* 🚫 Renaming an existing algorithm or metric (e.g., renaming CA-GRPO or $D_{\text{recovery}}$).
* 🚫 Presenting a pre-existing codebase extension as a standalone theoretical contribution without new empirical evidence.
