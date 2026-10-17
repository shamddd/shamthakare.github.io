import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

class AcademicCVCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        page_text = f"Sham Satish Thakare — Curriculum Vitae — Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 36, 20, page_text)
        self.drawString(36, 20, "Academic CV · Independent Researcher · Gold Medal in Mathematics (SPPU 2024)")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 612 - 36, 32)
        self.restoreState()


def build_academic_cv(output_pdf="Sham_Satish_Thakare_Academic_CV.pdf", output_docx="Sham_Satish_Thakare_Academic_CV.docx"):
    # 1. BUILD PDF
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        alignment=1,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1e293b"),
        alignment=1,
        spaceAfter=3
    )

    contact_style = ParagraphStyle(
        'ContactLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2563eb"),
        alignment=1,
        spaceAfter=8
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=8,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=10,
        spaceAfter=2.5
    )

    story = []

    # Header
    story.append(Paragraph("Sham Satish Thakare", title_style))
    story.append(Paragraph("<b>Independent Computer Science Researcher</b> &nbsp;|&nbsp; <b>Gold Medal in Mathematics (2024)</b>", subtitle_style))
    story.append(Paragraph(
        'Pune, India &nbsp;•&nbsp; <a href="mailto:shamthakare3000@gmail.com">shamthakare3000@gmail.com</a> &nbsp;•&nbsp; '
        '<a href="https://shamddd.github.io/shamthakare.github.io/">Portfolio: shamddd.github.io</a> &nbsp;•&nbsp; '
        '<a href="https://github.com/shamddd">GitHub: @shamddd</a> &nbsp;•&nbsp; '
        '<a href="https://ssrn.com/author=13130226">SSRN Author</a>',
        contact_style
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0f172a"), spaceBefore=0, spaceAfter=6))

    # Research Interests
    story.append(Paragraph("RESEARCH INTERESTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))
    story.append(Paragraph(
        "<b>Mathematical Machine Learning &amp; RLVR:</b> Token-predictive entropy confounding with completion length (r = +0.486), length-controlled credit allocation, and verifiable reward optimization in foundation models.<br/>"
        "<b>Fault-Tolerant Distributed Consensus:</b> Dynamic quorum adaptation algorithms, latency profiling under non-uniform round-trip delays, and tail latency elimination in C++20 Raft consensus clusters (<code>quorumshift</code>).<br/>"
        "<b>State-Matched Counterfactual Error Recovery:</b> Difference-in-differences evaluation protocols isolating self-correction from unconditional generative capacity under frozen structural covariates.",
        body_style
    ))
    story.append(Spacer(1, 3))

    # Education
    story.append(Paragraph("EDUCATION &amp; ACADEMIC HONORS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))
    
    edu_data = [
        [
            Paragraph("<b>Savitribai Phule Pune University (APCOER Pune)</b>, Pune, Maharashtra, India", body_style),
            Paragraph("<b>2020 – 2024</b>", ParagraphStyle('RightText', parent=body_style, alignment=2))
        ],
        [
            Paragraph("<i>Bachelor of Engineering (B.E.) in Artificial Intelligence and Data Science</i> &nbsp;|&nbsp; <b>First Class with Distinction</b>", body_style),
            Paragraph("Conferred April 2024", ParagraphStyle('RightTextSub', parent=body_style, alignment=2, textColor=colors.HexColor("#64748b")))
        ]
    ]
    t_edu = Table(edu_data, colWidths=[420, 120])
    t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_edu)
    story.append(Paragraph("• <b>Gold Medal in Mathematics (2024):</b> Conferred for highest academic standing across mathematical and quantitative curricula (Calculus, Linear Algebra, Discrete Mathematics, Probability &amp; Statistics, Optimization).", bullet_style))
    story.append(Paragraph("• <b>Academic Standing:</b> Cumulative GPA: <b>8.70 / 10.00</b> (170/170 Credits Completed, Total Grade Points: 1479/1700; Seat: <code>B191102032</code>, PRN: <code>72159719L</code>).", bullet_style))
    story.append(Paragraph("• <b>Final Year Academic Rank:</b> Final Year SGPA: <b>9.53 / 10.00</b> (Department Rank 1).", bullet_style))
    story.append(Paragraph("• <b>Flagship Coursework Honors (Grade O / 10.0 Outstanding):</b> Distributed Computing (10/10), Artificial Neural Networks (10/10), Operating Systems (10/10), Cyber Security (10/10), Capstone Senior Thesis (10/10), Industry Internship (10/10).", bullet_style))
    story.append(Paragraph("• <b>Medium of Instruction:</b> Certified as <b>ENGLISH</b> on official university transcripts (Ref: <code>EXAM./TRANS./BEN241203044</code>).", bullet_style))
    story.append(Spacer(1, 3))

    # Research & Professional Experience
    story.append(Paragraph("RESEARCH &amp; PROFESSIONAL EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))

    exp1 = [
        [Paragraph("<b>Independent Research</b> — Foundation Model Reasoning &amp; Systems", body_style), Paragraph("<b>06/2024 – Present</b>", ParagraphStyle('RightText', parent=body_style, alignment=2))],
        [Paragraph("<i>Pre-Doctoral Researcher / Systems Research Lead</i>", body_style), Paragraph("Pune, India", ParagraphStyle('RightTextSub', parent=body_style, alignment=2, textColor=colors.HexColor("#64748b")))]
    ]
    t_e1 = Table(exp1, colWidths=[420, 120])
    t_e1.setStyle(TableStyle([('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_e1)
    story.append(Paragraph("• Formulated failure-domain aware dynamic quorum adaptation algorithms and spectral latency estimators in C++20 Raft consensus clusters (<code>quorumshift</code>), proving non-empty quorum intersection invariants under asymmetric partitions.", bullet_style))
    story.append(Paragraph("• Eliminated p99 tail latency degradation under asymmetric partitions without violating safety or linearizability guarantees across multi-region benchmarks. Manuscript under review at <i>IEEE Transactions on Artificial Intelligence (IEEE TAI)</i>.", bullet_style))
    story.append(Paragraph("• Investigated token-predictive entropy confounding in reinforcement learning with verifiable rewards (GRPO), demonstrating substantial completion-length collinearity (r = +0.486) and developing length-controlled credit allocation estimators. Under review at <i>IEEE TAI 2026</i>.", bullet_style))
    story.append(Paragraph("• Formulated state-contrast continuation evaluation (D_recovery = -0.1100) in <code>recovery_eval</code> and <code>stateshift</code> to measure error recovery under frozen structural covariates. Under review at <i>IEEE BigData 2026</i> and submitted to <i>Elsevier AIJ</i>.", bullet_style))
    story.append(Paragraph("• Designed layered runtime boundary enforcement and deterministic state-interception architectures for autonomous tool execution safety (<code>medirush-safeagent</code>). In peer review at <i>Intelligence-Based Medicine (Elsevier)</i> &amp; SSRN 7446543.", bullet_style))
    story.append(Spacer(1, 3))

    exp2 = [
        [Paragraph("<b>APCOER Pune (Savitribai Phule Pune University)</b> — Dept. of AI &amp; Data Science", body_style), Paragraph("<b>06/2023 – 12/2024</b>", ParagraphStyle('RightText', parent=body_style, alignment=2))],
        [Paragraph("<i>Undergraduate Researcher &amp; Teaching Assistant</i>", body_style), Paragraph("Pune, India", ParagraphStyle('RightTextSub', parent=body_style, alignment=2, textColor=colors.HexColor("#64748b")))]
    ]
    t_e2 = Table(exp2, colWidths=[420, 120])
    t_e2.setStyle(TableStyle([('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_e2)
    story.append(Paragraph("• Conducted research on foundation model reasoning architectures, length confounding, and evaluation protocols with department faculty.", bullet_style))
    story.append(Paragraph("• Served as Teaching Assistant for undergraduate coursework in <i>Data Structures, Algorithms, and Foundations of Machine Learning</i>.", bullet_style))
    story.append(Paragraph("• Developed open-source benchmark scripts and automated test suites for algorithmic problem solving.", bullet_style))
    story.append(Spacer(1, 3))

    # Manuscripts & Publications
    story.append(Paragraph("PUBLICATIONS, PREPRINTS &amp; MANUSCRIPTS UNDER REVIEW", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))

    pubs = [
        ("When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning",
         "<b>Sham Satish Thakare</b>",
         "Under Review at <i>IEEE Transactions on Artificial Intelligence (IEEE TAI)</i>, 2026. [<a href='https://github.com/shamddd/ear_grpo_reasoning'>Code</a>] [<a href='https://shamddd.github.io/shamthakare.github.io/pdfs/when-confidence-confounds-reasoning-complexity.pdf'>PDF</a>]"),
        ("AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus",
         "<b>Sham Satish Thakare</b>",
         "Under Review at <i>IEEE Transactions on Artificial Intelligence (IEEE TAI)</i>, 2026. [<a href='https://github.com/shamddd/quorumshift'>Code (C++20)</a>]"),
        ("recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning",
         "<b>Sham Satish Thakare</b>",
         "Under Review at <i>11th IEEE Special Session on Machine Learning on Big Data (IEEE BigData 2026)</i>. [<a href='https://github.com/shamddd/recovery_eval'>Code</a>] [<a href='https://shamddd.github.io/shamthakare.github.io/pdfs/recovery-eval.pdf'>PDF</a>]"),
        ("StateShift: State-Matched Evaluation of Error Recovery in Neural Reasoning",
         "<b>Sham Satish Thakare</b>",
         "Submitted to <i>Elsevier Artificial Intelligence (AIJ)</i>, 2026. [<a href='https://github.com/shamddd/stateshift'>Code</a>] [<a href='https://shamddd.github.io/shamthakare.github.io/pdfs/stateshift.pdf'>PDF</a>]"),
        ("MediRush-SafeAgent: Layered Runtime Enforcement for Healthcare-Commerce LLM Tool Execution",
         "<b>Sham Satish Thakare</b>",
         "In Peer Review at <i>Intelligence-Based Medicine (Elsevier)</i> &amp; SSRN Preprint 7446543. [<a href='https://github.com/shamddd/medirush-safeagent'>Code</a>] [<a href='http://ssrn.com/abstract=7446543'>SSRN</a>]")
    ]

    for title, authors, venue in pubs:
        story.append(Paragraph(f"• <b>{title}</b>", body_style))
        story.append(Paragraph(f"&nbsp;&nbsp;{authors} &bull; {venue}", bullet_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 2))

    # Academic Leadership & Teaching
    story.append(Paragraph("TEACHING, MENTORSHIP &amp; LEADERSHIP", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))

    story.append(Paragraph("• <b>President, Social Volunteer Club</b>, APCOER Pune (2023 – 2024): Elected student head of university community outreach during final undergraduate year. Directed educational mentoring in quantitative and computational skills for 200+ underprivileged high-school youth, blood donation camps, digital literacy programs, and campus sustainability drives across Pune district.", bullet_style))
    story.append(Paragraph("• <b>Teaching Assistant, Foundations of Machine Learning</b>, APCOER Pune (2023 – 2024): Conducted tutorial sessions, code walkthroughs, and doubt-clearing labs covering supervised learning, optimization algorithms, loss landscape geometry, and PyTorch implementations.", bullet_style))
    story.append(Paragraph("• <b>Teaching Assistant, Data Structures &amp; Algorithms</b>, APCOER Pune (2023 – 2024): Led lab sessions on algorithmic complexity, graph traversal, balanced search trees, and dynamic programming. Designed automated test evaluation harnesses for student programming assignments.", bullet_style))
    story.append(Spacer(1, 3))

    # Skills & Standardized Tests
    story.append(Paragraph("TECHNICAL SKILLS &amp; CERTIFICATIONS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=0, spaceAfter=4))

    story.append(Paragraph("• <b>Mathematics &amp; Theory:</b> Real Analysis, Advanced Linear Algebra (Spectral Decomposition, SVD), Probability Theory &amp; Stochastic Processes, Convex Optimization (KKT Conditions, Gradient Dynamics), Discrete Mathematics, Graph Theory.", bullet_style))
    story.append(Paragraph("• <b>Machine Learning &amp; AI:</b> Reinforcement Learning (PPO, GRPO, RLVR), Transformer Architectures, Statistical Learning Theory, PyTorch, JAX, Hugging Face Transformers, NumPy, SciPy.", bullet_style))
    story.append(Paragraph("• <b>Systems Programming:</b> C++ (C++20 Multithreading, Lock-free Atomics), Distributed Consensus (Raft), POSIX, Linux Kernel Internals, OpenTelemetry, Git, Docker, LaTeX.", bullet_style))
    story.append(Paragraph("• <b>Standardized Exams &amp; Credentials:</b> Academic IELTS Overall Band <b>6.5</b> (CEFR B2) &bull; German APS Certificate (Prüfnummer <code>41183/24</code>) &bull; Oracle Certified Architect Associate (OCI 2024) &bull; Oracle AI Database Foundations &bull; Microsoft Certified: SQL AI Developer &bull; Google AI Professional Certificate &bull; IIT Bombay Kotlin Tutorial (Cert: <code>3206110F6D</code>).", bullet_style))

    doc.build(story, canvasmaker=AcademicCVCanvas)
    print(f"Generated PDF: {output_pdf}")

    # 2. BUILD DOCX
    doc_docx = docx.Document()
    for section in doc_docx.sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)

    p_head = doc_docx.add_paragraph()
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_name = p_head.add_run("Sham Satish Thakare\n")
    run_name.font.size = Pt(18)
    run_name.font.bold = True
    run_sub = p_head.add_run("Independent Computer Science Researcher | Gold Medal in Mathematics (2024)\n")
    run_sub.font.size = Pt(10)
    run_sub.font.bold = True
    run_contact = p_head.add_run("Pune, India | shamthakare3000@gmail.com | Portfolio: shamddd.github.io | GitHub: @shamddd\n\n")
    run_contact.font.size = Pt(9)

    p_sec1 = doc_docx.add_paragraph()
    r_s1 = p_sec1.add_run("RESEARCH INTERESTS\n")
    r_s1.font.bold = True
    p_sec1_body = doc_docx.add_paragraph(
        "• Mathematical Machine Learning & RLVR: Token-predictive entropy confounding with completion length (r = +0.486), length-controlled credit allocation, and verifiable reward optimization in foundation models.\n"
        "• Fault-Tolerant Distributed Consensus: Dynamic quorum adaptation algorithms, latency profiling under non-uniform round-trip delays, and tail latency elimination in C++20 Raft consensus clusters (quorumshift).\n"
        "• State-Matched Counterfactual Error Recovery: Difference-in-differences evaluation protocols isolating self-correction from unconditional generative capacity under frozen structural covariates.\n"
    )

    p_sec2 = doc_docx.add_paragraph()
    r_s2 = p_sec2.add_run("EDUCATION & ACADEMIC HONORS\n")
    r_s2.font.bold = True
    doc_docx.add_paragraph(
        "Savitribai Phule Pune University (APCOER Pune), Pune, Maharashtra, India (2020 – 2024)\n"
        "Bachelor of Engineering (B.E.) in Artificial Intelligence and Data Science | First Class with Distinction (Conferred April 2024)\n"
        "• Gold Medal in Mathematics (2024): Conferred for highest academic standing across mathematical and quantitative curricula.\n"
        "• Academic Standing: Cumulative GPA: 8.70 / 10.00 (Department Rank 1, Final Year SGPA: 9.53 / 10.00).\n"
        "• Medium of Instruction: Certified as ENGLISH on official university transcripts.\n"
    )

    p_sec3 = doc_docx.add_paragraph()
    r_s3 = p_sec3.add_run("RESEARCH & PROFESSIONAL EXPERIENCE\n")
    r_s3.font.bold = True
    doc_docx.add_paragraph(
        "Independent Research — Foundation Model Reasoning & Systems (06/2024 – Present)\n"
        "Pre-Doctoral Researcher / Systems Research Lead | Pune, India\n"
        "• Formulated failure-domain aware dynamic quorum adaptation algorithms and spectral latency estimators in C++20 Raft consensus clusters (quorumshift), proving non-empty quorum intersection invariants.\n"
        "• Eliminated p99 tail latency degradation under asymmetric partitions without violating safety or linearizability guarantees. Under review at IEEE Transactions on Artificial Intelligence (IEEE TAI).\n"
        "• Investigated token-predictive entropy confounding in reinforcement learning with verifiable rewards (GRPO), demonstrating substantial completion-length collinearity (r = +0.486). Under review at IEEE TAI 2026.\n"
        "• Formulated state-contrast continuation evaluation (D_recovery = -0.1100) in recovery_eval and stateshift. Under review at IEEE BigData 2026 and submitted to Elsevier AIJ.\n"
        "• Designed layered runtime boundary enforcement and deterministic state-interception architectures for autonomous tool execution safety (medirush-safeagent). Under review at Elsevier IBMED.\n\n"
        "APCOER Pune (Savitribai Phule Pune University) — Dept. of AI & Data Science (06/2023 – 12/2024)\n"
        "Undergraduate Researcher & Teaching Assistant | Pune, India\n"
        "• Conducted research on foundation model reasoning architectures, length confounding, and evaluation protocols with department faculty.\n"
        "• Served as Teaching Assistant for undergraduate coursework in Data Structures, Algorithms, and Foundations of Machine Learning.\n"
    )

    p_sec4 = doc_docx.add_paragraph()
    r_s4 = p_sec4.add_run("PUBLICATIONS & MANUSCRIPTS UNDER REVIEW\n")
    r_s4.font.bold = True
    for title, authors, venue in pubs:
        clean_authors = authors.replace("<b>", "").replace("</b>", "")
        clean_venue = venue.replace("<i>", "").replace("</i>", "").replace("&bull;", "•")
        # Strip html links
        import re
        clean_venue = re.sub(r'<[^>]+>', '', clean_venue)
        doc_docx.add_paragraph(f"• {title}\n  {clean_authors} • {clean_venue}")

    doc_docx.save(output_docx)
    print(f"Generated DOCX: {output_docx}")

if __name__ == "__main__":
    build_academic_cv()
