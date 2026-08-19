# PHASE 1I STORAGE AND I/O CAPACITY PLAN

**Milestone**: Phase 1I Infrastructure Storage & Disk Audit  
**Execution Timestamp**: `2026-08-19 22:20 UTC`  
**Storage Audit Verdict**: **`PASSED — DISK CAPACITY & I/O BANDWIDTH VERIFIED`**

---

## 1. Data Volume & Disk Capacity Estimates

For the full confirmatory experiment of **131,328 rollouts**:

| Resource Category | Format / Compression | Average Record Size | Total Storage Volume | Persistent Volume Location |
| :--- | :--- | :---: | :---: | :--- |
| **Raw Output Rollouts** | JSON Lines (`.jsonl`) | ~1.5 KB / rollout | **~197 MB** | Persistent Disk (`/workspace`) |
| **Compressed Rollouts** | `gzip` JSONL (`.jsonl.gz`) | ~0.35 KB / rollout | **~46 MB** | Local Mac & GCS Backup |
| **Execution Logs & Metrics**| Plain Text (`.log`) | ~5 MB / run | **~25 MB** | Persistent Storage |
| **Model Weights Cache** | HF Safetensors (9 checkpoints) | ~14.2 GB / checkpoint | **~128 GB** | Ephemeral / Shared Disk Cache |
| **Total Disk Capacity Required** | — | — | **~135 GB** | Recommended 150 GB container disk |

---

## 2. Ephemeral vs. Persistent Disk Policy

* **Irreplaceable Artifacts**: Rollout JSONL files, seed logs, and manifests are written directly to `/workspace` and streamed asynchronously to persistent storage. They are **NEVER** stored exclusively in ephemeral `/tmp` container layers.
* **Model Checkpoints**: Downloaded on-demand into Hugging Face cache (`~/.cache/huggingface/hub`). If disk space becomes constrained, cached checkpoints are removed sequentially after rollout generation.

*Signed by Research Infrastructure & GPU Capacity Engineer*
