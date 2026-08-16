# MANDATORY COLLISION AUDIT: SCALELOGIC & LONG-HORIZON RL

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. SCALELOGIC AUDIT (ARXIV:2605.06638)
* **Title**: *Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key*
* **Core Focus**: Evaluates power-law scaling of RL **training compute** $C_{\text{train}}$ with reasoning depth.
* **Distinction from Our Project**: ScaleLogic asks how much training compute RLVR requires to learn deep reasoning. Our project asks **how up-front training cost versus repeated inference cost changes the deployment-optimal intervention over future query horizon $Q$**.

## 2. OTHER LONG-HORIZON RL PAPERS
* **h1: Bootstrapping LLMs to Reason over Longer Horizons** (2026): Focuses on curriculum bootstrapping.
* **Reasoning Cache** (2026): Focuses on short-horizon RL memory caching.

**COLLISION VERDICT**: **`DISTINCT`**. Zero papers evaluate the query-amortized deployment horizon frontier $Q^*(a, b)$ under matched total compute.
