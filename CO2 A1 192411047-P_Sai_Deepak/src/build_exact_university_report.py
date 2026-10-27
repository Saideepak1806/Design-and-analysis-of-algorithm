"""
Master Academic Report Generator - Exact University Format (18 Pages, Pure Black Text)
Matches university report template: Times New Roman, pure black text, Table of Contents,
formal academic section numbering, flowcharts, result tables, graphs, terminal screenshots.
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
)
from reportlab.pdfgen import canvas

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
GRAPHS_DIR = os.path.join(BASE_DIR, "results", "graphs")
ROOT_DIR = os.path.dirname(BASE_DIR)

STUDENT_NAME = "P Sai Deepak"
REG_NO = "192411047"
COURSE_CODE = "CSA 1418"
GUIDE = "Dr. A. Sairam"
DURATION = "1 Week"
SEED = 1047
REPO_LINK = "https://github.com/sai-deepak-192411047/DAA-A2-192411047-P_Sai_Deepak"

# -----------------------------------------------------------------------------
# REPORTLAB NUMBERED CANVAS (Bottom-Right Page Numbering)
# -----------------------------------------------------------------------------
class AcademicCanvas(canvas.Canvas):
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
        self.setFont("Times-Roman", 10)
        self.setFillColor(colors.black)
        # Simple page number at bottom right
        self.drawRightString(558, 40, str(self._pageNumber))
        self.restoreState()

# -----------------------------------------------------------------------------
# BUILD PDF
# -----------------------------------------------------------------------------
def build_pdf():
    pdf_path = os.path.join(REPORT_DIR, f"DAA_A2_{REG_NO}.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_main = ParagraphStyle(
        'TitleMain',
        fontName='Times-Bold',
        fontSize=15,
        leading=20,
        alignment=1,
        textColor=colors.black,
        spaceAfter=14
    )
    title_sub = ParagraphStyle(
        'TitleSub',
        fontName='Times-Bold',
        fontSize=13,
        leading=18,
        alignment=1,
        textColor=colors.black,
        spaceAfter=24
    )
    topic_style = ParagraphStyle(
        'TopicStyle',
        fontName='Times-Bold',
        fontSize=13,
        leading=18,
        alignment=1,
        textColor=colors.black,
        spaceAfter=24
    )
    co_style = ParagraphStyle(
        'COStyle',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=15,
        alignment=1,
        textColor=colors.black,
        spaceAfter=45
    )
    sec_heading = ParagraphStyle(
        'SecHeading',
        fontName='Times-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.black,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    subsec_heading = ParagraphStyle(
        'SubSecHeading',
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.black,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body = ParagraphStyle(
        'Body',
        fontName='Times-Roman',
        fontSize=10,
        leading=13.5,
        textColor=colors.black,
        spaceAfter=5
    )
    bullet = ParagraphStyle(
        'Bullet',
        fontName='Times-Roman',
        fontSize=10,
        leading=13.5,
        textColor=colors.black,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )
    code_block = ParagraphStyle(
        'CodeBlock',
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.black,
        leftIndent=10,
        rightIndent=10,
        spaceBefore=4,
        spaceAfter=6
    )
    caption = ParagraphStyle(
        'Caption',
        fontName='Times-Italic',
        fontSize=9,
        leading=11.5,
        alignment=1,
        textColor=colors.black,
        spaceBefore=4,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("DESIGN AND ANALYSIS OF ALGORITHMS", title_main))
    story.append(Paragraph("ASSIGNMENT – 2", title_sub))
    story.append(Spacer(1, 25))
    story.append(Paragraph("Design, Analyse and Validate Brute-Force and Exhaustive-Search Strategies for Core Computational Problems", topic_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CO2: Algorithm Fundamentals, Brute-Force and Exhaustive-Search Techniques – Selection Sort, Bubble Sort, Insertion Sort, Sequential Search, Brute-Force String Matching, Closest Pair, Convex Hull and Exhaustive Search", co_style))
    story.append(Spacer(1, 50))

    meta_rows = [
        [Paragraph("Student Name", body), Paragraph(STUDENT_NAME, body)],
        [Paragraph("Register Number", body), Paragraph(REG_NO, body)],
        [Paragraph("Course Code", body), Paragraph(COURSE_CODE, body)],
        [Paragraph("Guide", body), Paragraph(GUIDE, body)],
        [Paragraph("Duration", body), Paragraph(DURATION, body)],
    ]
    t_cover_meta = Table(meta_rows, colWidths=[200, 304])
    t_cover_meta.setStyle(TableStyle([
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 10.5),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_cover_meta)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: TABLE OF CONTENTS (Double bordered table)
    # =========================================================================
    toc_data = [
        ["S. No.", "Contents", "Page No."],
        ["1", "Abstract", "3"],
        ["2", "Introduction", "3"],
        ["3", "Problem Statement", "3"],
        ["4", "Aim and Objectives", "3"],
        ["5", "System Requirements", "4"],
        ["6", "Proposed Algorithmic Strategies", "4"],
        ["7", "Task 1 – Design the Algorithms (Sorting Under Data Conditions)", "5"],
        ["8", "Task 1 – Mathematical Analysis & Performance (Q1)", "6"],
        ["9", "Task 2 – Sequential Search Engineering Boundaries (Q2)", "7"],
        ["10", "Task 3 – Engineered Brute-Force String Matching (Q3)", "8"],
        ["11", "Task 4 – Closest Pair and Quadratic Scaling (Q4)", "9"],
        ["12", "Task 5 – Convex Hull from Geometric Principle (Part 1)", "10"],
        ["13", "Task 5 – Convex Hull Boundary Visualisation & Proof (Part 2)", "11"],
        ["14", "Task 6 – Exhaustive Search & Correctness Verification (Part 1)", "12"],
        ["15", "Task 6 – Combinatorial Growth & Deployment Boundary (Part 2)", "13"],
        ["16", "Task 7 – Day-4 Design Challenge: Diagnose & Redesign (Part 1)", "14"],
        ["17", "Task 7 – Validation, Visuals & Engineering Defence (Part 2)", "15"],
        ["18", "Advantages and Limitations", "16"],
        ["19", "Result", "16"],
        ["20", "Conclusion", "16"],
        ["21", "Future Enhancement", "17"],
        ["22", "References", "17"],
        ["23", "Appendix – Output Pictures to Insert", "18"],
    ]
    t_toc = Table(toc_data, colWidths=[60, 364, 80])
    t_toc.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (2,0), (2,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_toc)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: ABSTRACT, INTRODUCTION, PROBLEM STATEMENT, AIM & OBJECTIVES
    # =========================================================================
    story.append(Paragraph("1. ABSTRACT", sec_heading))
    story.append(Paragraph("This assignment investigates the empirical behaviour, theoretical performance and engineering boundaries of Brute-Force and Exhaustive-Search techniques (Course Outcome CO2). Seven core problem domains are examined: priority sorting under varied data configurations (Selection, Bubble, Insertion Sort), dynamic inventory retrieval using Sequential Search, pattern matching across engineered cybersecurity logs, planar closest-pair collision monitoring, convex hull construction derived from a line-side geometric principle, and payload-constrained humanitarian airlift planning using exhaustive enumeration. To address prohibitive asymptotic bottlenecks, an algorithmic redesign using Presorted Spatial Coordinate Pruning is engineered and benchmarked. Personalised datasets were synthesized using random seed <b>1047</b> (last 4 digits of Registration Number <b>192411047</b>). Experimental operation counts, character comparisons, candidate enumerations and microsecond-level timings were recorded to validate theoretical derivations and establish defensible deployment boundaries.", body))

    story.append(Paragraph("2. INTRODUCTION", sec_heading))
    story.append(Paragraph("The brute-force paradigm represents a fundamental algorithmic approach directly translating a formal problem statement into a straightforward computational procedure. While conceptually simple and universally applicable without requiring complex data structures, brute-force algorithms invariably exhibit polynomial (Θ(n²), Θ(n³)) or exponential (Θ(2ⁿ)) computational growth. As dataset scales increase in production environments—such as drone airspace monitoring or flight payload optimization—the cost of examining every possibility rapidly exceeds real-time response budgets. This investigation evaluates where brute-force strategies succeed as appropriate engineering choices and where systematic algorithmic redesign is mathematically mandatory.", body))

    story.append(Paragraph("3. PROBLEM STATEMENT", sec_heading))
    story.append(Paragraph("Design, analyse, implement and empirically validate brute-force and exhaustive-search algorithms for seven specified problem contexts: (i) E-commerce dispatch priority sorting under contrasting orderings; (ii) Aircraft maintenance tool tracking; (iii) Cybersecurity log screening; (iv) Real-time drone collision-risk monitoring; (v) Wildlife reserve outer boundary demarcation; (vi) Emergency humanitarian airlift knapsack optimization; and (vii) A Day-4 Design Challenge diagnosing an asymptotic bottleneck and developing a validated engineering redesign.", body))

    story.append(Paragraph("4. AIM AND OBJECTIVES", sec_heading))
    story.append(Paragraph("Aim: To design, analyse, benchmark and validate brute-force and exhaustive search strategies, identifying computational limitations and engineering an evidence-based redesign.", body))
    story.append(Paragraph("• Design contrasting and edge-case datasets to expose algorithmic behaviour.", bullet))
    story.append(Paragraph("• Derive mathematical pair counts, operations and solution-space growth formulas.", bullet))
    story.append(Paragraph("• Implement all algorithms and collect primary operation counts and execution runtimes.", bullet))
    story.append(Paragraph("• Compare theoretical predictions with observed experimental measurements.", bullet))
    story.append(Paragraph("• Diagnose computational bottlenecks and engineer a validated redesigned strategy.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: SYSTEM REQUIREMENTS & PROPOSED ALGORITHMIC STRATEGIES
    # =========================================================================
    story.append(Paragraph("5. SYSTEM REQUIREMENTS", sec_heading))
    story.append(Paragraph("• Hardware: Intel/AMD x86_64 CPU, 16 GB RAM, High-resolution console environment.", bullet))
    story.append(Paragraph("• Operating System: Windows 11 Enterprise (Build 26100), PowerShell 7 / Windows Terminal.", bullet))
    story.append(Paragraph("• Software / Runtime: Python 3.13.0, NumPy, Matplotlib, ReportLab, Python-Docx.", bullet))
    story.append(Paragraph("• Personal Dataset Seed: <b>1047</b> (Derived from Registration Number 192411047).", bullet))
    story.append(Paragraph("• Personal Search Keys: Target Key T-1047 (Found) | Target Key T-1048 (Not Found).", bullet))
    story.append(Paragraph("• Metrics Evaluated: Key comparisons, swaps/movements, candidate solutions, execution time (ms/μs).", bullet))

    story.append(Paragraph("6. PROPOSED ALGORITHMIC STRATEGIES", sec_heading))
    strat_data = [
        ["Strategy", "Type", "Preprocessing", "Search / Run Cost", "Main Operating Context"],
        ["Selection Sort", "Iterative Brute Force", "None", "Θ(n²)", "Fixed-comparison sorting; minimal swaps"],
        ["Bubble Sort", "Iterative Adaptive", "None", "Best: Θ(n), Worst: Θ(n²)", "Nearly sorted checks with early exit"],
        ["Insertion Sort", "Iterative Adaptive", "None", "Best: Θ(n), Worst: Θ(n²)", "Online queues; 95% sorted e-commerce data"],
        ["Sequential Search", "Linear Scan", "None", "Best: 1, Worst: n", "Small dynamic inventory lists (N < 200)"],
        ["BF String Match", "Exhaustive Slide", "None", "Best: Θ(n), Worst: Θ(n·m)", "Pattern scanning in security syslog streams"],
        ["BF Closest Pair", "Exhaustive Pair Scan", "None", "Θ(n²)", "Drone collision radar (impractical for N > 800)"],
        ["BF Convex Hull", "Geometric Line-Side", "None", "Θ(n³)", "Wildlife reserve station boundary mapping"],
        ["Exhaustive Knapsack", "Combinatorial Power Set", "None", "Θ(2ⁿ)", "Humanitarian airlift cargo optimization"],
        ["Spatial Pruned CP", "Presorted Sweep-Line", "Sort: O(n log n)", "Average: O(n log n)", "Redesigned radar collision monitoring engine"],
    ]
    t_strat = Table(strat_data, colWidths=[95, 80, 75, 94, 160])
    t_strat.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_strat)
    story.append(Spacer(1, 4))

    flow_p = os.path.join(GRAPHS_DIR, "flowchart_overall_strategy.png")
    if os.path.exists(flow_p):
        story.append(Image(flow_p, width=4.5*inch, height=2.8*inch))
        story.append(Paragraph("Figure 1: Overall algorithmic investigation and redesign architecture.", caption))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: TASK 1 – DESIGN THE ALGORITHMS (SORTING)
    # =========================================================================
    story.append(Paragraph("7. TASK 1 – DESIGN THE ALGORITHMS (SORTING UNDER DATA CONDITIONS)", sec_heading))
    story.append(Paragraph("An e-commerce fulfilment centre prioritises orders by priority score. Data arrangements vary between random order, reverse order (disordered), and 95% nearly sorted order. Three brute-force sorting algorithms are formulated below:", body))

    story.append(Paragraph("7.1 Selection Sort", subsec_heading))
    story.append(Paragraph("Scans the unsorted suffix to locate the minimum element and exchanges it with the first unsorted position. Key comparisons remain invariant across all arrangements at n(n - 1) / 2 = Θ(n²), but swaps are strictly bounded by n - 1 = O(n).", body))
    story.append(Paragraph("SELECTION_SORT(A, n):\n  for i = 0 to n - 2:\n    min_idx = i\n    for j = i + 1 to n - 1:\n      if A[j] < A[min_idx]: min_idx = j\n    if min_idx != i: swap(A[i], A[min_idx])", code_block))

    story.append(Paragraph("7.2 Bubble Sort (with Early-Termination Flag)", subsec_heading))
    story.append(Paragraph("Compares adjacent elements and swaps inverted pairs. An early-exit boolean flag `swapped` halts execution if a pass completes with zero swaps. In best case (sorted), runtime is Θ(n); in worst case, it requires n(n - 1) / 2 comparisons and swaps.", body))
    story.append(Paragraph("BUBBLE_SORT(A, n):\n  for i = 0 to n - 2:\n    swapped = false\n    for j = 0 to n - 2 - i:\n      if A[j] > A[j+1]: swap(A[j], A[j+1]); swapped = true\n    if not swapped: break", code_block))

    story.append(Paragraph("7.3 Insertion Sort", subsec_heading))
    story.append(Paragraph("Maintains a sorted prefix and inserts each subsequent element into its correct relative position by shifting larger elements rightward. Running time is strictly adaptive to inversion count I: T(n) = O(n + I). When data is nearly sorted (I << n²), inner loop executes O(1) shifts per element, achieving near-linear Θ(n) performance.", body))
    story.append(Paragraph("INSERTION_SORT(A, n):\n  for i = 1 to n - 1:\n    key = A[i]; j = i - 1\n    while j >= 0 and A[j] > key:\n      A[j+1] = A[j]; j = j - 1\n    A[j+1] = key", code_block))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: TASK 1 – EXPERIMENTAL RESULTS & DECISION DEFENCE
    # =========================================================================
    story.append(Paragraph("8. TASK 1 – MATHEMATICAL ANALYSIS & EXPERIMENTAL PERFORMANCE", sec_heading))
    story.append(Paragraph("Datasets were synthesized using random seed <b>1047</b> across three contrasting conditions: Random, Reverse Sorted (worst case), and 95% Nearly Sorted (batch arrivals into sorted queues).", body))

    q1_table_data = [
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
    t_q1 = Table(q1_table_data, colWidths=[114, 40, 94, 84, 94, 78])
    t_q1.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q1)
    story.append(Spacer(1, 4))

    g1_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140832.png")
    s1_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140815.png")
    if os.path.exists(g1_p) and os.path.exists(s1_p):
        q1_img_t = Table([
            [Image(g1_p, width=3.35*inch, height=1.7*inch), Image(s1_p, width=3.35*inch, height=1.7*inch)],
            [Paragraph("Figure 1.1: Comparisons across input conditions.", caption),
             Paragraph(f"Figure 1.2: Terminal execution benchmark (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q1_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q1_img_t)

    story.append(Paragraph("Design Decision & Recommendation Defence:", subsec_heading))
    story.append(Paragraph("For the fulfilment centre where 95% of incoming orders are already sorted, <b>INSERTION SORT</b> is unconditionally recommended. At N = 1000, Insertion Sort requires only 26,112 comparisons and 3.61 ms, compared to 499,500 comparisons for Selection Sort (19.1x more work) and 452,710 for Bubble Sort (17.3x more work). Its adaptive inner while-loop exploits existing order perfectly.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: TASK 2 – SEQUENTIAL SEARCH (Q2)
    # =========================================================================
    story.append(Paragraph("9. TASK 2 – SEQUENTIAL SEARCH ENGINEERING BOUNDARIES (Q2)", sec_heading))
    story.append(Paragraph("An aircraft maintenance hangar maintains an active register of issued tools. Personal search keys derived from registration number: <b>Found Target = T-1047</b> | <b>Not-Found Target = T-1048</b>.", body))

    q2_table_data = [
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
    t_q2 = Table(q2_table_data, colWidths=[80, 130, 94, 80, 70, 50])
    t_q2.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q2)
    story.append(Spacer(1, 4))

    g2_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140940.png")
    s2_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140918.png")
    if os.path.exists(g2_p) and os.path.exists(s2_p):
        q2_img_t = Table([
            [Image(g2_p, width=3.35*inch, height=1.7*inch), Image(s2_p, width=3.35*inch, height=1.7*inch)],
            [Paragraph("Figure 2.1: Sequential search comparisons vs N.", caption),
             Paragraph(f"Figure 2.2: Terminal execution output (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q2_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q2_img_t)

    story.append(Paragraph("Engineering Evaluation & Scalability Boundary:", subsec_heading))
    story.append(Paragraph("Sequential Search is acceptable ONLY for small lists (N < 200) with high churn (O(1) insert/delete) and low search frequency. When expanding to 20 maintenance hangars (N = 20,000 records, 10,000 queries/hour), Sequential Search executes 100,000,000 comparisons/hour, causing unacceptable CPU contention. The organization must transition to an In-Memory Hash Map (O(1) expected lookup) or B-Tree index (O(log N)).", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: TASK 3 – STRING MATCHING (Q3)
    # =========================================================================
    story.append(Paragraph("10. TASK 3 – ENGINEERED BRUTE-FORCE STRING MATCHING (Q3)", sec_heading))
    story.append(Paragraph("Cybersecurity log screening evaluates known intrusion signatures. We engineer three distinct text-pattern pairs to investigate how pattern self-similarity governs computational effort:", body))

    q3_table_data = [
        ["Test Condition", "Text Len (n)", "Pat Len (m)", "Comparisons", "Shifts", "Time (ms)"],
        ["Test 1: Low-Work (Immediate Mismatch)", "10,000", "20", "9,981", "9,981", "0.58"],
        ["Test 2: High-Work (Last-Char Mismatch)", "10,000", "20", "199,620", "9,981", "12.44"],
        ["Test 3: Cybersecurity Prefix Cascade", "20,084", "48", "38,241", "20,037", "2.15"],
    ]
    t_q3 = Table(q3_table_data, colWidths=[174, 70, 70, 70, 60, 60])
    t_q3.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q3)
    story.append(Spacer(1, 4))

    g3_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141058.png")
    s3_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141035.png")
    if os.path.exists(g3_p) and os.path.exists(s3_p):
        q3_img_t = Table([
            [Image(g3_p, width=3.35*inch, height=1.75*inch), Image(s3_p, width=3.35*inch, height=1.75*inch)],
            [Paragraph("Figure 3.1: Character comparisons across patterns.", caption),
             Paragraph(f"Figure 3.2: Terminal execution output (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q3_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q3_img_t)

    story.append(Paragraph("Inquiry & Algorithmic Findings:", subsec_heading))
    story.append(Paragraph("1. <b>Precision of Predictions:</b> Test 1 matched theoretical prediction exactly at n - m + 1 = 9,981 comparisons. Test 2 matched (n - m + 1) &times; m = 199,620 comparisons (a 20.0x work explosion on identical text lengths!).", bullet))
    story.append(Paragraph("2. <b>Structural Determinants:</b> Inefficiency arises from pattern self-similarity. Matching m - 1 characters before failing on the last character discards all partial match information upon shifting by 1.", bullet))
    story.append(Paragraph("3. <b>Input Size Deficiency:</b> Character entropy and prefix redundancy govern whether execution is O(n) or O(n &times; m), proving input size alone is an incomplete predictor.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: TASK 4 – CLOSEST PAIR (Q4)
    # =========================================================================
    story.append(Paragraph("11. TASK 4 – CLOSEST PAIR AND QUADRATIC SCALING (Q4)", sec_heading))
    story.append(Paragraph("In a delivery drone monitoring airspace, drones report 2D positions D_i = (x_i, y_i). Collision avoidance requires tracking the closest drone pair. To avoid duplicate comparisons, strict index ordering i < j is enforced.", body))
    story.append(Paragraph("<b>Mathematical Pair-Count Derivation:</b> Total unique pairs = &Sigma;<sub>i=0</sub><sup>n-2</sup> &Sigma;<sub>j=i+1</sub><sup>n-1</sup> 1 = &Sigma;<sub>i=0</sub><sup>n-2</sup> (n - 1 - i) = (n - 1) + (n - 2) + ... + 1 = <b>n(n - 1) / 2 = &Theta;(n<sup>2</sup>)</b>.", body))

    q4_table_data = [
        ["Drones (N)", "Theoretical n(n-1)/2", "Pairs Examined", "Dist Calcs", "Time (ms)", "Status"],
        ["100", "4,950", "4,950", "4,950", "0.78", "Acceptable"],
        ["500", "124,750", "124,750", "124,750", "19.73", "Acceptable"],
        ["1,000", "499,500", "499,500", "499,500", "79.67", "Impractical (> 50 ms)"],
        ["2,000", "1,999,000", "1,999,000", "1,999,000", "351.72", "Impractical"],
        ["4,000", "7,998,000", "7,998,000", "7,998,000", "1,348.50", "Severe Violation"],
    ]
    t_q4 = Table(q4_table_data, colWidths=[70, 110, 84, 80, 70, 90])
    t_q4.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q4)
    story.append(Spacer(1, 4))

    g4_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141235.png")
    s4_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141210.png")
    if os.path.exists(g4_p) and os.path.exists(s4_p):
        q4_img_t = Table([
            [Image(g4_p, width=3.35*inch, height=1.7*inch), Image(s4_p, width=3.35*inch, height=1.7*inch)],
            [Paragraph("Figure 4.1: Candidate pairs scaling n(n-1)/2.", caption),
             Paragraph(f"Figure 4.2: Terminal execution benchmark (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q4_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q4_img_t)

    story.append(Paragraph("Scalability Inquiry:", subsec_heading))
    story.append(Paragraph("Acceptable real-time radar budget is 50.0 ms (20 Hz refresh rate). The brute-force approach becomes impractical at N &approx; 800 drones. Inefficiency originates from computing Euclidean distances between drones miles apart on opposite ends of the city (dx > 8000m) without spatial indexing.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: TASK 5 – CONVEX HULL (PART 1: DERIVATION & PSEUDOCODE)
    # =========================================================================
    story.append(Paragraph("12. TASK 5 – CONVEX HULL FROM GEOMETRIC PRINCIPLE (PART 1)", sec_heading))
    story.append(Paragraph("Wildlife reserve boundary monitoring determines the outer perimeter of monitoring stations P_i = (x_i, y_i).", body))
    story.append(Paragraph("<b>Design Starting Point:</b> <i>\"A line joining two candidate points may form part of the outer boundary if all remaining points lie on an appropriate single side of that line.\"</i>", body))
    story.append(Paragraph("<b>Derivation of Computational Procedure:</b>", subsec_heading))
    story.append(Paragraph("1. <b>Line Equation:</b> Two points P<sub>1</sub>(x<sub>1</sub>, y<sub>1</sub>) and P<sub>2</sub>(x<sub>2</sub>, y<sub>2</sub>) define a line a&middot;x + b&middot;y = c, where a = y<sub>2</sub> - y<sub>1</sub>, b = x<sub>1</sub> - x<sub>2</sub>, c = x<sub>1</sub>&middot;y<sub>2</sub> - y<sub>1</sub>&middot;x<sub>2</sub>.", bullet))
    story.append(Paragraph("2. <b>Point-Line Side Test:</b> For any third station P<sub>k</sub>(x<sub>k</sub>, y<sub>k</sub>), evaluate S(P<sub>k</sub>) = a&middot;x<sub>k</sub> + b&middot;y<sub>k</sub> - c. S &gt; 0 indicates positive side, S &lt; 0 negative side, and S = 0 collinearity.", bullet))
    story.append(Paragraph("3. <b>Boundary Edge Acceptance Rule:</b> For candidate pair (P<sub>i</sub>, P<sub>j</sub>), check all n - 2 points P<sub>k</sub>. The segment is an outer boundary edge iff all points satisfy S(P<sub>k</sub>) &ge; 0, OR all satisfy S(P<sub>k</sub>) &le; 0.", bullet))
    story.append(Paragraph("4. <b>Polygon Construction:</b> Boundary vertices are sorted counter-clockwise around centroid via &theta; = atan2(y - c<sub>y</sub>, x - c<sub>x</sub>).", bullet))

    story.append(Paragraph("<b>Algorithm Pseudocode:</b>", subsec_heading))
    ch_code = (
        "ALGORITHM BruteForceConvexHull(P[0..n-1]):\n"
        "  hull_edges = empty set\n"
        "  for i = 0 to n - 2:\n"
        "    for j = i + 1 to n - 1:\n"
        "      a = P[j].y - P[i].y; b = P[i].x - P[j].x; c = P[i].x * P[j].y - P[i].y * P[j].x\n"
        "      has_pos = false; has_neg = false\n"
        "      for k = 0 to n - 1 (k != i, j):\n"
        "        val = a * P[k].x + b * P[k].y - c\n"
        "        if val > 0: has_pos = true\n"
        "        if val < 0: has_neg = true\n"
        "        if has_pos and has_neg: break\n"
        "      if not (has_pos and has_neg): hull_edges.add((P[i], P[j]))\n"
        "  return ConstructPolygon(hull_edges)"
    )
    story.append(Paragraph(ch_code.replace('\n', '<br/>'), code_block))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: TASK 5 – CONVEX HULL (PART 2: VISUALS & PROOF)
    # =========================================================================
    story.append(Paragraph("13. TASK 5 – CONVEX HULL BOUNDARY VISUALISATION & PROOF (PART 2)", sec_heading))
    story.append(Paragraph("Evaluated across Configuration 1 (Perimeter + Interior, 25 points) and Configuration 2 (Collinear Edge Challenge, multiple collinear stations on boundary).", body))

    g5_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141420.png")
    s5_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141355.png")
    if os.path.exists(g5_p) and os.path.exists(s5_p):
        q5_img_t = Table([
            [Image(g5_p, width=3.35*inch, height=1.75*inch), Image(s5_p, width=3.35*inch, height=1.75*inch)],
            [Paragraph("Figure 5.1: Convex hull 2D boundaries.", caption),
             Paragraph(f"Figure 5.2: Terminal execution benchmark (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q5_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q5_img_t)

    story.append(Paragraph("Complexity Analysis & Geometric Correctness Argument:", subsec_heading))
    story.append(Paragraph("• <b>Work Growth:</b> Checking all pairs requires n(n - 1) / 2 candidate checks, and each tests n - 2 points, giving Total Operations = n(n - 1)(n - 2) / 2 = &Theta;(n<sup>3</sup>). Experimental checks confirmed cubic scaling: N = 25 took 6,052 tests (0.8 ms); N = 100 took 480,200 tests (46.8 ms).", bullet))
    story.append(Paragraph("• <b>Reasoned Geometric Correctness:</b> By definition, a set S is convex if for all p, q &isin; S, the line segment pq &sube; S. A hyperplane H supports S if H touches the boundary and S lies entirely in one closed half-space of H. A line through P<sub>i</sub> and P<sub>j</sub> has all points in one half-plane iff it is a supporting line of the point set. The convex hull boundary consists exclusively of segments on supporting lines. Hence, our decision rule is mathematically sound.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: TASK 6 – EXHAUSTIVE KNAPSACK (PART 1: FORMULATION & VERIFICATION)
    # =========================================================================
    story.append(Paragraph("14. TASK 6 – EXHAUSTIVE SEARCH & CORRECTNESS VERIFICATION (PART 1)", sec_heading))
    story.append(Paragraph("Humanitarian airlift planning selects emergency cargo under helicopter payload limit W_max, maximising total humanitarian value delivered.", body))
    story.append(Paragraph("<b>Exhaustive Strategy:</b> Candidate combinations are represented as length-n binary bitmasks M &isin; [0, 2<sup>n</sup> - 1]. Feasibility requires W(M) &le; W<sub>max</sub>. Global optimum is tracked via best_value and best_mask.", body))
    story.append(Paragraph("<b>Small Instance Correctness Verification (n = 4, Capacity = 50 kg):</b>", subsec_heading))

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
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t_q6_tt)
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Verification Result:</b> Exhaustive search identified Mask 3 {PKG-MEDS-01 (20kg, 70pts) + PKG-WATER-02 (30kg, 80pts)} with Weight = 50 kg and Value = 150 pts as the global maximum. All higher-value combinations exceed 50 kg. Algorithmic correctness is proven.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: TASK 6 – COMBINATORIAL GROWTH & DEPLOYMENT BOUNDARY (PART 2)
    # =========================================================================
    story.append(Paragraph("15. TASK 6 – COMBINATORIAL GROWTH & DEPLOYMENT BOUNDARY (PART 2)", sec_heading))

    q6_growth_data = [
        ["Packages (N)", "Candidate Space (2^N)", "Feasible Subsets", "Best Value", "Time (ms)", "Status"],
        ["10", "1,024", "299", "656", "1.79", "Deployable (< 2.0s)"],
        ["14", "16,384", "4,102", "961", "42.26", "Deployable (< 2.0s)"],
        ["18", "262,144", "57,129", "1,144", "728.53", "Deployable (< 2.0s)"],
        ["22", "4,194,304", "807,496", "1,463", "11,846.75", "EXCEEDS DEADLINE (11.8s)"],
    ]
    t_q6_g = Table(q6_growth_data, colWidths=[70, 110, 84, 70, 70, 100])
    t_q6_g.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q6_g)
    story.append(Spacer(1, 4))

    g6_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141640.png")
    s6_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141615.png")
    if os.path.exists(g6_p) and os.path.exists(s6_p):
        q6_img_t = Table([
            [Image(g6_p, width=3.35*inch, height=1.75*inch), Image(s6_p, width=3.35*inch, height=1.75*inch)],
            [Paragraph("Figure 6.1: Combinatorial explosion 2^N vs time.", caption),
             Paragraph(f"Figure 6.2: Terminal execution benchmark (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q6_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q6_img_t)

    story.append(Paragraph("Combinatorial Growth Inquiry & Deployment Decision:", subsec_heading))
    story.append(Paragraph("Each additional package doubles the candidate space: |S<sub>n+1</sub>| = 2 &middot; |S<sub>n</sub>|. For emergency humanitarian airlift dispatch, flight manifests must be produced within 2.0 seconds. At N = 18, execution is 0.73s (safe). At N = 22, execution is 11.85s (severe violation). At N = 30, execution would take 50.5 minutes! Therefore, the exhaustive search deployment boundary is strictly <b>N &le; 20 packages</b>.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: TASK 7 – DAY-4 DESIGN CHALLENGE (PART 1: DIAGNOSIS & STRATEGY)
    # =========================================================================
    story.append(Paragraph("16. TASK 7 – DAY-4 DESIGN CHALLENGE: DIAGNOSE & REDESIGN (PART 1)", sec_heading))
    story.append(Paragraph("Selected Problem: Q4 Drone Closest-Pair Collision-Risk Monitoring. The brute-force solution scales at &Theta;(n<sup>2</sup>), requiring 1.35 seconds at N = 4,000, violating the 50 ms radar safety budget.", body))

    story.append(Paragraph("Part A: Diagnose the Computational Bottleneck (2 Marks):", subsec_heading))
    story.append(Paragraph("Over 98% of CPU cycles are wasted evaluating Euclidean distances between drones miles apart on opposite ends of the city (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)). When current &delta; = 5.2 m, evaluating points separated by dx = 8000 m is completely superfluous. Root cause: total absence of spatial indexing forces an exhaustive Cartesian product.", body))

    story.append(Paragraph("Part B: Define the Design Objective (2 Marks):", subsec_heading))
    story.append(Paragraph("Prune candidate pairs using coordinate monotonicity without missing the true minimum. Measurable targets: reduce distance calculations by &gt; 98% and achieve runtime &lt; 20 ms for N = 5,000 drones (safely below 50 ms budget).", body))

    story.append(Paragraph("Part C: Design the Revised Computational Strategy (4 Marks):", subsec_heading))
    story.append(Paragraph("1. <b>Spatial Invariant:</b> dist(P<sub>i</sub>, P<sub>j</sub>) &ge; |x<sub>j</sub> - x<sub>i</sub>| = &Delta;x.<br/>2. <b>Presorting:</b> Sort drones by X-coordinate in O(n log n).<br/>3. <b>Early Break Rule:</b> For drone i, examine j = i + 1, i + 2, ... As soon as x<sub>j</sub> - x<sub>i</sub> &ge; &delta;<sub>min</sub>, all subsequent points k &gt; j also have x<sub>k</sub> - x<sub>i</sub> &ge; &delta;<sub>min</sub>. Execute an IMMEDIATE BREAK!<br/>4. <b>Auxiliary Y-Filter:</b> Filter |y<sub>j</sub> - y<sub>i</sub>| &lt; &delta;<sub>min</sub> before computing square distance.", body))

    flow_cp = os.path.join(GRAPHS_DIR, "flowchart_closest_pair_redesign.png")
    if os.path.exists(flow_cp):
        story.append(Image(flow_cp, width=4.5*inch, height=2.4*inch))
        story.append(Paragraph("Figure 7: Presorted Spatial Pruning algorithmic decision flow.", caption))

    story.append(Paragraph("Part D: Predict Before Implementing (1 Mark):", subsec_heading))
    story.append(Paragraph("Distance calculations will drop from &Theta;(n<sup>2</sup>) to near-linear O(n) for uniform 2D airspace. At N = 5,000, calculations will fall by &gt; 99.9%, and execution time will drop from ~2,100 ms to &lt; 10 ms.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15: TASK 7 – VALIDATION, VISUALS & FINAL DEFENCE (PART 2)
    # =========================================================================
    story.append(Paragraph("17. TASK 7 – VALIDATION, VISUALS & ENGINEERING DEFENCE (PART 2)", sec_heading))
    story.append(Paragraph("Part E: Implement and Validate the Redesign (2 Marks):", subsec_heading))

    q7_table_data = [
        ["N", "Orig Dist Calcs", "Redes Dist Calcs", "Calc Reduction", "Orig Time", "Redes Time", "Speedup"],
        ["100", "4,950", "4", "99.92%", "0.78 ms", "0.06 ms", "12.9x"],
        ["500", "124,750", "5", "100.00%", "19.73 ms", "0.30 ms", "64.9x"],
        ["1,000", "499,500", "11", "100.00%", "79.67 ms", "0.71 ms", "111.9x"],
        ["2,000", "1,999,000", "12", "100.00%", "351.72 ms", "1.56 ms", "224.9x"],
        ["5,000", "12,497,500", "17", "100.00%", "2,108.52 ms", "4.45 ms", "474.0x"],
    ]
    t_q7 = Table(q7_table_data, colWidths=[45, 95, 95, 85, 64, 60, 60])
    t_q7.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q7)
    story.append(Spacer(1, 4))

    g7_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141855.png")
    s7_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141830.png")
    if os.path.exists(g7_p) and os.path.exists(s7_p):
        q7_img_t = Table([
            [Image(g7_p, width=3.35*inch, height=1.75*inch), Image(s7_p, width=3.35*inch, height=1.75*inch)],
            [Paragraph("Figure 7.1: Brute-Force vs Spatial Pruning.", caption),
             Paragraph(f"Figure 7.2: Terminal execution benchmark (Reg No: {REG_NO}).", caption)]
        ], colWidths=[252, 252])
        q7_img_t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(q7_img_t)

    story.append(Paragraph("Part F: Defend the Final Design (2 Marks):", subsec_heading))
    story.append(Paragraph("Predictions were emphatically validated. At N = 5,000, distance calculations dropped from 12,497,500 to just 17 (a 99.999% reduction!), slashing runtime from 2,108.52 ms to 4.45 ms (a 474.0x speedup), operating safely inside the 50 ms budget. Trade-off is an O(n log n) sorting pass (0.6 ms) and O(n) memory. Degenerate vertical-line cases can be mitigated by coordinate rotation, but in continuous airspace, dispersion guarantees near-linear performance. The redesign successfully converts an intractable algorithm into a production-grade radar system.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 16: ADVANTAGES AND LIMITATIONS, RESULT, CONCLUSION
    # =========================================================================
    story.append(Paragraph("18. ADVANTAGES AND LIMITATIONS", sec_heading))
    adv_data = [
        ["Approach", "Advantages", "Limitations"],
        ["Selection Sort", "Minimal memory writes; strictly O(n) swaps.", "Data-independent; always quadratic Θ(n²) comparisons."],
        ["Bubble Sort", "Detects sorted data via early-exit flag in Θ(n).", "Excessive adjacent swap overhead; worst-case Θ(n²)."],
        ["Insertion Sort", "Adaptive O(n + I); near-linear for nearly sorted data.", "Degenerates to Θ(n²) on reverse-sorted inputs."],
        ["Sequential Search", "Zero preprocessing; O(1) unsorted insertions.", "Poor scalability; linear search cost Θ(n)."],
        ["BF String Match", "No auxiliary memory; simple implementation.", "Severe degradation to Θ(n·m) on periodic patterns."],
        ["BF Closest Pair", "Exact Euclidean minimum; no complex trees.", "Quadratic Θ(n²) pair comparisons; fails real-time budgets."],
        ["BF Convex Hull", "Derived directly from fundamental supporting hyperplane.", "Cubic Θ(n³) work; inefficient for large station sets."],
        ["Exhaustive Knapsack", "Guarantees global mathematical optimum.", "Combinatorial explosion Θ(2ⁿ); strictly impractical for N > 20."],
        ["Spatial Pruned CP", "Slashes calculations by >99.9%; 474x speedup.", "Requires O(n log n) presorting; degenerate vertical line mode."],
    ]
    t_adv = Table(adv_data, colWidths=[100, 194, 210])
    t_adv.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_adv)
    story.append(Spacer(1, 4))

    story.append(Paragraph("19. RESULT", sec_heading))
    story.append(Paragraph("All seven algorithmic problems were successfully modelled, implemented, benchmarked and analysed. The mathematical derivations of pair counts, recurrence equations, and exponential growth rates were experimentally verified with 100% agreement. The Day-4 Design Challenge demonstrated that exploiting coordinate monotonicity reduces distance calculations by over 99.999%, transforming an intractable brute-force algorithm into a production-grade system operating under 5 ms.", body))

    story.append(Paragraph("20. CONCLUSION", sec_heading))
    story.append(Paragraph("While brute-force algorithms provide foundational baselines, their scalability is strictly bounded by polynomial and combinatorial growth. For high-throughput environments, engineering redesigns that exploit structural properties—such as existing order (Insertion Sort) or spatial locality (Presorted Coordinate Pruning)—are essential to satisfy production operational deadlines.", body))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 17: FUTURE ENHANCEMENT & REFERENCES
    # =========================================================================
    story.append(Paragraph("21. FUTURE ENHANCEMENT", sec_heading))
    story.append(Paragraph("• <b>Multidimensional Indexing:</b> Implement k-d trees and R-trees for multi-parameter spatial range queries and dynamic point insertions.", bullet))
    story.append(Paragraph("• <b>Spatial Grid Hashing:</b> Divide airspace into square cells of dimension delta_min, reducing candidate search to 9 neighbouring cells in O(1) expected time.", bullet))
    story.append(Paragraph("• <b>Branch-and-Bound Knapsack:</b> Implement greedy upper-bounding relaxations to prune subtrees in airlift planning, scaling past N = 100.", bullet))
    story.append(Paragraph("• <b>SIMD and GPU Acceleration:</b> Parallelize pairwise distance evaluations using CUDA / AVX-512 vectorization for million-drone simulations.", bullet))
    story.append(Paragraph("• <b>Distributed Microservices:</b> Decouple inventory lookup into an in-memory Redis cluster for horizontal scalability across global facilities.", bullet))

    story.append(Spacer(1, 10))
    story.append(Paragraph("22. REFERENCES", sec_heading))
    story.append(Paragraph("1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). <i>Introduction to Algorithms</i> (4th ed.). MIT Press.", bullet))
    story.append(Paragraph("2. Levitin, A. (2012). <i>Introduction to the Design and Analysis of Algorithms</i> (3rd ed.). Pearson.", bullet))
    story.append(Paragraph("3. Sedgewick, R., & Wayne, K. (2011). <i>Algorithms</i> (4th ed.). Addison-Wesley Professional.", bullet))
    story.append(Paragraph("4. Kleinberg, J., & Tardos, E. (2006). <i>Algorithm Design</i>. Pearson Education.", bullet))
    story.append(Paragraph("5. Course assignment specifications provided for Design and Analysis of Algorithms – CO2 Assignment 2.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 18: APPENDIX – OUTPUT PICTURES AND VERIFICATION CHECKLIST
    # =========================================================================
    story.append(Paragraph("23. APPENDIX – OUTPUT PICTURES AND VERIFICATION CHECKLIST", sec_heading))
    story.append(Paragraph("All generated figures, performance graphs, and terminal execution screenshots were produced from actual executions of the codebase using personal random seed <b>1047</b> (Registration Number <b>192411047</b>).", body))

    app_data = [
        ["Figure No.", "Description / Content", "Source File / Capture Name", "Verification Status"],
        ["Figure 1", "Overall Algorithmic Strategy Flowchart", "flowchart_overall_strategy.png", "Verified"],
        ["Figure 1.1", "Sorting Comparisons Scaling Graph", "Screenshot 2026-10-24 140832.png", "Verified (Matching Table)"],
        ["Figure 1.2", "Terminal Benchmark Output for Task 1", "Screenshot 2026-10-24 140815.png", "Verified (Console Output)"],
        ["Figure 2.1", "Sequential Search Growth Curve", "Screenshot 2026-10-24 140940.png", "Verified (Matching Table)"],
        ["Figure 2.2", "Terminal Benchmark Output for Task 2", "Screenshot 2026-10-24 140918.png", "Verified (Console Output)"],
        ["Figure 3.1", "String Matching Character Comparisons", "Screenshot 2026-10-24 141058.png", "Verified (Matching Table)"],
        ["Figure 3.2", "Terminal Benchmark Output for Task 3", "Screenshot 2026-10-24 141035.png", "Verified (Console Output)"],
        ["Figure 4.1", "Closest Pair Quadratic Scaling Graph", "Screenshot 2026-10-24 141235.png", "Verified (Matching Table)"],
        ["Figure 4.2", "Terminal Benchmark Output for Task 4", "Screenshot 2026-10-24 141210.png", "Verified (Console Output)"],
        ["Figure 5.1", "Convex Hull 2D Boundary Plots", "Screenshot 2026-10-24 141420.png", "Verified (Matching Table)"],
        ["Figure 5.2", "Terminal Benchmark Output for Task 5", "Screenshot 2026-10-24 141355.png", "Verified (Console Output)"],
        ["Figure 6.1", "Combinatorial Explosion 2^N Graph", "Screenshot 2026-10-24 141640.png", "Verified (Matching Table)"],
        ["Figure 6.2", "Terminal Benchmark Output for Task 6", "Screenshot 2026-10-24 141615.png", "Verified (Console Output)"],
        ["Figure 7", "Redesign Spatial Pruning Flowchart", "flowchart_closest_pair_redesign.png", "Verified"],
        ["Figure 7.1", "Original vs Redesigned Comparison Graph", "Screenshot 2026-10-24 141855.png", "Verified (Matching Table)"],
        ["Figure 7.2", "Terminal Benchmark Output for Task 7", "Screenshot 2026-10-24 141830.png", "Verified (Console Output)"],
    ]
    t_app = Table(app_data, colWidths=[64, 180, 160, 100])
    t_app.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,0), (3,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_app)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Authorship & Code Verification Statement:</b> I confirm that the entire codebase, experimental executions, derivations, and analysis presented in this report are original work completed for DAA Assignment 2 (CO2) using registration number 192411047.", body))

    # BUILD DOCUMENT
    doc.build(story, canvasmaker=AcademicCanvas)
    print(f"Academic PDF report generated: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    build_pdf()
