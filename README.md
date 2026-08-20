# StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training

[![CI](https://github.com/shamthakare/stateshift/actions/workflows/ci.yml/badge.svg)](https://github.com/shamthakare/stateshift/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Publication Status**: Submitted to *Artificial Intelligence* (Elsevier), 2026 — Manuscript ARTINT-D-26-01491  

---

## 📌 Executive Summary & Main Findings

Standard evaluations of reinforcement-learning (RL) post-training in large language models emphasize aggregate benchmark accuracy, potentially obscuring how local reasoning capabilities evolve during post-training. **StateShift** is a controlled framework that measures target-transition recovery conditional on intermediate reasoning state.

```
       Recovery Condition (R)                          Control Condition (C)
  [Invalid Intermediate State]                    [Matched Baseline State]
               │                                             │
               ▼                                             ▼
  Target-Transition Success (μ_R,t)              Target-Transition Success (μ_C,t)
               └──────────────────────┬──────────────────────┘
                                      ▼
                        Interaction Contrast (Γ_t)
                     Γ_t = (μ_R,t - μ_R,0) - (μ_C,t - μ_C,0)
```

### Key Empirical Results

| Study Phase | Sample Size | Primary Estimand | Empirical Value | 95% Problem-Blocked Bootstrap CI | Status / Interpretation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Study A (Endpoint)** | $N=454, K=16$ ($29,056$ rollouts) | $\Gamma_{256}$ | **`+0.1176`** | $[+0.0955, +0.1400]$ ($p < 0.0001$) | $+11.76$ percentage-point state-by-checkpoint interaction |
| **Strict Subgroup** | $N_{\text{Strict}}=388, K=16$ | $\Gamma_{256,\text{Strict}}$ | **`+0.1160`** | $[+0.0913, +0.1408]$ | Robust under strict decontamination filtering |
| **Trajectory (Step 32)** | $N=454, K=2/3$ | $\Gamma_{32}$ | **`+0.0333`** | $[+0.0011, +0.0655]$ (Multiplicity-Adj.) | Statistically detectable by earliest available checkpoint ($t=32$) |
| **Study B (Natural Recovery)**| $N=200, K=16$ ($3,200$ rollouts) | $\text{NRR}$ | **`30.93%`** | $[27.19\%, 34.82\%]$ ($180/582$ episodes) | Conditional natural post-error recovery rate ($\text{NEI}=18.19\%$) |

---

## 📈 Complete Nine-Checkpoint Empirical Trajectory

Evaluating intermediate checkpoints across post-training ($t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$) yields the empirical interaction vector:

$$\mathbf{\Gamma} = [0.0000,\ +0.0333,\ +0.0337,\ +0.0774,\ +0.0748,\ +0.0598,\ +0.0976,\ +0.0950,\ +0.1176]$$

![StateShift Trajectory](figures/figure2_trajectory.png)

> **Trajectory Interpretation**: Across nine empirically evaluated checkpoints, the interaction was consistent with a non-decreasing trajectory under prespecified order-restricted analysis (Pooled Adjacent Violators Algorithm, PAVA) despite local variation in unconstrained estimates. The interaction was already statistically detectable at the earliest available post-training checkpoint ($t=32$).

---

## 🎯 Scientific Claim Boundaries

To ensure scientific integrity, StateShift distinguishes between supported empirical conclusions and disallowed overclaims:

| Claim Topic | Supported Scientific Statement | Disallowed / Unsupported Overclaim |
| :--- | :--- | :--- |
| **Endpoint Contrast** | *"Between base and step-256 checkpoints, we observe an 11.76-percentage-point interaction ($\Gamma_{256}=+0.1176$)."* | ❌ *"11.76% acceleration"* |
| **Trajectory Trend** | *"Consistent with a non-decreasing trajectory under prespecified order-restricted analysis."* | ❌ *"Strict pairwise monotonicity across all checkpoints"* |
| **Emergence** | *"Interaction was already statistically detectable at the earliest available checkpoint, $t=32$."* | ❌ *"The effect emerged exactly at step 32"* |
| **Natural Recovery** | *"Among 582 verifier-confirmed natural error episodes, 180 subsequently satisfied autonomous recovery ($30.93\%$)."* | ❌ *"The model self-corrects 30.93% of the time"* |

---

## 🚀 Reproduction & Artifact Verification

StateShift is designed for 100% zero-GPU statistical reproduction using pure Python scripts:

### Installation
```bash
git clone https://github.com/shamthakare/stateshift.git
cd stateshift
pip install -e .
```

### Zero-GPU Statistical Reproduction
```bash
# 1. Run full statistical reproduction suite
python scripts/reproduce_analysis.py

# 2. Verify publication artifact assertions (100% match assertion)
python scripts/verify_artifacts.py

# 3. Run unit test suite
PYTHONPATH=. pytest tests/
```

---

## 🔗 Model Provenance & Checkpoint Lineage

All evaluated checkpoints belong to the open-source DeepScaler model lineage (`UWNSL/Qwen2.5-7B-deepscaler_4k_step_X`), anchored by the base model `Qwen/Qwen2.5-7B` at $t=0$:

| Checkpoint ($t$) | Repository ID | Verified Git Commit SHA |
| :---: | :--- | :--- |
| **$t=0$** | `Qwen/Qwen2.5-7B` | Base Pretrained Model |
| **$t=32$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_32` | `f46f9eac9908013a502735b7e882821f492ca61e` |
| **$t=64$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_64` | `d57afa929761825af618c6545ab7f7a5b28b3dc1` |
| **$t=96$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_96` | `5164cb6d7dcace900aed6a961cea33de40f2b6dc` |
| **$t=128$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_128` | `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec` |
| **$t=160$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_160` | `d8df8a5d6290bcc7b4b5fa108121cc5b9808bf58` |
| **$t=192$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_192` | `cb3f9bda37c44699246d04b9af21df41879e0ac3` |
| **$t=224$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_224` | `1833fa4e7beea19c2451e1f7a4dfe3068454edaf` |
| **$t=256$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` | `7667ad787966f5733fdca3d2b240452d7095ff95` |

---

## 📂 Repository Architecture

```
stateshift/
├── README.md
├── LICENSE (MIT)
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
│
├── stateshift/                    # Core Python package
│   ├── evaluation/                # Evaluator routines
│   ├── perturbations/             # Matched Recovery/Control state builder
│   ├── verification/              # Deterministic answer verifier
│   ├── statistics/                # Blocked bootstrap & NEI/NRR metrics
│   ├── trajectory/                # Order-restricted PAVA analysis
│   └── natural_recovery/          # Natural error episode detector
│
├── configs/                       # Experiment YAML configurations
├── scripts/                       # Reproduction & verification scripts
├── figures/                       # Vector PDF & PNG publication figures
├── tests/                         # Pytest unit & integrity test suite
├── docs/                          # Comprehensive methodology & audit docs
└── paper/                         # LaTeX manuscript companion source
```

---

## 📜 Citation & License

```bibtex
@article{Thakare2026StateShift,
  title={StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training},
  author={Thakare, Sham Satish},
  journal={Prepared/submitted to Artificial Intelligence (Elsevier)},
  year={2026}
}
```

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
