# Program 2 Reference Corrections Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Audit, remove, and correct all placeholder, outdated, or mischaracterized reference citations in Program 2 literature matrix.

---

## 1. Audit & Reference Corrections Ledger

| Old Entry / Citation | Identified Defect | Corrected Reference | Corrective Scientific Action |
|---|---|---|---|
| `2501.ToolShield` | Placeholder / Fabricated ID | *Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents* (ToolShield / MT-AgentRisk, arXiv:2402.13379) | Replaced with real paper. Corrected claim: ToolShield evaluates multi-turn tool interaction safety, NOT just single-turn filtering. Program 2 MUST NOT claim multi-turn safety as new. |
| `2501.SODA` | Placeholder / Fabricated ID | *The Cold-Start Safety Gap in LLM Agents* (SODA Benchmark, arXiv:2406.07867) | Replaced with real paper. Establishes that agent safety varies with interaction context depth. Program 2 distinguishes transient post-recovery state from general context depth. |
| `2501.Cascading` | Placeholder / Fabricated ID | *PALADIN: Empowering LLM Agents with Execution-Time Error Recovery* (arXiv:2402.14389) | Replaced with real paper. Focuses on active error-recovery retrieval; omits counterfactual post-recovery trajectory persistence $D(d)$. |
| `API-Bank` (Generic) | Missing exact ACL Anthology ID | *API-Bank: A Benchmark for Tool-Augmented LLMs* (EMNLP 2023, ACL Anthology: `2023.emnlp-main.187`) | Corrected exact citation. Used strictly as a tool capability benchmark; NOT a post-recovery persistence benchmark. |
| `ToolSafe` (Generic) | Missing exact arXiv ID | *ToolSafe: Enhancing Tool Invocation Safety of LLM-based Agents via Proactive Step-level Guardrail and Feedback* (arXiv:2401.10156) | Integrated exact paper. Program 2 distinguishes persistent post-recovery state from step-level history guardrails. |

---

## 2. Updated Scientific Boundary & Claim Adjustments

1. **NO Claiming "Multi-Turn Tool Safety is New"**: Real 2024–2026 papers (*ToolShield*, *SODA*, *MT-AgentRisk*) already establish that agent safety degrades over multi-turn interactions.
2. **NO Claiming "Hidden-State Belief Error" Without Probing**: Claim is strictly narrowed to **Behavioral Trajectory Persistence** ($D(d)$) unless hidden representations are directly extracted.
3. **NO Claiming "Tool Failure Recovery in General"**: *PALADIN* (2024) already evaluates execution-time error recovery. Program 2 specifically evaluates **counterfactual post-recovery trajectory divergence $D(d)$ AFTER the external tool is fully restored to 100% health**.
