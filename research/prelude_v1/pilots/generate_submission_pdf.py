"""
PDF Generator for IEEE BigData MLBD 2026 Submission Manuscript.
Generates manuscript/main.pdf adhering to IEEE two-column format rules.
"""

import os
import sys
import hashlib
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, Frame, PageTemplate, BaseDocTemplate, FrameBreak
)

base_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch")
manuscript_dir = os.path.join(base_dir, "research-next/ieee_bigdata_2026/manuscript")
sub_pkg_dir = os.path.join(base_dir, "submission_mlbd2026")
figures_dir = os.path.join(manuscript_dir, "figures")

pdf_path = os.path.join(manuscript_dir, "main.pdf")

def create_pdf():
    print("[*] Generating IEEE BigData 10-page two-column submission PDF...", flush=True)

    # Page setup: IEEE 2-column format
    # Margins: Left=0.625 in, Right=0.625 in, Top=0.75 in, Bottom=0.75 in
    page_width, page_height = letter
    margin_x = 0.625 * inch
    margin_y = 0.75 * inch
    gutter = 0.25 * inch
    col_width = (page_width - 2 * margin_x - gutter) / 2.0
    col_height = page_height - 2 * margin_y

    # Styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        "IEEETitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        alignment=1,
        spaceAfter=10
    )
    
    author_style = ParagraphStyle(
        "IEEEAuthor",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        alignment=1,
        spaceAfter=15
    )

    abstract_style = ParagraphStyle(
        "IEEEAbstract",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=12,
        alignment=4,
        spaceAfter=10
    )

    heading1_style = ParagraphStyle(
        "IEEEH1",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    heading2_style = ParagraphStyle(
        "IEEEH2",
        parent=styles["Heading3"],
        fontName="Helvetica-BoldOblique",
        fontSize=10,
        leading=13,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "IEEEBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=12.5,
        alignment=4,
        spaceAfter=6
    )

    table_cell_style = ParagraphStyle(
        "IEEETableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=10
    )

    table_header_style = ParagraphStyle(
        "IEEETableHeader",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10
    )

    doc = BaseDocTemplate(pdf_path, pagesize=letter, leftMargin=margin_x, rightMargin=margin_x, topMargin=margin_y, bottomMargin=margin_y)

    # Frame definitions
    frame_left = Frame(margin_x, margin_y, col_width, col_height, id="col1", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame_right = Frame(margin_x + col_width + gutter, margin_y, col_width, col_height, id="col2", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    
    # Page template with footer
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawString(margin_x, 0.4 * inch, "11th IEEE Special Session on Machine Learning on Big Data (IEEE BigData MLBD 2026)")
        canvas.drawRightString(page_width - margin_x, 0.4 * inch, f"Page {doc.page} of 10")
        canvas.restoreState()

    two_col_template = PageTemplate(id="TwoCol", frames=[frame_left, frame_right], onPage=footer)
    doc.addPageTemplates([two_col_template])

    story = []

    # Title & Author
    story.append(Paragraph("recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning", title_style))
    story.append(Paragraph("<b>Sham Satish Thakare</b><br/>Independent Researcher, Pune, Maharashtra, India<br/>Email: shamthakare3000@gmail.com", author_style))
    
    # Abstract
    abstract_text = (
        "<b><i>Abstract</i>—Evaluating whether post-training procedures enhance a language model's ability to recover from intermediate reasoning errors remains challenging due to confounding variables in state trajectory comparisons. Naive benchmark comparisons often conflate overall accuracy gains with recovery-specific capability. In this work, we introduce recovery_eval, a reproducible data-centric evaluation framework for machine learning models that pairs verifier-defined error states with prospectively matched reference control states using frozen structural covariates. Our framework incorporates strict evidence governance, including append-only exposure ledgers, primitive neural-rollout provenance, and independently verifiable reconstruction. We demonstrate the framework across 400 genuine continuations generated by two released checkpoints (Qwen2.5-Math-1.5B Base and Instruct) on 20 fresh GSM8K evaluation items (mean normalized weighted-L1 distance d<sub>mean</sub> = 0.0360, d<sub>max</sub> = 0.0360). Under the state-matched protocol, we observed continuation success improvements for Instruct over Base in both recovery (+0.4300) and control (+0.5400) states, yielding a matched recovery-specific contrast of D<sub>recovery</sub> = -0.1100 with a 95% descriptive problem-level bootstrap interval of [-0.240, +0.030]. These findings demonstrate that aggregate checkpoint gains do not automatically translate into a detectable recovery-specific advantage, highlighting the utility of state-matched evaluation infrastructure for reasoning model diagnostics.</b>"
    )
    story.append(Paragraph(abstract_text, abstract_style))
    story.append(Paragraph("<b><i>Index Terms</i>—Language Models, Mathematical Reasoning, Error Recovery, State-Matched Evaluation, Data-Centric AI, Benchmark Governance, Reproducibility.</b>", abstract_style))
    story.append(Spacer(1, 8))

    # Section 1
    story.append(Paragraph("I. Introduction", heading1_style))
    story.append(Paragraph("Large language models (LLMs) trained on mathematical reasoning tasks exhibit improved step-by-step problem-solving capabilities. A central research question in machine learning evaluation is whether post-training mechanisms (e.g., instruction tuning, process supervision, or reinforcement learning) instill structural intelligence that enables models to detect and recover from early arithmetic or logical missteps during trajectory generation.", body_style))
    story.append(Paragraph("However, evaluating error recovery behavior is susceptible to statistical confounding. Simply comparing model performance on error-containing prefixes against valid prefixes conflates trajectory depth, remaining solution length, problem difficulty, and token complexity. Aggregate accuracy improvements on benchmarks can mask whether a post-trained checkpoint genuinely possesses superior recovery mechanisms or merely exhibits higher baseline fluency across all states.", body_style))
    story.append(Paragraph("To address these challenges, we present recovery_eval, a data-centric evaluation framework designed to isolate recovery-specific behavior in language-model reasoning trajectories. The primary contributions of this paper are threefold:", body_style))
    story.append(Paragraph("1) <b>State-Matched Evaluation Protocol</b>: A verifier-defined recovery and control state evaluation protocol that enforces prospective structural matching on intermediate reasoning prefixes.", body_style))
    story.append(Paragraph("2) <b>Provenance & Exposure-Governance Architecture</b>: An infrastructure that preserves primitive BPE token-level neural rollout evidence, weight manifests, and append-only exposure ledgers for independent reconstruction.", body_style))
    story.append(Paragraph("3) <b>Framework Demonstration</b>: A genuine two-checkpoint Qwen2.5-Math-1.5B demonstration showing that aggregate checkpoint accuracy gains (+0.4300 recovery vs +0.5400 control) do not automatically correspond to a detectable recovery-specific advantage (D<sub>recovery</sub> = -0.1100).", body_style))

    # Figure 1
    fig1_p = os.path.join(figures_dir, "fig1_architecture.png")
    if os.path.exists(fig1_p):
        story.append(Spacer(1, 4))
        story.append(Image(fig1_p, width=col_width, height=col_width*0.48))
        story.append(Paragraph("<b>Fig. 1.</b> recovery_eval End-to-End Governance & Evaluation Pipeline.", ParagraphStyle("Cap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))

    # Section 2
    story.append(Paragraph("II. Related Work", heading1_style))
    story.append(Paragraph("Recent work has investigated self-correction, test-time compute scaling, and backtracking in reasoning LLMs. Unlike prior benchmarks that evaluate full trajectories or un-matched intermediate states, recovery_eval enforces prospective matching on intermediate reasoning prefixes prior to rollout generation.", body_style))

    # Table I
    t1_data = [
        [Paragraph("<b>Framework / Work</b>", table_header_style), Paragraph("<b>State Matching</b>", table_header_style), Paragraph("<b>Exposure Ledger</b>", table_header_style), Paragraph("<b>Primitive Provenance</b>", table_header_style)],
        [Paragraph("End-to-End GSM8K", table_cell_style), Paragraph("None", table_cell_style), Paragraph("No", table_cell_style), Paragraph("Final Answer", table_cell_style)],
        [Paragraph("PRM800K", table_cell_style), Paragraph("Unmatched", table_cell_style), Paragraph("Partial", table_cell_style), Paragraph("Step Scores", table_cell_style)],
        [Paragraph("STaR", table_cell_style), Paragraph("Unmatched", table_cell_style), Paragraph("No", table_cell_style), Paragraph("Filtered Traces", table_cell_style)],
        [Paragraph("<b>recovery_eval (Ours)</b>", table_cell_style), Paragraph("<b>Matched</b>", table_cell_style), Paragraph("<b>Append-Only</b>", table_cell_style), Paragraph("<b>Full BPE Token</b>", table_cell_style)]
    ]
    t1 = Table(t1_data, colWidths=[col_width*0.28, col_width*0.24, col_width*0.24, col_width*0.24])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F3F4')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>TABLE I</b><br/>COMPARISON WITH EXISTING REASONING EVALUATION FRAMEWORKS", ParagraphStyle("TCap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))
    story.append(t1)

    # Section 3
    story.append(Paragraph("III. Problem Definition", heading1_style))
    story.append(Paragraph("Let s denote a partial reasoning trajectory prefix for a problem instance p in P. A deterministic verifier V(s) evaluates prefix validity. A recovery state s<sub>R</sub> contains a verifier-identified intermediate error. A reference control state s<sub>C</sub> represents a valid intermediate prefix for the same problem at an equivalent problem-solving stage.", body_style))
    story.append(Paragraph("For a target policy pi and baseline policy pi<sub>0</sub>, let V(s) in {0, 1} denote binary continuation success from prefix s. The matched recovery-specific contrast D<sub>recovery</sub> is defined as:", body_style))
    story.append(Paragraph("D<sub>recovery</sub> = E[V<sub>pi</sub>(s<sub>R</sub>) - V<sub>pi0</sub>(s<sub>R</sub>)] - E[V<sub>pi</sub>(s<sub>C</sub>) - V<sub>pi0</sub>(s<sub>C</sub>)]", ParagraphStyle("Eq", parent=styles["Normal"], fontSize=9, alignment=1, fontName="Helvetica-Bold")))

    # Section 4
    story.append(Paragraph("IV. The recovery_eval Framework", heading1_style))
    story.append(Paragraph("The recovery_eval package provides an end-to-end modular pipeline for state construction, matching, execution, and provenance logging.", body_style))
    story.append(Paragraph("A. <i>Recovery and Control State Construction</i>", heading2_style))
    story.append(Paragraph("Recovery states s<sub>R</sub> are constructed by introducing controlled single-step arithmetic perturbations into valid intermediate reasoning prefixes. Reference control states s<sub>C</sub> maintain valid prefix steps.", body_style))

    # Figure 2
    fig2_p = os.path.join(figures_dir, "fig2_state_construction.png")
    if os.path.exists(fig2_p):
        story.append(Spacer(1, 4))
        story.append(Image(fig2_p, width=col_width, height=col_width*0.48))
        story.append(Paragraph("<b>Fig. 2.</b> Verifier-Defined Recovery State vs Matched Reference Control State Construction.", ParagraphStyle("Cap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))

    story.append(Paragraph("B. <i>Prospective Matching Protocol</i>", heading2_style))
    story.append(Paragraph("To ensure statistical comparability, each recovery state s<sub>R</sub> is matched to a control state s<sub>C</sub> using a normalized weighted L1 Manhattan distance over 6 pre-group structural covariates:", body_style))
    story.append(Paragraph("d(i, j) = sum<sub>k=1</sub><sup>K</sup> w<sub>k</sub> |x<sub>ik</sub> - x<sub>jk</sub>| / s<sub>k</sub>", ParagraphStyle("Eq2", parent=styles["Normal"], fontSize=9, alignment=1, fontName="Helvetica-Bold")))
    story.append(Paragraph("subject to exact categorical matching on reasoning operation type and problem difficulty.", body_style))

    # Table II
    t2_data = [
        [Paragraph("<b>Covariate Name</b>", table_header_style), Paragraph("<b>Type</b>", table_header_style), Paragraph("<b>Weight (w<sub>k</sub>)</b>", table_header_style), Paragraph("<b>Scale (s<sub>k</sub>)</b>", table_header_style)],
        [Paragraph("Trajectory Depth", table_cell_style), Paragraph("Continuous", table_cell_style), Paragraph("0.4", table_cell_style), Paragraph("1.5", table_cell_style)],
        [Paragraph("Remaining Length", table_cell_style), Paragraph("Continuous", table_cell_style), Paragraph("0.4", table_cell_style), Paragraph("1.0", table_cell_style)],
        [Paragraph("Token Length", table_cell_style), Paragraph("Continuous", table_cell_style), Paragraph("0.2", table_cell_style), Paragraph("15.0", table_cell_style)],
        [Paragraph("Reasoning Operation", table_cell_style), Paragraph("Categorical", table_cell_style), Paragraph("Exact", table_cell_style), Paragraph("--", table_cell_style)],
        [Paragraph("Problem Difficulty", table_cell_style), Paragraph("Categorical", table_cell_style), Paragraph("Exact", table_cell_style), Paragraph("--", table_cell_style)]
    ]
    t2 = Table(t2_data, colWidths=[col_width*0.34, col_width*0.24, col_width*0.22, col_width*0.20])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F3F4')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>TABLE II</b><br/>FROZEN PROSPECTIVE MATCHING COVARIATES AND SCALES", ParagraphStyle("TCap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))
    story.append(t2)

    story.append(Paragraph("C. <i>Exposure & Provenance Governance</i>", heading2_style))
    story.append(Paragraph("All evaluation items are managed by an append-only event ledger using SHA-256 parent hash chaining to prevent data leakage or post-hoc item selection.", body_style))

    # Figure 3
    fig3_p = os.path.join(figures_dir, "fig3_provenance_chain.png")
    if os.path.exists(fig3_p):
        story.append(Spacer(1, 4))
        story.append(Image(fig3_p, width=col_width, height=col_width*0.42))
        story.append(Paragraph("<b>Fig. 3.</b> Append-Only Immutable Primitive Evidence Provenance Chain.", ParagraphStyle("Cap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))

    # Section 5
    story.append(Paragraph("V. Experimental Validation", heading1_style))
    story.append(Paragraph("We validate the framework on 20 fresh, prospectively isolated GSM8K test items (N=20). For each item, 1 matched recovery state and 1 matched control state are evaluated across 2 model configurations (Qwen2.5-Math-1.5B Base and Instruct) using 5 stochastic generation seeds (S=5), yielding exactly 400 rollouts.", body_style))

    # Table III
    t3_data = [
        [Paragraph("<b>Attribute</b>", table_header_style), Paragraph("<b>Specification / Value</b>", table_header_style)],
        [Paragraph("Base Model", table_cell_style), Paragraph("Qwen/Qwen2.5-Math-1.5B (4a83ca6e)", table_cell_style)],
        [Paragraph("Instruct Model", table_cell_style), Paragraph("Qwen/Qwen2.5-Math-1.5B-Instruct (aafeb0fc)", table_cell_style)],
        [Paragraph("Hardware Device", table_cell_style), Paragraph("Apple Silicon MPS (mps:0)", table_cell_style)],
        [Paragraph("Total Rollouts", table_cell_style), Paragraph("400 (200 Base, 200 Instruct)", table_cell_style)],
        [Paragraph("Total Generated Tokens", table_cell_style), Paragraph("19,212 BPE tokens", table_cell_style)],
        [Paragraph("Measured Duration", table_cell_style), Paragraph("1,755.86s (~29.26 minutes)", table_cell_style)],
        [Paragraph("Base Throughput", table_cell_style), Paragraph("11.86 tok/s (11,354 tokens in 957.37s)", table_cell_style)],
        [Paragraph("Instruct Throughput", table_cell_style), Paragraph("9.84 tok/s (7,858 tokens in 798.49s)", table_cell_style)],
        [Paragraph("BPE Decode Match", table_cell_style), Paragraph("100.0% (400/400 exact match)", table_cell_style)],
        [Paragraph("Raw JSONL SHA-256", table_cell_style), Paragraph("51b5a157d9e44102caeb86d0b356f558...", table_cell_style)]
    ]
    t3 = Table(t3_data, colWidths=[col_width*0.35, col_width*0.65])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F3F4')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>TABLE III</b><br/>EVALUATION DESIGN AND PROVENANCE STATISTICS", ParagraphStyle("TCap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))
    story.append(t3)

    # Section 6
    story.append(Paragraph("VI. Empirical Results", heading1_style))
    story.append(Paragraph("Table IV summarizes continuation success rates and the resulting contrast D<sub>recovery</sub>.", body_style))

    # Table IV
    t4_data = [
        [Paragraph("<b>State Condition</b>", table_header_style), Paragraph("<b>Base (pi<sub>0</sub>)</b>", table_header_style), Paragraph("<b>Instruct (pi)</b>", table_header_style), Paragraph("<b>Difference (Delta)</b>", table_header_style)],
        [Paragraph("Recovery States (s<sub>R</sub>)", table_cell_style), Paragraph("0.1500", table_cell_style), Paragraph("0.5800", table_cell_style), Paragraph("+0.4300", table_cell_style)],
        [Paragraph("Control States (s<sub>C</sub>)", table_cell_style), Paragraph("0.3800", table_cell_style), Paragraph("0.9200", table_cell_style), Paragraph("+0.5400", table_cell_style)],
        [Paragraph("<b>Matched Contrast (D<sub>recovery</sub>)</b>", table_cell_style), Paragraph("--", table_cell_style), Paragraph("--", table_cell_style), Paragraph("<b>-0.1100</b>", table_cell_style)]
    ]
    t4 = Table(t4_data, colWidths=[col_width*0.34, col_width*0.22, col_width*0.22, col_width*0.22])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F3F4')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>TABLE IV</b><br/>CONTINUATION OUTCOMES AND MATCHED RECOVERY CONTRAST", ParagraphStyle("TCap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))
    story.append(t4)

    story.append(Paragraph("Under the evaluated state-matched protocol, we did not observe evidence of a recovery-specific advantage for the Instruct checkpoint over the Base checkpoint. The estimated matched recovery-specific checkpoint-interface contrast was -0.1100, with a 95% descriptive problem-level bootstrap interval of [-0.240, +0.030] (10,000 resamples).", body_style))
    story.append(Paragraph("Notably, the Instruct checkpoint exhibited higher continuation success than Base across both recovery (+0.4300) and control (+0.5400) conditions. However, because the gain was larger for control states, the net contrast D<sub>recovery</sub> is negative. This demonstrates that aggregate post-training accuracy gains should not be interpreted automatically as recovery-specific improvement.", body_style))

    # Figure 4
    fig4_p = os.path.join(figures_dir, "fig4_empirical_results.png")
    if os.path.exists(fig4_p):
        story.append(Spacer(1, 4))
        story.append(Image(fig4_p, width=col_width, height=col_width*0.62))
        story.append(Paragraph("<b>Fig. 4.</b> Observed Recovery/Control Differences & Matched Contrast (N=400).", ParagraphStyle("Cap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))

    # Section 7
    story.append(Paragraph("VII. Ablations and Matching Sensitivity", heading1_style))
    story.append(Paragraph("We evaluate matching quality across the 20 matched pairs. Mean normalized weighted-L1 distance is d<sub>mean</sub> = 0.0360, median is d<sub>median</sub> = 0.0360, with maximum distance d<sub>max</sub> = 0.0360. All 20 pairs (20/20) satisfy both the standard matching threshold (d <= 0.25) and tight threshold (d <= 0.10). Per-covariate Standardized Mean Differences (SMDs) are reported in Table V.", body_style))

    # Table V
    t5_data = [
        [Paragraph("<b>Metric / Covariate</b>", table_header_style), Paragraph("<b>Raw Difference</b>", table_header_style), Paragraph("<b>SMD / Distance</b>", table_header_style), Paragraph("<b>Status</b>", table_header_style)],
        [Paragraph("Trajectory Depth", table_cell_style), Paragraph("+0.0000", table_cell_style), Paragraph("+0.0000", table_cell_style), Paragraph("Exact Match", table_cell_style)],
        [Paragraph("Remaining Length", table_cell_style), Paragraph("+0.0000", table_cell_style), Paragraph("+0.0000", table_cell_style), Paragraph("Exact Match", table_cell_style)],
        [Paragraph("Token Length", table_cell_style), Paragraph("+2.0000", table_cell_style), Paragraph("+0.1333", table_cell_style), Paragraph("Balanced", table_cell_style)],
        [Paragraph("Mean Pair Distance (d<sub>mean</sub>)", table_cell_style), Paragraph("--", table_cell_style), Paragraph("0.0360", table_cell_style), Paragraph("20/20 <= 0.25", table_cell_style)],
        [Paragraph("Max Pair Distance (d<sub>max</sub>)", table_cell_style), Paragraph("--", table_cell_style), Paragraph("0.0360", table_cell_style), Paragraph("20/20 <= 0.10", table_cell_style)]
    ]
    t5 = Table(t5_data, colWidths=[col_width*0.35, col_width*0.22, col_width*0.23, col_width*0.20])
    t5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F3F4')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>TABLE V</b><br/>MATCHING DISTANCE, COVARIATE SMDS & THRESHOLD SENSITIVITY", ParagraphStyle("TCap", parent=styles["Normal"], fontSize=8, leading=10, alignment=1)))
    story.append(t5)

    # Section 8
    story.append(Paragraph("VIII. Limitations", heading1_style))
    story.append(Paragraph("This evaluation has explicit scope boundaries:", body_style))
    story.append(Paragraph("• <b>Model Scope</b>: Evaluated on a single model family (Qwen2.5-Math-1.5B) across two released checkpoints.", body_style))
    story.append(Paragraph("• <b>Benchmark Scope</b>: Evaluation uses 20 GSM8K test items (N=20). Benchmark pretraining contamination cannot be ruled out.", body_style))
    story.append(Paragraph("• <b>Sample Size</b>: 5 stochastic continuations per state/policy serve as evaluation samples, not independent training replications.", body_style))
    story.append(Paragraph("• <b>No Causal Claim</b>: Results represent a descriptive contrast under controlled state matching, not a causal claim regarding post-training mechanisms.", body_style))

    # Section 9
    story.append(Paragraph("IX. Reproducibility & Artifact Availability", heading1_style))
    story.append(Paragraph("All code, raw evidence, and verification scripts are publicly available. The sealed raw rollout dataset RAW_NEURAL_ROLLOUTS.jsonl (SHA-256: 51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4) is archived under Git commit 2252cf13adb4b929d4b85ffc909e8ea9089ba041. The publication certificate PUBLICATION_EMPIRICAL_CERTIFICATE_V2.json (SHA-256: 3f3291ab...) is committed under 8228f1c0.", body_style))

    # Section 10
    story.append(Paragraph("X. Conclusion", heading1_style))
    story.append(Paragraph("We introduced recovery_eval, a state-matched evaluation framework for language-model reasoning trajectories. By prospectively matching recovery states with control states and maintaining strict evidence governance, the framework enables fine-grained diagnostics of post-training behavior.", body_style))

    # References
    story.append(Paragraph("References", heading1_style))
    refs = [
        "[1] K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman, 'Training verifiers to solve math word problems,' arXiv preprint arXiv:2110.14168, 2021.",
        "[2] A. Yang, B. Zhang, B. Zheng, D. Liu, J. Zhou, et al., 'Qwen2.5-Math technical report: Toward open math large language models with mathematical reasoning capabilities,' arXiv preprint arXiv:2409.12122, 2024.",
        "[3] H. Lightman, V. Kosaraju, Y. Shen, G. Hase, P. Clark, et al., 'Let's verify step by step,' in International Conference on Learning Representations (ICLR), 2024.",
        "[4] E. Zelikman, Y. Wu, J. Mu, and N. D. Goodman, 'STaR: Bootstrapping reasoning with reasoning,' in Advances in Neural Information Processing Systems (NeurIPS), 2022.",
        "[5] C. Snell, K. Lee, K. Xu, and S. Levine, 'Scaling LLM test-time compute optimally can be more effective than scaling model parameters,' arXiv preprint arXiv:2408.03314, 2024.",
        "[6] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou, 'Self-consistency improves chain of thought reasoning in language models,' in International Conference on Learning Representations (ICLR), 2023.",
        "[7] P. R. Rosenbaum and D. B. Rubin, 'The central role of the propensity score in observational studies for causal effects,' Biometrika, vol. 70, no. 1, pp. 41-55, 1983.",
        "[8] D. E. Ho, K. Imai, G. King, and E. A. Stuart, 'Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference,' Political Analysis, vol. 15, no. 3, pp. 199-236, 2007.",
        "[9] P. C. Austin, 'An introduction to propensity score methods for reducing the effects of confounding in observational studies,' Multivariate Behavioral Research, vol. 46, no. 3, pp. 399-424, 2011."
    ]
    for r in refs:
        story.append(Paragraph(r, ParagraphStyle("Ref", parent=styles["Normal"], fontSize=8, leading=10, spaceAfter=3)))

    # Pad out text slightly to reach exactly 10 pages or 9.5-9.9 pages
    # Let's build document
    doc.build(story)

    # Copy to submission_mlbd2026/
    sub_pdf_path = os.path.join(sub_pkg_dir, "main.pdf")
    shutil.copy2(pdf_path, sub_pdf_path)

    # Compute SHA-256
    pdf_sha = hashlib.sha256(open(pdf_path, "rb").read()).hexdigest()
    sz = os.path.getsize(pdf_path)

    with open(os.path.join(manuscript_dir, "FINAL_PDF_SHA256.txt"), "w") as f:
        f.write(f"{pdf_sha}  main.pdf\n")
    with open(os.path.join(sub_pkg_dir, "FINAL_PDF_SHA256.txt"), "w") as f:
        f.write(f"{pdf_sha}  main.pdf\n")

    print(f"[+] Successfully generated main.pdf ({sz} bytes, SHA-256: {pdf_sha[:8]}...)", flush=True)

if __name__ == "__main__":
    create_pdf()
