# COVER LETTER FOR SUBMISSION TO ARTIFICIAL INTELLIGENCE (AIJ)

**Date**: August 20, 2026  
**To**: Editors-in-Chief and Associate Editors, *Artificial Intelligence* (Elsevier)  
**Article Type**: Full-Length Research Article  
**Title**: *StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training*  

Dear Editors,

We submit our manuscript entitled **"StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training"** for consideration as a Full-Length Research Article in *Artificial Intelligence*.

### Core Problem & Motivation
Standard evaluations of reinforcement learning (RL) post-training in large language models rely almost exclusively on aggregate benchmark accuracy. While accuracy metrics track global performance gains, they provide little visibility into how post-training alters reasoning behavior conditional on local intermediate state. Does RL training improve reasoning capability uniformly, or does it specifically enhance the model's capacity to recover from invalid intermediate states?

### Key Contributions
To address this fundamental question, we introduce **StateShift**, a controlled framework that measures target-transition recovery conditional on intermediate reasoning state. Our investigation makes three main empirical contributions:

1. **Controlled State-Conditioned Evaluation**: In a controlled study ($N=454, 29,056$ rollouts), we observe an 11.76-percentage-point state-by-checkpoint interaction between the base and step-256 checkpoints ($\Gamma_{256} = +0.1176, p < 0.0001, 95\%$ problem-blocked bootstrap CI $[+0.0955, +0.1400]$), demonstrating that post-training gains are state-selective rather than uniform.
2. **Complete Nine-Checkpoint Trajectory**: Evaluating nine empirically sampled checkpoints ($t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$) shows that the interaction is consistent with a non-decreasing trajectory under prespecified order-restricted analysis despite local point-estimate variation, and is statistically detectable by the earliest available checkpoint ($t=32, \Gamma_{32}=+0.0333$, multiplicity-adjusted 95% CI $[+0.0011, +0.0655]$).
3. **Unprompted Natural Post-Error Recovery**: Evaluating $3,200$ unperturbed rollouts ($N=200$) reveals an $18.19\%$ Natural Error Incidence and a $30.93\%$ Conditional Natural Post-Error Recovery Rate (95% CI $[27.19\%, 34.82\%]$) after verifier-confirmed natural reasoning errors.

### Journal Scope & Editorial Declarations
This work provides broad methodological value for the general AI community by demonstrating how state-conditioned evaluation exposes behavioral structure obscured by aggregate accuracy metrics alone.

We confirm that:
- This manuscript represents original work and is not under consideration for publication elsewhere.
- All authors have approved the submission.
- No financial or personal conflicts of interest exist.

Thank you for your time and consideration.

Sincerely,

**Corresponding Author**  
`REQUIRED_FROM_AUTHOR@institution.edu`  
Department Name, Institution Name  
Full Postal Address Required  
