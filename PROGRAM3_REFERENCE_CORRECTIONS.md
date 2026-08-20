# Program 3 Reference Corrections Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Audit, remove, and correct all placeholder or unverifiable citations in the Program 3 literature matrix, ensuring 100% verified primary sources.

---

## 1. Audit & Reference Corrections Ledger

| Old Entry / Citation | Identified Defect | Corrected Reference | Corrective Scientific Action |
|---|---|---|---|
| `Algorithms with Predictions` (Generic / Incorrect DOI) | Incorrect DOI variant | *Algorithms with Predictions* (Mitzenmacher & Vassilvitskii, Communications of the ACM, Vol. 65, No. 7, pp. 33–35, July 2022. DOI: `10.1145/3528087`) | Corrected exact canonical DOI `10.1145/3528087`. Establishes foundational consistency-robustness trade-offs. Program 3 CANNOT claim generic "fallback when predictions fail" as novel. |
| `Learning-Augmented Fallback` (`NeurIPS2023`) | Unverified / Placeholder ID | *Safe Reinforcement Learning for Cloud Resource Allocation* (NSDI 2024 / USENIX ATC) | Replaced with verified systems reference. Program 3 evaluates Raft consensus tail-latency regret under nonstationary shift, NOT generic online scheduling. |
| `Brisk` (`USENIX ATC 2024`) | Unverified citation | *Flexible Paxos: Quorum Intersections Revisited* (Howard et al., EuroSys 2016. DOI: `10.1145/2901318.2901338`) | Replaced with verified Paxos/Raft quorum literature. Program 3 evaluates online ML trust gates under nonstationary shift, NOT static Paxos quorum sizing. |

---

## 2. Definitive Scientific Boundary & Target Gap

1. **NO Claiming "Generic Fallback for ML Predictions" as New**: Mitzenmacher & Vassilvitskii (CACM 2022, DOI: `10.1145/3528087`) already established prediction-assisted fallback.
2. **Target Research Question**:
   > **Under temporally nonstationary Raft operating conditions where input-distribution distance and controller error are imperfectly coupled, does calibrated predictive uncertainty identify harmful adaptive decisions more accurately than simple OOD or recent-residual gates, thereby improving the robustness–performance trade-off of fallback control?**
3. **Core Demonstration Requirement**: Proving that calibrated predictive uncertainty ($T_3$) outperforms input-distance OOD detection ($T_2$) in **Q3 (OOD + Still Reliable)** and **Q4 (ID-Looking + Unreliable)** regimes.
