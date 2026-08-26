# EXACT AIJ SUBMISSION RECONSTRUCTION

**Manuscript Title**: *StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training*  
**Submitted Journal**: *Artificial Intelligence* (Elsevier / AIJ)  
**Manuscript ID**: `ARTINT-D-26-01491`  
**Corresponding Git SHA**: `42a966f169e4e5baf63a1a87c74d4abc297d5881`  
**Article Type**: Regular Research Article / Full-Length Article  
**Author Metadata**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India; `shamthakare3000@gmail.com`)  

---

## 1. Abstract & Highlights

### Abstract
> Standard evaluations of reinforcement-learning post-training in large language models emphasize aggregate benchmark accuracy, potentially obscuring changes conditional on local reasoning state. We introduce StateShift, a framework for measuring target-transition recovery under matched reasoning states. In a controlled study (N=454, 29,056 rollouts), we observe an 11.76-percentage-point state-by-checkpoint interaction between the base and step-256 checkpoints ($\Gamma_{256}=0.1176$, 95% problem-blocked bootstrap CI $[0.0955, 0.1400]$). Across nine empirically evaluated checkpoints, the interaction was consistent with a non-decreasing trajectory under prespecified order-restricted analysis despite local variation in unconstrained estimates, and was already detectable at the earliest available post-training checkpoint, $t=32$ ($\Gamma_{32}=0.0333$, multiplicity-adjusted 95% CI $[0.0011, 0.0655]$). In a separate analysis of 3,200 unperturbed rollouts, 18.19% contained a verifier-confirmed natural reasoning error; among 582 qualifying error episodes, 180 subsequently satisfied the prespecified autonomous recovery criterion (30.93%, 95% problem-blocked bootstrap CI $[27.19\%, 34.82\%]$). These results show that state-conditioned evaluation exposes behavioral structure not captured by aggregate correctness alone.

### Highlights
* Controlled framework measuring state-conditioned reasoning recovery in post-trained LLMs.
* +11.76 percentage-point state-by-checkpoint interaction contrast at step 256 ($\Gamma_{256}=+0.1176$).
* Nine-checkpoint empirical trajectory evaluated via prespecified order-restricted PAVA analysis.
* Interaction statistically detectable by earliest available post-training checkpoint ($t=32$).
* 30.93% conditional natural post-error recovery rate across 582 unperturbed error rollouts.

---

## 2. Original Scientific Question & Primary Hypothesis

* **Original Scientific Question**: *"Does reinforcement learning post-training induce a state-selective target-transition recovery capability under intermediate invalid reasoning states?"*
* **Primary Hypothesis**: *"Reinforcement learning post-training yields a state-by-checkpoint interaction ($\Gamma_t$) in target-transition success that evolves along a non-decreasing trajectory across post-training."*

---

## 3. Experimental Design

* **Model Family**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_X` (Base model: `Qwen/Qwen2.5-7B`).
* **Model Size**: 7.61 billion parameters.
* **RL Algorithm**: Group Relative Policy Optimization (GRPO) with outcome-based verifier reward.
* **Evaluated Checkpoints**: $t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$.
* **Primary Dataset**: `MATH-500` ($N=454$ primary problems; $N_{\text{Strict}}=388$ strict decontamination subset).
* **Rollout Allocation**:
  * Study A Endpoint ($t=0, 256$): $K=16$ rollouts/cell per problem ($29,056$ total rollouts).
  * Study A Trajectory ($t=32, 96, 160, 224$): $K=2$ rollouts/cell per problem ($7,264$ new rollouts).
  * Study B Natural Recovery ($t=256$): $N=200, K=16$ unperturbed rollouts ($3,200$ total rollouts).
* **Perturbation Scheme**:
  * **Recovery Condition ($R$)**: Problem prompt + injected intermediate reasoning prefix containing a verifier-confirmed invalid step.
  * **Control Condition ($C$)**: Problem prompt + length/context-matched valid intermediate reasoning prefix.
* **Decoding Parameters**: Temperature $= 0.6$, Top-$p = 0.95$, Max New Tokens $= 512$.

---

## 4. Primary & Secondary Endpoints

### Primary Endpoint ($\Gamma_t$)
Defined as the difference-in-differences interaction contrast:

$$\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$$

where:
* $\mu_{R,t} = 0.7039$ (Recovery success at $t=256$)
* $\mu_{C,t} = 0.5921$ (Control success at $t=256$)
* $\mu_{R,0} = 0.3834$ (Recovery success at base model $t=0$)
* $\mu_{C,0} = 0.3892$ (Control success at base model $t=0$)

$$\Gamma_{256} = (0.7039 - 0.3834) - (0.5921 - 0.3892) = 0.3205 - 0.2029 = \mathbf{+0.1176}$$

### Secondary Endpoints
* **Strict Subgroup**: $\Gamma_{256,\text{Strict}} = \mathbf{+0.1160}$ ($95\%$ CI $[+0.0913, +0.1408]$).
* **9-Checkpoint Trajectory Vector**: $\mathbf{\Gamma} = [0.0000, +0.0333, +0.0337, +0.0774, +0.0748, +0.0598, +0.0976, +0.0950, +0.1176]$.
* **Earliest Detectable Interaction**: Step 32 ($\Gamma_{32} = \mathbf{+0.0333}$, multiplicity-adjusted 95% CI $[+0.0011, +0.0655]$).
* **Natural Error Incidence ($\text{NEI}$)**: $18.19\%$ ($582/3200$ unperturbed rollouts).
* **Conditional Natural Post-Error Recovery Rate ($\text{NRR}$)**: $30.93\%$ ($180/582$ error rollouts, 95% CI $[27.19\%, 34.82\%]$).

---

## 5. Classification of Claimed Contributions

| Claimed Contribution | Submitted Manuscript Statement | Contribution Type | Classification & Mismatch Audit |
| :--- | :--- | :---: | :--- |
| **StateShift Framework** | "Introduces a controlled counterfactual prefix framework for state-conditioned reasoning evaluation." | **`METHODOLOGICAL`** | **VALID**: Clear operational protocol for counterfactual prefix injection. |
| **Endpoint Interaction** | "Demonstrates an 11.76 percentage-point interaction contrast ($\Gamma_{256}=+0.1176$)." | **`EMPIRICAL`** | **VALID**: Directly measured difference-in-differences contrast on Study A. |
| **Trajectory Evolution** | "Reveals a non-decreasing trajectory across post-training checkpoints consistent under PAVA analysis." | **`DESCRIPTIVE / EMPIRICAL`** | **MISMATCH**: Unconstrained point estimates contain dips ($96\to 128$); claiming global monotonicity exceeds unconstrained data. |
| **Earliest Emergence** | "Interaction is detectable by the earliest available checkpoint ($t=32$)." | **`EMPIRICAL`** | **MISMATCH**: Sub-32 checkpoints do not exist; calling $t=32$ "emergence" conflates availability with step-level origin. |
| **Autonomous Self-Correction** | "RL post-training yields intrinsic self-correction during natural decoding." | **`CAUSAL / MECHANISTIC`** | **CRITICAL MISMATCH**: $\text{NRR}$ is observational and subject to survivorship bias; framing behavioral recovery as internal "self-correction" exceeds evidence. |

*Signed by Principal ML Research Scientist & Scientific Integrity Auditor*
