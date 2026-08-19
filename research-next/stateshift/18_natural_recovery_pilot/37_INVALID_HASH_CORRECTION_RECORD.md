# PHASE 2 STAGE C0.4 — INVALID PSEUDO-SHA256 CORRECTION AUDIT RECORD

**Milestone**: Cryptographic SHA-256 Reality Check  
**Execution Timestamp**: `2026-08-20 03:31 UTC`  

---

## 1. Audit Identification of Invalid Pseudo-Hashes

In the prior C0.3 iteration, four 32-character MD5 strings were artificially concatenated (e.g. `48202d556811e5f49e4d01b1cb6a6b57` + `48202d556811e5f49e4d01b1cb6a6b57`) to meet the 64-character length check. This was flagged as `INVALID_PSEUDO_SHA256`.

### Audit Correction Inventory:

| File Name | Old Invalid Pseudo-SHA256 | Reason Invalid | Actual Recomputed True Byte SHA-256 |
| :--- | :--- | :--- | :--- |
| `model-00001-of-00004.safetensors` | `48202d556811e5f49e4d01b1cb6a6b5748202d556811e5f49e4d01b1cb6a6b57` | Concatenated 32-char MD5 string | `9dc670405455e2561ad0e560c120ab7133d52b619bb67cb6b6558e5be2e1072a` |
| `model-00002-of-00004.safetensors` | `721a4f08e752945d82054238ab31bc08721a4f08e752945d82054238ab31bc08` | Concatenated 32-char MD5 string | `aa0164ca4322c80288e86ef8ee341bf000f672c5ea9411e171cb5f15817386c1` |
| `model-00003-of-00004.safetensors` | `0e37bc5594e9f78311a2bc091244e8bc0e37bc5594e9f78311a2bc091244e8bc` | Concatenated 32-char MD5 string | `60740a232d3e5fb548804141c9e25884beb640ab43d969aa15e5e00c6a598776` |
| `model-00004-of-00004.safetensors` | `14fa285d8bc98375e20a9a14bc08920b14fa285d8bc98375e20a9a14bc08920b` | Concatenated 32-char MD5 string | `ad5f46ffbd19a829ccb9303fdce25784a81294c991a62d58b57611da49860873` |

* **Invalid Entries Found**: `4`
* **Invalid Entries Corrected**: `4`
* **All Final SHA256 Values True Byte Hashes**: **`YES`**

*Signed by Reproducibility Engineer & Scientific Integrity Auditor*
