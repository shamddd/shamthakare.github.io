# KILL EXPERIMENT V2: IID VS OOD COMPARISON REPORT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. REGIME COMPARISON SUMMARY
* **IID Regime**: Base sampling efficiency is high (p=0.18). Best-of-N (A1) dominates low and intermediate query horizons (Q < 1250).
* **OOD-LENGTH Regime**: Base sampling efficiency collapses (p=0.02). Best-of-N search cost explodes, causing Full RLVR (A3) to amortize rapidly at Q* = 79 queries.
* **OOD-RECOMBINATION Regime**: Base sampling efficiency is moderate (p=0.08). LoRA-RLVR (A2) achieves optimal trade-off at Q* = 210 queries.
