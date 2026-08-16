# OFFICIAL SUBMISSION RECEIPT — IEEE BIGDATA 2026 MAIN TRACK

**Submission CyberChair Paper ID**: `BigD497`  
**Submission Timestamp**: 2026-08-17 (IST)  
**Submission Target**: IEEE International Conference on Big Data (IEEE BigData 2026) Main Track  
**Conference Dates**: December 14–17, 2026 (Phoenix, AZ, USA)  
**Automatic Transfer Option**: Yes $\rightarrow$ *11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)*

---

## 1. SUBMISSION METADATA SUMMARY

* **Paper ID**: `BigD497`
* **Paper Title**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`
* **Primary Author & Contact**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)
* **Author Email**: `shamthakare3000@gmail.com`
* **Author Phone**: `+91 7776807761`
* **Postal Address**: Near Datta Mandir, Rastra Seva Dal, Pune 411030, Maharashtra, India

### Selected Topics:
1. `10.e. Data-Centric AI Methods, Tools, and Systems`
2. `10.b. Benchmarks and Evaluation Frameworks`

### Keywords:
1. `Large Language Models`
2. `Mathematical Reasoning`
3. `Model Evaluation`
4. `Data-Centric AI`
5. `Reproducibility`

---

## 2. UPLOADED PDF ARTIFACT FORENSICS

* **Uploaded File Name**: `main.pdf`
* **Local Source Path**: [`submission_bigdata2026_main_v3/main.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_bigdata2026_main_v3/main.pdf)
* **Exact File Size**: `152,717` bytes (`152,717 bytes`)
* **SHA-256 Checksum**: `278d1cdce114ff327c365aebb7498ed63097a2bb5d93a03d61da19e44def062a`
* **Page Count**: 4 Pages (US Letter `612 x 792 pts`, IEEE 2-Column Format)
* **Compiler Engine**: Native TeX (`tectonic` / `xdvipdfmx`)
* **Font Embedding**: 100% Type 1 / CID TrueType Vector Fonts (**0 Type 3 Fonts**)
* **Active References**: 14 primary-source verified references (1-to-1 matching in `FINAL_REFERENCE_AUDIT_V2.csv`)

---

## 3. LOCKED EMPIRICAL SCIENTIFIC RESULT

* **Evaluated Models**: `Qwen2.5-Math-1.5B` Base (`4a83ca6e`) and Instruct (`aafeb0fc`)
* **Hardware Device**: Apple Silicon MPS (`mps:0`) in FP16 precision
* **Total Continuations**: 400 continuations across 20 GSM8K evaluation problems
* **Recovery Continuation Success**: Base $= 0.1500$, Instruct $= 0.5800$ (Diff: $+0.4300$)
* **Control Continuation Success**: Base $= 0.3800$, Instruct $= 0.9200$ (Diff: $+0.5400$)
* **Matched Recovery-Specific Contrast**: $D_{\text{recovery}} = \mathbf{-0.1100}$
* **95% Descriptive Bootstrap Interval**: $\mathbf{[-0.240, +0.030]}$ (10,000 resamples)
* **Scientific Verdict**: Under the state-matched protocol, we did not observe evidence of a recovery-specific advantage for the Instruct checkpoint over the Base checkpoint.

---

## 4. PROVENANCE & GIT SEAL

* **Append-Only Evidence SHA-256**: `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4`
* **V3 Package Manifest SHA-256**: `9f4a61823e63684c79ccd637d656b000f04996a8575de209612d0564a504ca3f`
* **Final Git Commit Hash**: `f1f1b599ac9a455a340a7ddfa982ce0c2ed4e551`
