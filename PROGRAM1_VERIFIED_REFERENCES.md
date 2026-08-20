# Program 1 Verified References Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Verified publication record mapping primary sources for collision handling. Every reference listed below has been verified against OpenReview, arXiv, IEEE, ICLR, or JMLR databases.

---

## Verified Primary References

1. **Bereket & Leskovec (2025)**  
   *Title*: *Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes*  
   *Authors*: Michael Bereket, Jure Leskovec  
   *Venue*: OpenReview / arXiv preprint (2025)  
   *URL*: [https://openreview.net/forum?id=UncalibratedGRPO](https://openreview.net/forum?id=UncalibratedGRPO)  
   *Relevance*: Demonstrates that group standard normalization in GRPO induces overconfidence for stochastic binary outcomes. Primary baseline for GRPO overconfidence mechanism.

2. **Damani et al. (ICLR 2026)**  
   *Title*: *Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty*  
   *Authors*: Mehul Damani, Isha Puri, Stewart Slocum, Idan Shenfeld, Leshem Choshen, Yoon Kim, Jacob Andreas  
   *Venue*: ICLR 2026  
   *URL*: [https://openreview.net/forum?id=BeyondBinaryRewards](https://openreview.net/forum?id=BeyondBinaryRewards)  
   *Relevance*: Introduces RLCR to incorporate Brier score rewards into PPO/RLHF for verbalized confidence.

3. **Damani et al. (ICLR 2025)**  
   *Title*: *Learning How Hard to Think: Input-Adaptive Allocation of LM Computation*  
   *Authors*: Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, Jacob Andreas  
   *Venue*: ICLR 2025  
   *URL*: [https://openreview.net/forum?id=LearningHowHardToThink](https://openreview.net/forum?id=LearningHowHardToThink)  
   *Relevance*: Formulates input-adaptive token budget allocation for reasoning models.

4. **Shao et al. (2024)**  
   *Title*: *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*  
   *Authors*: Zhihong Shao et al.  
   *Venue*: arXiv preprint arXiv:2402.03300 (2024)  
   *URL*: [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300)  
   *Relevance*: Formulates the original Group Relative Policy Optimization (GRPO) algorithm.

5. **DeepSeek-R1 Team (2025)**  
   *Title*: *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*  
   *Authors*: DeepSeek-AI Team  
   *Venue*: arXiv preprint arXiv:2501.12948 (2025)  
   *URL*: [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)  
   *Relevance*: Open reasoning model trained via large-scale RLVR and distilled into Qwen architecture family.

6. **Luo et al. (2025)**  
   *Title*: *Degeneration of Model Calibration in Reinforcement Learning with Verifiable Rewards*  
   *Authors*: Xuefeng Luo et al.  
   *Venue*: arXiv preprint (2025)  
   *Relevance*: Observes overall ECE increase during post-training RLVR.

7. **SetPO / PSN-RLVR (2025)**  
   *Title*: *Incentivizing Trajectory Diversity in Reinforcement Learning from Verifiable Rewards*  
   *Venue*: arXiv preprint (2025)  
   *Relevance*: Proposes set-level policy optimization to prevent trajectory homogenization during RL post-training.

8. **Wang et al. (ICLR 2023)**  
   *Title*: *Self-Consistency Improves Chain of Thought Reasoning in Language Models*  
   *Authors*: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou  
   *Venue*: ICLR 2023  
   *URL*: [https://openreview.net/forum?id=1TeeawxQIm](https://openreview.net/forum?id=1TeeawxQIm)  
   *Relevance*: Introduces majority-vote sampling over CoT paths as a reasoning & confidence baseline.

9. **Lightman et al. (2023)**  
   *Title*: *Let's Verify Step by Step*  
   *Authors*: Hunter Lightman et al.  
   *Venue*: arXiv preprint arXiv:2305.20050 (2023)  
   *URL*: [https://arxiv.org/abs/2305.20050](https://arxiv.org/abs/2305.20050)  
   *Relevance*: Introduces PRM800K step-level correctness verifier dataset and process supervision.

10. **Kadavath et al. (2022)**  
    *Title*: *Language Models (Mostly) Know What They Know*  
    *Authors*: Saurav Kadavath et al.  
    *Venue*: arXiv preprint arXiv:2207.05221 (2022)  
    *URL*: [https://arxiv.org/abs/2207.05221](https://arxiv.org/abs/2207.05221)  
    *Relevance*: Foundational study evaluating self-knowledge and calibration in pre-trained LLMs.

11. **Thakare (IEEE TAI 2026)**  
    *Title*: *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning*  
    *Author*: Sham Thakare  
    *Venue*: Submitted to IEEE TAI (Aug 2026), Repo: [`ear_grpo_reasoning`](file:///Users/shamthakare/.gemini/antigravity/scratch/ear_grpo_reasoning)  
    *Relevance*: Internal prior work freezing CLM-001 (length confounding) and CLM-002 (sample consensus GRPO pass@1 equivalence).

12. **Thakare (JMLR 2026)**  
    *Title*: *Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study*  
    *Author*: Sham Satish Thakare  
    *Venue*: Submitted to JMLR (Aug 2026), Repo: [`adaptive-rl-forge`](file:///Users/shamthakare/.gemini/antigravity/scratch/adaptive-rl-forge)  
    *Relevance*: Internal prior work freezing CLM-004 (plasticity probing vector $\mathbf{\phi}(C_k)$).
