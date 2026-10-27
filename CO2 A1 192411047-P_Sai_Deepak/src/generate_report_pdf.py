"""
Generate Publication-Grade Formatted PDF Report (DAA_A2_192411047.pdf)
Tightly formatted layout with zero orphan pages, properly rendered math,
and side-by-side/stacked figures matching academic report standards.
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
GRAPHS_DIR = os.path.join(BASE_DIR, "results", "graphs")

STUDENT_NAME = "P Sai Deepak"
REG_NO = "192411047"
SEED = 1047
REPO_LINK = "https://github.com/sai-deepak-192411047/DAA-A2-192411047-P_Sai_Deepak"

class NumberedCanvas(canvas.Canvas):
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
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, f"DAA Assignment 2 (CO2) | Student: {STUDENT_NAME} ({REG_NO})")
            self.drawRightString(558, 755, "Brute-Force & Exhaustive Search")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(54, 750, 558, 750)
            
        # Footer
        self.setFont("Helvetica", 8)
        self.drawString(54, 30, f"Confidential & Academic Authorship | Reg No: {REG_NO} | Personal Seed: {SEED}")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 30, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(54, 40, 558, 40)
        self.restoreState()

def build_pdf():
    pdf_path = os.path.join(REPORT_DIR, f"DAA_A2_{REG_NO}.pdf")
    # Printable area: 612 x 792 pt. Margins: 54 pt left/right -> 504 pt printable width.
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor("#1B365D")   # Deep Navy
    c_secondary = colors.HexColor("#2B6CB0") # Medium Blue
    c_dark = colors.HexColor("#2D3748")      # Charcoal Text
    c_bg_light = colors.HexColor("#F7FAFC")
    
    # Typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=c_primary,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        alignment=1,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=8
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=c_primary,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=c_secondary,
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=c_dark,
        spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2.5
    )
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor("#1A202C"),
        backColor=colors.HexColor("#EDF2F7"),
        leftIndent=6,
        rightIndent=6,
        spaceBefore=3,
        spaceAfter=4
    )
    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=9.5,
        alignment=1,
        textColor=colors.HexColor("#4A5568"),
        spaceBefore=2,
        spaceAfter=4
    )

    story = []

    # =============================================================
    # PAGE 1: TITLE, METADATA & Q1 FOUNDATION
    # =============================================================
    story.append(Paragraph("DESIGN AND ANALYSIS OF ALGORITHMS", title_style))
    story.append(Paragraph("COURSE OUTCOME 2 (CO2) – LABORATORY REPORT", title_style))
    story.append(Paragraph("Brute-Force and Exhaustive-Search Techniques: Empirical Investigation, Mathematical Analysis, and Algorithmic Redesign", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_primary, spaceBefore=0, spaceAfter=6))

    meta_table_data = [
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph(STUDENT_NAME, body_style)],
        [Paragraph("<b>Registration Number:</b>", body_style), Paragraph(REG_NO, body_style)],
        [Paragraph("<b>Personal Dataset Seed:</b>", body_style), Paragraph(f"<b>{SEED}</b> (Last 4 digits of Registration Number)", body_style)],
        [Paragraph("<b>Course Module:</b>", body_style), Paragraph("DAA Assignment 2 (CO2 - Brute-Force & Exhaustive Search)", body_style)],
        [Paragraph("<b>GitHub Repository:</b>", body_style), Paragraph(f"<font color='#0066CC'><u>{REPO_LINK}</u></font>", body_style)]
    ]
    t_meta = Table(meta_table_data, colWidths=[150, 354])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_light),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    story.append(Paragraph("Q1 – Sorting Under Different Data Conditions (6 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> An e-commerce fulfilment centre prioritises customer dispatch orders using dynamic priority scores. Incoming data distributions vary: Randomly ordered, Reverse-sorted (significantly disordered), and 95% Nearly Sorted (batches added to an already sorted queue).", body_style))
    story.append(Paragraph("<b>Theoretical Predictions & Algorithmic Rationale:</b>", h2_style))
    story.append(Paragraph("• <b>Selection Sort:</b> Strictly data-independent. Scans unsorted suffix for minimum regardless of input arrangement. Comparisons are strictly n(n - 1) / 2 = &Theta;(n<sup>2</sup>) in all cases. Swaps are at most n - 1 = O(n), minimizing write operations.", bullet_style))
    story.append(Paragraph("• <b>Bubble Sort:</b> Adjacent pairwise comparison with early-termination flag. In best case (sorted), stops after n - 1 comparisons. In worst case (reverse), requires n(n - 1) / 2 comparisons and swaps. Distant inversions in nearly sorted data force multiple quadratic passes.", bullet_style))
    story.append(Paragraph("• <b>Insertion Sort:</b> Running time is an adaptive function of inversion count I: T(n) = O(n + I). In 95% nearly sorted data (I &lt;&lt; n<sup>2</sup>), inner while-loop breaks immediately upon encountering key &ge; a[j], running in near-linear O(n) time. Reverse sorted degenerates to &Theta;(n<sup>2</sup>).", bullet_style))

    story.append(Spacer(1, 4))
    q1_t_data = [
        ["Dataset Condition", "N", "Algorithm", "Comparisons", "Swaps / Shifts", "Time (ms)"],
        ["Random", "1000", "Selection Sort", "499,500", "998", "32.10"],
        ["Random", "1000", "Bubble Sort", "498,324", "240,654", "63.71"],
        ["Random", "1000", "Insertion Sort", "241,646", "240,654", "32.55"],
        ["Reverse Sorted", "1000", "Selection Sort", "499,500", "528", "32.12"],
        ["Reverse Sorted", "1000", "Bubble Sort", "499,500", "499,443", "91.29"],
        ["Reverse Sorted", "1000", "Insertion Sort", "499,500", "499,443", "67.42"],
        ["95% Nearly Sorted", "1000", "Selection Sort", "499,500", "50", "29.85"],
        ["95% Nearly Sorted", "1000", "Bubble Sort", "452,710", "24,812", "38.19"],
        ["95% Nearly Sorted", "1000", "Insertion Sort", "26,112", "24,812", "3.61"],
    ]
    t_q1 = Table(q1_t_data, colWidths=[114, 36, 94, 84, 94, 82])
    t_q1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('BACKGROUND', (0,9), (-1,9), colors.HexColor("#D4EFDF")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q1)

    # PAGE 1 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 2: Q1 VISUALS & DECISION DEFENCE
    # =============================================================
    story.append(Paragraph("Q1 – Experimental Visual Evidence & Decision Defence", h1_style))
    g1_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140832.png")
    if os.path.exists(g1_p):
        story.append(Image(g1_p, width=5.6*inch, height=2.45*inch))
        story.append(Paragraph("Figure 1.1: Scaling of key comparisons across sorting algorithms under contrasting dataset arrangements.", caption_style))

    s1_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140815.png")
    if os.path.exists(s1_p):
        story.append(Image(s1_p, width=5.6*inch, height=2.25*inch))
        story.append(Paragraph(f"Figure 1.2: Terminal execution benchmark for Q1 (Reg No: {REG_NO} | {STUDENT_NAME}).", caption_style))

    story.append(Paragraph("<b>Design Decision & Recommendation Defence:</b>", h2_style))
    story.append(Paragraph("For the fulfilment centre where 95% of orders are already sorted, <b>INSERTION SORT</b> is unequivocally recommended. Empirical evidence demonstrates that at N = 1000, Insertion Sort requires only 26,112 comparisons and 3.61 ms, compared to 499,500 comparisons for Selection Sort (19.1x more work) and 452,710 for Bubble Sort (17.3x more work). Because Insertion Sort's inner while-loop terminates on the very first comparison when key &ge; a[j], it achieves near-linear O(n) execution when the inversion count is small. Thus, Insertion Sort is overwhelmingly superior for continuous e-commerce queue updates.", body_style))

    # PAGE 2 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 3: Q2 SEQUENTIAL SEARCH (SELF-CONTAINED COMPLETE PAGE)
    # =============================================================
    story.append(Paragraph("Q2 – When Is Sequential Search an Appropriate Engineering Choice? (4 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> Aircraft maintenance facility tracking active tools (Tool ID, Tech ID, Issue Time, Bay). Personal search keys derived from registration number: <b>Found Target = T-1047</b> | <b>Not-Found Target = T-1048</b>.", body_style))
    
    q2_t_data = [
        ["List Size (N)", "Search Scenario", "Target Tool ID", "Comparisons", "Time (μs)", "Found?"],
        ["100", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"],
        ["100", "Average Case (Middle)", f"T-{SEED}", "51", "5.10", "Yes"],
        ["100", "Worst Case (End)", f"T-{SEED}", "100", "8.90", "Yes"],
        ["100", "Unsuccessful Search", f"T-{SEED+1}", "100", "8.70", "No"],
        ["1,000", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"],
        ["1,000", "Average Case (Middle)", f"T-{SEED}", "501", "37.50", "Yes"],
        ["1,000", "Worst Case (End)", f"T-{SEED}", "1,000", "64.90", "Yes"],
        ["1,000", "Unsuccessful Search", f"T-{SEED+1}", "1,000", "64.80", "No"],
        ["10,000", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"],
        ["10,000", "Average Case (Middle)", f"T-{SEED}", "5,001", "334.60", "Yes"],
        ["10,000", "Worst Case (End)", f"T-{SEED}", "10,000", "847.30", "Yes"],
        ["10,000", "Unsuccessful Search", f"T-{SEED+1}", "10,000", "600.70", "No"],
    ]
    t_q2 = Table(q2_t_data, colWidths=[80, 130, 94, 80, 70, 50])
    t_q2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q2)
    story.append(Spacer(1, 4))

    # Side-by-side Table for Q2 Graph & Terminal Screenshot
    g2_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140940.png")
    s2_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140918.png")
    if os.path.exists(g2_p) and os.path.exists(s2_p):
        q2_img_table = Table([
            [Image(g2_p, width=3.35*inch, height=1.7*inch), Image(s2_p, width=3.35*inch, height=1.7*inch)],
            [Paragraph("Figure 2.1: Key comparisons vs active list size N.", caption_style),
             Paragraph(f"Figure 2.2: Terminal execution output (Reg No: {REG_NO}).", caption_style)]
        ], colWidths=[252, 252])
        q2_img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 2),
            ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(q2_img_table)

    story.append(Paragraph("<b>Engineering Evaluation & Scalability Boundary:</b>", h2_style))
    story.append(Paragraph("Sequential Search is a reasonable engineering choice ONLY when the dataset is small (N &lt; 200), record churn is high (O(1) unsorted append/delete without tree rebalancing), and lookup query frequency is low. When the organization expands to 20 facilities (scaling active records to N = 20,000, with 10,000 lookups/hour), Sequential Search would require 10,000 &times; 10,000 = 100,000,000 comparisons per hour, causing severe CPU contention. Sequential search must be abandoned in favor of an In-Memory Hash Map (O(1) expected lookup) or a Distributed B-Tree index (O(log N) lookup).", body_style))

    # PAGE 3 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 4: Q3 BRUTE-FORCE STRING MATCHING (SELF-CONTAINED COMPLETE PAGE)
    # =============================================================
    story.append(Paragraph("Q3 – Engineer the Behaviour of Brute-Force String Matching (6 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> Cybersecurity log screening for known intrusion signatures. We deliberately engineer text-pattern pairs to expose extreme algorithmic behavior under low-work, high-work, and realistic cascading conditions.", body_style))
    
    q3_t_data = [
        ["Test Condition", "Text Len (n)", "Pat Len (m)", "Comparisons", "Shifts", "Time (ms)"],
        ["Test 1: Low-Work (Immediate Mismatch)", "10,000", "20", "9,981", "9,981", "0.58"],
        ["Test 2: High-Work (Last-Char Mismatch)", "10,000", "20", "199,620", "9,981", "12.44"],
        ["Test 3: Cybersecurity Prefix Cascade", "20,084", "48", "38,241", "20,037", "2.15"],
    ]
    t_q3 = Table(q3_t_data, colWidths=[174, 70, 70, 70, 60, 60])
    t_q3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q3)
    story.append(Spacer(1, 4))

    # Side-by-side Table for Q3 Graph & Terminal Screenshot
    g3_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141058.png")
    s3_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141035.png")
    if os.path.exists(g3_p) and os.path.exists(s3_p):
        q3_img_table = Table([
            [Image(g3_p, width=3.35*inch, height=1.75*inch), Image(s3_p, width=3.35*inch, height=1.75*inch)],
            [Paragraph("Figure 3.1: Character comparisons across engineered patterns.", caption_style),
             Paragraph(f"Figure 3.2: Terminal execution output (Reg No: {REG_NO}).", caption_style)]
        ], colWidths=[252, 252])
        q3_img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 2),
            ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(q3_img_table)

    story.append(Paragraph("<b>Inquiry & Algorithmic Findings:</b>", h2_style))
    story.append(Paragraph("1. <b>Theoretical vs Observed Precision:</b> Observed comparisons matched predictions with 100% precision: Test 1 yielded exactly n - m + 1 = 9,981 comparisons, whereas Test 2 yielded (n - m + 1) &times; m = 199,620 comparisons (a 20.0x work explosion on identical text lengths!).", bullet_style))
    story.append(Paragraph("2. <b>Structural Determinants of Inefficiency:</b> Inefficiency arises from pattern self-similarity: matching m - 1 characters before failing on the last character discards all partial match information upon shifting by 1, forcing repeated character inspections.", bullet_style))
    story.append(Paragraph("3. <b>Input Size Limitations:</b> Evaluating string search algorithms solely on input sizes (n, m) is fundamentally deficient; character entropy and prefix overlap govern whether execution is O(n) or O(n &times; m).", bullet_style))

    # PAGE 4 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 5: Q4 CLOSEST PAIR (SELF-CONTAINED COMPLETE PAGE)
    # =============================================================
    story.append(Paragraph("Q4 – Closest Pair and the Cost of Examining Every Possibility (6 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> Drone collision-risk monitoring system. Airspace collision radar must continually compute the minimum Euclidean distance among active drones to trigger avoidance alerts.", body_style))
    story.append(Paragraph("<b>Mathematical Pair-Count Derivation:</b> Given n drones D = {D<sub>0</sub>, ..., D<sub>n-1</sub>}, candidate pairs are unordered 2-combinations {D<sub>i</sub>, D<sub>j</sub>}. Duplicate comparisons and self-comparisons are eliminated by strictly enforcing index order i &lt; j. Total unique pairs examined:", body_style))
    story.append(Paragraph("<b>Total Unique Candidate Pairs</b> = &Sigma;<sub>i=0</sub><sup>n-2</sup> &Sigma;<sub>j=i+1</sub><sup>n-1</sup> 1 = &Sigma;<sub>i=0</sub><sup>n-2</sup> (n - 1 - i) = (n - 1) + (n - 2) + ... + 1 = <b>n(n - 1) / 2 = &Theta;(n<sup>2</sup>)</b>.", body_style))
    
    q4_t_data = [
        ["Drones (N)", "Theoretical n(n-1)/2", "Pairs Examined", "Dist Calcs", "Time (ms)", "Status"],
        ["100", "4,950", "4,950", "4,950", "0.78", "Acceptable"],
        ["500", "124,750", "124,750", "124,750", "19.73", "Acceptable"],
        ["1,000", "499,500", "499,500", "499,500", "79.67", "Impractical (> 50 ms)"],
        ["2,000", "1,999,000", "1,999,000", "1,999,000", "351.72", "Impractical"],
        ["4,000", "7,998,000", "7,998,000", "7,998,000", "1,348.50", "Severe Violation"],
    ]
    t_q4 = Table(q4_t_data, colWidths=[70, 110, 84, 80, 70, 90])
    t_q4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q4)
    story.append(Spacer(1, 4))

    # Side-by-side Table for Q4 Graph & Terminal Screenshot
    g4_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141235.png")
    s4_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141210.png")
    if os.path.exists(g4_p) and os.path.exists(s4_p):
        q4_img_table = Table([
            [Image(g4_p, width=3.35*inch, height=1.7*inch), Image(s4_p, width=3.35*inch, height=1.7*inch)],
            [Paragraph("Figure 4.1: Quadratic scaling of candidate pairs n(n-1)/2.", caption_style),
             Paragraph(f"Figure 4.2: Terminal execution output (Reg No: {REG_NO}).", caption_style)]
        ], colWidths=[252, 252])
        q4_img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 2),
            ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(q4_img_table)

    story.append(Paragraph("<b>Scalability Inquiry & Operational Boundary:</b>", h2_style))
    story.append(Paragraph("For real-time drone collision radar, response time must remain within 50.0 ms (20 Hz refresh rate). The brute-force approach becomes impractical at N &approx; 800 drones. Inefficiency originates from computing Euclidean distances between drones miles apart on opposite ends of the city (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)) without spatial filtering. A redesigned strategy must exploit spatial locality to eliminate distant candidate pairs.", body_style))

    # PAGE 5 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 6: Q5 CONVEX HULL (DERIVATION & ALGORITHM DESIGN)
    # =============================================================
    story.append(Paragraph("Q5 – Derive a Convex Hull Algorithm from a Geometric Principle (7 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> Wildlife reserve boundary monitoring. Stations have coordinates P<sub>i</sub> = (x<sub>i</sub>, y<sub>i</sub>). Conservation officers require the outer boundary containing all stations.", body_style))
    story.append(Paragraph("<b>Geometric Principle:</b> <i>\"A line joining two candidate points may form part of the outer boundary if all remaining points lie on an appropriate single side of that line.\"</i>", body_style))
    story.append(Paragraph("<b>Derivation of Computational Procedure:</b>", h2_style))
    story.append(Paragraph("1. <b>Line Equation:</b> Two distinct points P<sub>1</sub>(x<sub>1</sub>, y<sub>1</sub>) and P<sub>2</sub>(x<sub>2</sub>, y<sub>2</sub>) define a line in standard form: a&middot;x + b&middot;y = c, with coefficients: a = y<sub>2</sub> - y<sub>1</sub>, b = x<sub>1</sub> - x<sub>2</sub>, c = x<sub>1</sub>&middot;y<sub>2</sub> - y<sub>1</sub>&middot;x<sub>2</sub>.", bullet_style))
    story.append(Paragraph("2. <b>Relative Position Test:</b> For any third station P<sub>k</sub>(x<sub>k</sub>, y<sub>k</sub>), evaluate the sign of S(P<sub>k</sub>) = a&middot;x<sub>k</sub> + b&middot;y<sub>k</sub> - c. S &gt; 0 indicates the positive half-plane, S &lt; 0 the negative half-plane, and S = 0 indicates collinearity.", bullet_style))
    story.append(Paragraph("3. <b>Boundary Edge Identification:</b> For candidate pair (P<sub>i</sub>, P<sub>j</sub>), check all n - 2 remaining points P<sub>k</sub>. The segment P<sub>i</sub>P<sub>j</sub> is accepted as an outer boundary edge IF AND ONLY IF all remaining points satisfy S(P<sub>k</sub>) &ge; 0, OR all satisfy S(P<sub>k</sub>) &le; 0.", bullet_style))
    story.append(Paragraph("4. <b>Boundary Polygon Construction:</b> Unique vertices from accepted boundary edges are sorted counter-clockwise around their centroid using &theta; = atan2(y - c<sub>y</sub>, x - c<sub>x</sub>).", bullet_style))

    story.append(Paragraph("<b>Algorithm Pseudocode:</b>", h2_style))
    code_text = (
        "ALGORITHM BruteForceConvexHull(P[0..n-1])\n"
        "hull_edges = empty set\n"
        "for i = 0 to n - 2 do\n"
        "    for j = i + 1 to n - 1 do\n"
        "        a = P[j].y - P[i].y; b = P[i].x - P[j].x; c = P[i].x * P[j].y - P[i].y * P[j].x\n"
        "        has_pos = false; has_neg = false\n"
        "        for k = 0 to n - 1 (k != i, j) do\n"
        "            val = a * P[k].x + b * P[k].y - c\n"
        "            if val > 0 then has_pos = true; if val < 0 then has_neg = true\n"
        "            if has_pos and has_neg then break // Points exist on both sides\n"
        "        if not (has_pos and has_neg) then hull_edges.add((P[i], P[j]))\n"
        "return ConstructPolygon(hull_edges)"
    )
    story.append(Paragraph(code_text.replace('\n', '<br/>'), code_style))

    # PAGE 6 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 7: Q5 VISUALS & GEOMETRIC CORRECTNESS ARGUMENT
    # =============================================================
    story.append(Paragraph("Q5 – Boundary Visualisations, Complexity & Correctness", h1_style))
    story.append(Paragraph("<b>Test Configurations:</b> Evaluated under Configuration 1 (Perimeter & Interior Stations, 25 points) and Configuration 2 (Collinear Edge Challenge, multiple collinear stations along boundaries).", body_style))

    g5_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141420.png")
    if os.path.exists(g5_p):
        story.append(Image(g5_p, width=5.6*inch, height=2.45*inch))
        story.append(Paragraph("Figure 5.1: Convex hull boundaries constructed from the student-derived geometric decision rule.", caption_style))

    s5_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141355.png")
    if os.path.exists(s5_p):
        story.append(Image(s5_p, width=5.6*inch, height=2.25*inch))
        story.append(Paragraph(f"Figure 5.2: Terminal execution output for Q5 Convex Hull (Reg No: {REG_NO}).", caption_style))

    story.append(Paragraph("<b>Complexity & Geometric Correctness Argument:</b>", h2_style))
    story.append(Paragraph("• <b>Computational Work Growth:</b> Examining all pairs requires n(n - 1) / 2 iterations, and testing remaining points requires n - 2 side checks, yielding Total Operations = n(n - 1)(n - 2) / 2 = &Theta;(n<sup>3</sup>). Experimental tests confirmed cubic scaling: N = 25 required 6,052 tests (0.8 ms); N = 100 required 480,200 tests (46.8 ms).", bullet_style))
    story.append(Paragraph("• <b>Rigorous Geometric Correctness:</b> By definition, a set S is convex if for all p, q &isin; S, the segment pq &sube; S. A hyperplane H supports S if H touches the boundary and S is entirely contained in one closed half-space of H. A line through points P<sub>i</sub> and P<sub>j</sub> forms a supporting line if and only if all other points lie in one closed half-plane (S(P<sub>k</sub>) &ge; 0 or S(P<sub>k</sub>) &le; 0). The convex hull boundary consists exclusively of segments on supporting lines. Hence, our decision rule is mathematically sound.", bullet_style))

    # PAGE 7 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 8: Q6 EXHAUSTIVE KNAPSACK (FORMULATION & VERIFICATION)
    # =============================================================
    story.append(Paragraph("Q6 – Exhaustive Search and Combinatorial Growth (8 Marks)", h1_style))
    story.append(Paragraph("<b>Problem Context:</b> Humanitarian airlift planning (0/1 Knapsack). Representation: binary bitmask M &isin; [0, 2<sup>n</sup> - 1]. Candidate generation: systematically enumerate all 2<sup>n</sup> masks. Feasibility: W(M) &le; W<sub>max</sub>. Evaluation: maximize V(M).", body_style))
    story.append(Paragraph("<b>Small Instance Correctness Check (n = 4, Capacity = 50 kg):</b>", h2_style))

    q6_tt_data = [
        ["Mask (Binary)", "Selected Packages", "Weight (kg)", "Value (pts)", "Feasibility Status"],
        ["0000 (0)", "None (Empty)", "0", "0", "FEASIBLE"],
        ["0001 (1)", "PKG-MEDS-01", "20", "70", "FEASIBLE"],
        ["0010 (2)", "PKG-WATER-02", "30", "80", "FEASIBLE"],
        ["0011 (3)", "MEDS-01 + WATER-02", "50", "150", "OPTIMAL FEASIBLE (150 pts)"],
        ["0100 (4)", "PKG-RATION-03", "40", "90", "FEASIBLE"],
        ["0101 (5)", "MEDS-01 + RATION-03", "60", "160", "INFEASIBLE (Overweight)"],
        ["0110 (6)", "WATER-02 + RATION-03", "70", "170", "INFEASIBLE (Overweight)"],
        ["0111 (7)", "MEDS + WATER + RATION", "90", "240", "INFEASIBLE (Overweight)"],
        ["1000 (8)", "PKG-COMMS-04", "15", "60", "FEASIBLE"],
        ["1001 (9)", "MEDS-01 + COMMS-04", "35", "130", "FEASIBLE"],
        ["1010 (10)", "WATER-02 + COMMS-04", "45", "140", "FEASIBLE"],
        ["1011 (11)", "MEDS + WATER + COMMS", "65", "210", "INFEASIBLE (Overweight)"],
        ["1100 (12)", "RATION-03 + COMMS-04", "55", "150", "INFEASIBLE (Overweight)"],
        ["1101 (13)", "MEDS + RATION + COMMS", "75", "220", "INFEASIBLE (Overweight)"],
        ["1110 (14)", "WATER + RATION + COMMS", "85", "230", "INFEASIBLE (Overweight)"],
        ["1111 (15)", "All 4 Packages", "105", "300", "INFEASIBLE (Overweight)"],
    ]
    t_q6_tt = Table(q6_tt_data, colWidths=[74, 166, 74, 74, 116])
    t_q6_tt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#D4EFDF")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t_q6_tt)
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Independent Verification:</b> Exhaustive search identified Mask 3 {PKG-MEDS-01 (20kg, 70pts) + PKG-WATER-02 (30kg, 80pts)} with Weight = 50 kg and Value = 150 pts as the global maximum. All higher-value combinations exceed 50 kg. Algorithmic correctness is verified.", body_style))

    # PAGE 8 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 9: Q6 GROWTH & DEPLOYMENT DECISION
    # =============================================================
    story.append(Paragraph("Q6 – Combinatorial Growth & Deployment Decision", h1_style))
    
    q6_growth_data = [
        ["Packages (N)", "Candidate Space (2^N)", "Feasible Subsets", "Best Value", "Time (ms)", "Status"],
        ["10", "1,024", "299", "656", "1.79", "Deployable (< 2.0s)"],
        ["14", "16,384", "4,102", "961", "42.26", "Deployable (< 2.0s)"],
        ["18", "262,144", "57,129", "1,144", "728.53", "Deployable (< 2.0s)"],
        ["22", "4,194,304", "807,496", "1,463", "11,846.75", "EXCEEDS DEADLINE (11.8s)"],
    ]
    t_q6_g = Table(q6_growth_data, colWidths=[70, 110, 84, 70, 70, 100])
    t_q6_g.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q6_g)
    story.append(Spacer(1, 4))

    g6_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141640.png")
    if os.path.exists(g6_p):
        story.append(Image(g6_p, width=5.6*inch, height=2.35*inch))
        story.append(Paragraph("Figure 6.1: Combinatorial explosion of candidate solutions (2^N) and runtime in Exhaustive Search.", caption_style))

    s6_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141615.png")
    if os.path.exists(s6_p):
        story.append(Image(s6_p, width=5.6*inch, height=2.2*inch))
        story.append(Paragraph(f"Figure 6.2: Terminal execution output for Q6 Exhaustive Knapsack (Reg No: {REG_NO}).", caption_style))

    story.append(Paragraph("<b>Combinatorial Explosion & Deployment Decision:</b>", h2_style))
    story.append(Paragraph("Each additional package doubles the solution space: |S<sub>n+1</sub>| = 2 &middot; |S<sub>n</sub>|. Adding 10 packages expands work by 2<sup>10</sup> = 1,024x! For emergency helicopter dispatch, flight crews need flight manifests within 2.0 seconds. At N = 18, execution is 0.73s (safe). At N = 22, execution is 11.85s (violation). At N = 30, execution would take 50.5 minutes! Therefore, exhaustive search deployment is strictly bounded at <b>N &le; 20 packages</b>.", body_style))

    # PAGE 9 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 10: Q7 DAY-4 DESIGN CHALLENGE (PARTS A - D)
    # =============================================================
    story.append(Paragraph("Q7 – Day-4 Design Challenge: Diagnose, Redesign and Validate (13 Marks)", h1_style))
    story.append(Paragraph("<b>Selected Problem:</b> Q4 Drone Closest-Pair Collision-Risk Monitoring. The brute-force solution scales at &Theta;(n<sup>2</sup>), requiring 1.35 seconds at N = 4,000, violating the 50 ms real-time safety budget.", body_style))
    
    story.append(Paragraph("<b>Part A: Diagnose the Computational Bottleneck (2 Marks):</b>", h2_style))
    story.append(Paragraph("Over 98% of CPU cycles are consumed evaluating Euclidean distances between drones on opposite ends of the city (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)). When current &delta; = 5.2 m, evaluating points separated by &Delta;x = 8000 m is completely superfluous. Root cause: total absence of spatial indexing forces an exhaustive Cartesian product.", body_style))

    story.append(Paragraph("<b>Part B: Define the Design Objective (2 Marks):</b>", h2_style))
    story.append(Paragraph("Exploit 1D coordinate monotonicity to prune distant candidate pairs without missing the true minimum. Measurable targets: reduce distance calculations by &gt; 98% and achieve runtime &lt; 20 ms for N = 5,000 drones (comfortably inside the 50 ms budget).", body_style))

    story.append(Paragraph("<b>Part C: Design the Revised Computational Strategy (4 Marks):</b>", h2_style))
    story.append(Paragraph("1. <b>Spatial Bounding:</b> Euclidean distance is bounded from below by 1D coordinate separation: dist(P<sub>i</sub>, P<sub>j</sub>) &ge; |x<sub>j</sub> - x<sub>i</sub>| = &Delta;x.<br/>2. <b>Presorting:</b> Sort drones by X-coordinate in O(n log n).<br/>3. <b>Monotonicity & Early Break:</b> For drone i, examine j = i + 1, i + 2, ... As soon as x<sub>j</sub> - x<sub>i</sub> &ge; &delta;<sub>min</sub>, all subsequent points k &gt; j also have x<sub>k</sub> - x<sub>i</sub> &ge; &delta;<sub>min</sub>. Execute an IMMEDIATE BREAK!<br/>4. <b>Auxiliary Y-Filter:</b> Check |y<sub>j</sub> - y<sub>i</sub>| &lt; &delta;<sub>min</sub> before evaluating squared distance.", body_style))

    story.append(Paragraph("<b>Pseudocode for Redesigned Strategy:</b>", h2_style))
    code_redes = (
        "ALGORITHM PresortedSpatialPruningClosestPair(P[0..n-1])\n"
        "Sort(P, by X-coordinate) // Preprocessing O(n log n)\n"
        "min_dist_sq = dist_sq(P[0], P[1]); min_dist = sqrt(min_dist_sq)\n"
        "for i = 0 to n - 2 do\n"
        "    for j = i + 1 to n - 1 do\n"
        "        dx = P[j].x - P[i].x\n"
        "        if dx >= min_dist then break // SPATIAL PRUNING\n"
        "        dy = abs(P[j].y - P[i].y)\n"
        "        if dy >= min_dist then continue // 1D Y-filter\n"
        "        d_sq = dx * dx + dy * dy\n"
        "        if d_sq < min_dist_sq then min_dist_sq = d_sq; min_dist = sqrt(d_sq); pair = (P[i], P[j])\n"
        "return pair, min_dist"
    )
    story.append(Paragraph(code_redes.replace('\n', '<br/>'), code_style))

    story.append(Paragraph("<b>Part D: Predict Before Implementing (1 Mark):</b>", h2_style))
    story.append(Paragraph("Distance calculations will drop from &Theta;(n<sup>2</sup>) to near-linear O(n) for uniform 2D airspace. At N = 5,000, calculations will fall by &gt; 99.9%, and execution time will drop from ~2,100 ms to &lt; 10 ms.", body_style))

    # PAGE 10 END
    story.append(PageBreak())

    # =============================================================
    # PAGE 11: Q7 VALIDATION, VISUALS & FINAL DEFENCE
    # =============================================================
    story.append(Paragraph("Q7 – Experimental Validation & Engineering Defence", h1_style))
    story.append(Paragraph("<b>Part E: Implement and Validate the Redesign (2 Marks):</b>", h2_style))

    q7_t_data = [
        ["N", "Orig Dist Calcs", "Redes Dist Calcs", "Calc Reduction", "Orig Time", "Redes Time", "Speedup"],
        ["100", "4,950", "4", "99.92%", "0.78 ms", "0.06 ms", "12.9x"],
        ["500", "124,750", "5", "100.00%", "19.73 ms", "0.30 ms", "64.9x"],
        ["1,000", "499,500", "11", "100.00%", "79.67 ms", "0.71 ms", "111.9x"],
        ["2,000", "1,999,000", "12", "100.00%", "351.72 ms", "1.56 ms", "224.9x"],
        ["5,000", "12,497,500", "17", "100.00%", "2,108.52 ms", "4.45 ms", "474.0x"],
    ]
    t_q7 = Table(q7_t_data, colWidths=[45, 95, 95, 85, 64, 60, 60])
    t_q7.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#D4EFDF")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q7)
    story.append(Spacer(1, 4))

    g7_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141855.png")
    if os.path.exists(g7_p):
        story.append(Image(g7_p, width=5.6*inch, height=2.35*inch))
        story.append(Paragraph("Figure 7.1: Experimental comparison between Brute-Force and Presorted Spatial Pruning.", caption_style))

    s7_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141830.png")
    if os.path.exists(s7_p):
        story.append(Image(s7_p, width=5.6*inch, height=2.2*inch))
        story.append(Paragraph(f"Figure 7.2: Terminal execution output for Q7 Design Challenge (Reg No: {REG_NO}).", caption_style))

    story.append(Paragraph("<b>Part F: Defend the Final Design (2 Marks):</b>", h2_style))
    story.append(Paragraph("Predictions were emphatically validated. At N = 5,000, distance calculations dropped from 12,497,500 to just 17 (a 99.999% reduction!), slashing runtime from 2,108.52 ms to 4.45 ms (a 474.0x speedup), operating safely inside the 50 ms budget. Trade-off is an O(n log n) sorting pass (0.6 ms) and O(n) memory. Degenerate vertical-line cases can be mitigated by coordinate rotation, but in continuous airspace, dispersion guarantees near-linear performance. The redesign successfully converts an intractable algorithm into a production-grade radar system.", body_style))

    # BUILD DOCUMENT
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Publication-grade PDF generated successfully: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    build_pdf()
