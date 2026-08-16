# COVER LETTER

**To**: Program Committee, IEEE BigData 2026  
**Special Session**: Machine Learning on Big Data  
**Submission Title**: A State-Matched Framework for Evaluating Recovery Behavior in Language-Model Reasoning  

Dear Program Chairs and Reviewers,

I am pleased to submit our manuscript, *"A State-Matched Framework for Evaluating Recovery Behavior in Language-Model Reasoning,"* for consideration in IEEE BigData 2026 (Special Session on Machine Learning on Big Data).

### Summary of Work
Evaluating whether post-training procedures enable language models to recover from intermediate reasoning errors is confounded by differences in trajectory depth, solution length, and problem difficulty. We introduce `recovery_eval`, a prospective state-matched evaluation framework that pairs verifier-defined error states with reference control states using frozen structural covariates. Our framework incorporates append-only exposure ledgers, primitive neural-rollout provenance, and independently verifiable reconstruction. 

In a study across 400 genuine continuations from `Qwen2.5-Math-1.5B` (Base and Instruct) on 20 fresh GSM8K test items, we observe that while the Instruct checkpoint improves overall continuation success over Base in both recovery ($+0.4300$) and control ($+0.5400$) states, the net matched contrast is $D_{\text{recovery}} = -0.1100$ ($95\%$ descriptive bootstrap interval $[-0.240, +0.030]$). This demonstrates that aggregate post-training accuracy gains do not automatically translate into a detectable recovery-specific advantage.

### Single-Blind Compliance & Author Declaration
In accordance with IEEE BigData single-blind CFP rules, the author metadata is fully visible:
* **Author**: Sham Satish Thakare
* **Affiliation**: Independent Researcher, Pune, Maharashtra, India
* **Email**: `shamthakare3000@gmail.com`

No artificial institutional or supervisor affiliations have been claimed.

Thank you for your time and consideration.

Sincerely,  
**Sham Satish Thakare**  
Independent Researcher  
Pune, Maharashtra, India  
`shamthakare3000@gmail.com`  
