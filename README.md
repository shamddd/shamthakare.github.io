# StateShift

State-conditioned evaluation of reasoning recovery across reinforcement learning post-training checkpoints.

[![CI](https://github.com/shamddd/stateshift/actions/workflows/ci.yml/badge.svg)](https://github.com/shamddd/stateshift/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)

**Publication Status**: Submitted to *Artificial Intelligence* (Elsevier), 2026 — Manuscript ARTINT-D-26-01491

---

## Overview

Standard evaluations of reinforcement-learning (RL) post-training in large language models emphasize aggregate benchmark accuracy, which can mask behavioral changes conditional on local reasoning state. StateShift is an experimental framework designed to measure target-transition recovery conditional on intermediate reasoning state.

By comparing model completion success under matched Recovery (invalid intermediate step) and Control (baseline step) conditions, StateShift isolates the state-dependent transition capability acquired during post-training.

---

## Main Results

* **Controlled Endpoint Interaction ($\Gamma_{256}$)**: Between base ($t=0$) and step-256 checkpoints, we observe an 11.76-percentage-point interaction ($\Gamma_{256} = +0.1176$, $95\%$ problem-blocked bootstrap CI $[+0.0955, +0.1400]$).
* **Strict Decontamination Subgroup**: Under strict decontamination filtering ($N_{\text{Strict}}=388$), the interaction remains robust ($\Gamma_{256,\text{Strict}} = +0.1160$, $95\%$ CI $[+0.0913, +0.1408]$).
* **Earliest Detectable Checkpoint ($t=32$)**: The interaction is statistically detectable by the earliest available post-training checkpoint ($t=32$, $\Gamma_{32} = +0.0333$, multiplicity-adjusted $95\%$ CI $[+0.0011, +0.0655]$).

---

## Method

StateShift compares model behavior across two counterfactual states for each problem:

1. **Recovery Condition ($R$)**: An intermediate reasoning state containing a verifier-confirmed invalid step.
2. **Control Condition ($C$)**: A matched baseline state matched for length and context.

The difference-in-differences interaction contrast $\Gamma_t$ at checkpoint step $t$ is calculated as:

$$\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$$

where $\mu_{R,t}$ and $\mu_{C,t}$ denote target-transition success rates in the Recovery and Control conditions, respectively.

---

## Training Trajectory

Evaluating intermediate checkpoints ($t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$) yields the nine-point empirical interaction vector:

$$\mathbf{\Gamma} = [0.0000,\ +0.0333,\ +0.0337,\ +0.0774,\ +0.0748,\ +0.0598,\ +0.0976,\ +0.0950,\ +0.1176]$$

![StateShift Trajectory](figures/figure2_trajectory.png)

Across nine empirically evaluated checkpoints, the interaction was consistent with a non-decreasing trajectory under prespecified order-restricted analysis (Pooled Adjacent Violators Algorithm, PAVA) despite local variation in unconstrained estimates.

**Claim Boundaries**:
* Strict monotonicity across all adjacent checkpoints is **not established** due to sampling variation at intermediate checkpoints.
* The exact training step at which the interaction emerged is **not identifiable** because checkpoints between $t=0$ and $t=32$ are unavailable.
* Checkpoint $t=32$ represents the **earliest available** statistically detectable checkpoint in the evaluated lineage.

---

## Natural Recovery

In a separate study of 3,200 unperturbed rollouts across 200 problems (Study B):

* **Natural Error Incidence ($\text{NEI}$)**: $18.19\%$ of rollouts contained a verifier-confirmed natural reasoning error ($582/3200$).
* **Conditional Natural Post-Error Recovery Rate ($\text{NRR}$)**: Among 582 qualifying error episodes, 180 subsequently satisfied the autonomous recovery criterion ($30.93\%$, $95\%$ problem-blocked bootstrap CI $[27.19\%, 34.82\%]$).

---

## Reproducing the Analysis

To run statistical reproduction, artifact verification, and unit tests:

```bash
python -m pip install -e .
python scripts/reproduce_analysis.py
python scripts/verify_artifacts.py
PYTHONPATH=. pytest tests/
```

---

## Repository Structure

```
stateshift/
├── README.md
├── LICENSE
├── CITATION.cff
├── CITATION.bib
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .gitattributes
├── .github/
│   └── workflows/ci.yml
├── stateshift/
├── configs/
├── scripts/
├── tests/
├── figures/
├── docs/
├── artifacts/
└── paper/
```

---

## Model Provenance

Detailed checkpoint commit SHAs, weight identity proofs, and Hugging Face repository mappings are documented in [`docs/MODEL_PROVENANCE.md`](docs/MODEL_PROVENANCE.md).

---

## Citation

```bibtex
@unpublished{thakare2026stateshift,
  author = {Thakare, Sham Satish},
  title = {StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training},
  year = {2026},
  note = {Submitted to Artificial Intelligence (Elsevier), manuscript ARTINT-D-26-01491}
}
```

---

## License

Distributed under the [MIT License](LICENSE).
