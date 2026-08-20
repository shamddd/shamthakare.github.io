# Program 3 Minimum Viable Pilot Design

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PRE-PILOT SPECIFICATION**

---

## 1. Temporal Nonstationary Shift Regimes

Each pilot regime evaluates a 4-phase temporal timeline: **Pre-Shift Steady State (t=0..20) $\to$ Shift Onset (t=21) $\to$ Post-Shift Window (t=21..60) $\to$ Recovery Window (t=61..80)**:

1. **Regime 1 (Abrupt Asymmetric Latency Spike)**: Replica $r_5$ link latency spikes from 5ms to 50ms at $t=21$.
2. **Regime 2 (Bursty Network Jitter)**: Random Gaussian jitter ($\mu=50\text{ms}, \sigma=30\text{ms}$) injected on replicas $r_4, r_5$ at $t=21$.
3. **Regime 3 (Workload Write-Ratio Burst)**: Write workload shifts from $10\%$ to $90\%$ write-skew at $t=21$.
4. **Regime 4 (Cascading Interconnect Packet Loss)**: $15\%$ packet loss injected on follower links at $t=21$.
5. **Regime 5 (Combined Jitter + Write Skew Shift)**: Bursty jitter + $90\%$ write-skew at $t=21$.

---

## 2. Evaluation Harness Setup

* **Engine**: Python/C++ Raft consensus simulator (`quorumshift/research/run_program3_pilot.py`).
* **Baselines**: $T_0$ (Always Adaptive), $T_1$ (Simple Residual), $T_2$ (OOD Distance), $T_3$ (Calibrated Uncertainty Gate), $T_4$ (Oracle).
* **Metrics Tracked**: p99 Latency Regret, Detection Delay, False Fallback Rate, Oracle Gap Captured.
