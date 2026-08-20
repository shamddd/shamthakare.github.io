# STAGE 9: NATURAL RECOVERY-STATE REPLICATION FORMULATION

**Date**: August 16, 2026  
**Target Venue Strategy**: JMLR (Main Submission) / TMLR (Fallback if bounded)  

---

## 1. CENTRAL EXTERNAL VALIDITY QUESTION

$$\boxed{\Delta_{\text{late}}^{\text{natural}} = \mathbb{E}_{S_R}[V_{\text{FULL}} - V_{\text{PREFIX}}] - \mathbb{E}_{S_C}[V_{\text{FULL}} - V_{\text{PREFIX}}] > 0}$$

We test whether the recovery-specific late-state advantage for Full-RLVR over PrefixRL replicates on **naturally written, verifiably solvable reasoning problems** containing objectively identifiable intermediate error/recovery states ($S_R$).

> **CRITICAL BOUNDARY**: This is **NOT** a simple benchmark accuracy test (e.g., GSM8K Pass@1). It strictly evaluates state-matched value differences given externally fixed intermediate recovery states.
