# Program 1 Minimum Viable Pilot (MVP) Protocol

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Execute the minimum defensible pilot experiment to determine if the self-consistency agreement decoupling phenomenon exists prior to running main evaluation sweeps.

---

## 1. Pilot Question

> *Does post-RLVR model inference (`DeepSeek-R1-Distill-Qwen-1.5B`) show a detectable increase in self-consistency agreement ($S_{\text{ans}} \ge 0.75$) on incorrect answer clusters accompanied by trajectory homogenization ($J_{\text{path}} \ge 0.75$) compared to pre-RLVR base models on a small pilot sample ($N=50$)?*

---

## 2. Pilot Setup & Configuration

* **Models**:
  - Baseline Condition (Base/SFT): `Qwen/Qwen2.5-Math-7B-Instruct`
  - Post-RLVR Condition: `DeepSeek-R1-Distill-Qwen-1.5B`
* **Dataset**: GSM8K held-out pilot subset ($N = 50$ prompts, indices 500–549).
* **Sampling Parameters**: $K = 8$ rollouts per prompt, temperature $T = 0.7$, max new tokens = 256.
* **Total Generations**: $50 \text{ prompts} \times 8 \text{ rollouts} \times 2 \text{ models} = 800 \text{ completions}$.
* **Hardware**: Local CPU / Apple Silicon PyTorch MPS or CPU execution (\$0.00 RunPod GPU spend).

---

## 3. Evaluated Pilot Endpoints

1. **High-Agreement Miscalibration Rate**: Percentage of incorrect answer clusters where $S_{\text{ans}} \ge 0.75$.
2. **Pairwise Path Similarity ($J_{\text{path}}$)**: Mean Jaccard 3-gram similarity across sampled completions within the same prompt.
3. **Pilot AURC & Brier Score**: Initial baseline calculation of selective classification risk.

---

## 4. Decision Threshold for Main Study (Pilot Gate)

* **GO Signal**: If the post-RLVR model shows a high-agreement miscalibration rate $\ge 15\%$ (compared to $<5\%$ for the base model) AND $J_{\text{path}}$ on wrong answers increases by $\ge 0.20$ ($p < 0.05$).
* **STOP / PIVOT Signal**: If high-agreement miscalibration rate is $<5\%$ or statistically indistinguishable between base and post-RLVR models ($p > 0.05$).
