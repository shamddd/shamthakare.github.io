# PHASE 7 TRAINING LINEAGE SELECTION

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare  

---

## 1. Selected Post-Training Lineage

| Parameter | Base Model ($t=0$) | Post-Trained Model ($t=256$) |
| :--- | :--- | :--- |
| **Model Repository ID** | `Qwen/Qwen2.5-7B` | `UWNSL/Qwen2.5-7B-deepscaler` |
| **Hugging Face Revision Hash** | `e1d4b...` | `9a83f...` |
| **Architecture** | Qwen2ForCausalLM (7.61B parameters) | Qwen2ForCausalLM (7.61B parameters) |
| **Post-Training Method** | Base Pre-trained | Group Relative Policy Optimization (GRPO) |
| **Reward Function** | N/A | Sympy Boxed Answer Outcome Verifier |
| **Training Data** | Pre-training Corpus | DeepScaler-4K Math Reasoning Dataset |

---

## 2. Scientific Justification

Evaluating base ($t=0$) versus step-256 ($t=256$) on the same controlled DeepScaler RL lineage guarantees strict within-lineage causal control.

*Signed by Senior Research Scientist & ML Systems Engineer*
