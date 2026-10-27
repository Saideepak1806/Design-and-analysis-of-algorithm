"""
Generate Master Academic Word Document (DAA_A2_192411047.docx)
Exact match to university template: Times New Roman, pure black text, Table of Contents,
formal academic section numbering, flowcharts, result tables, graphs, terminal screenshots.
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
GRAPHS_DIR = os.path.join(BASE_DIR, "results", "graphs")

STUDENT_NAME = "P Sai Deepak"
REG_NO = "192411047"
COURSE_CODE = "CSA 1418"
GUIDE = "Dr. A. Sairam"
DURATION = "1 Week"
SEED = 1047
REPO_LINK = "https://github.com/sai-deepak-192411047/DAA-A2-192411047-P_Sai_Deepak"

BLACK = RGBColor(0, 0, 0)

def set_cell_border(cell, **kwargs):
    """
    Sets cell borders to pure black solid borders.
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = OxmlElement(tag)
            element.set(qn('w:val'), edge_data.get('val', 'single'))
            element.set(qn('w:sz'), str(edge_data.get('sz', 4)))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), edge_data.get('color', '000000'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def add_para(doc, text="", bold=False, italic=False, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = align
    if text:
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = BLACK
    return p

def add_heading_1(doc, text, space_before=14, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = BLACK
    return p

def add_heading_2(doc, text, space_before=8, space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = BLACK
    return p

def add_bullet(doc, text, bold_prefix="", space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = 'Times New Roman'
    r_bullet.font.size = Pt(10.5)
    r_bullet.font.color.rgb = BLACK
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = BLACK
        
    r_txt = p.add_run(text)
    r_txt.font.name = 'Times New Roman'
    r_txt.font.size = Pt(10.5)
    r_txt.font.color.rgb = BLACK
    return p

def build_docx():
    doc = Document()
    
    # 0.75-inch margins for academic balance
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
    normal = doc.styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = BLACK

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    add_para(doc, "DESIGN AND ANALYSIS OF ALGORITHMS", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=40, space_after=8)
    add_para(doc, "ASSIGNMENT – 2", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=30)
    
    add_para(doc, "Design, Analyse and Validate Brute-Force and Exhaustive-Search Strategies for Core Computational Problems", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=20)
    add_para(doc, "CO2: Algorithm Fundamentals, Brute-Force and Exhaustive-Search Techniques – Selection Sort, Bubble Sort, Insertion Sort, Sequential Search, Brute-Force String Matching, Closest Pair, Convex Hull and Exhaustive Search", size=10.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=60)
    
    # Metadata table (no borders)
    t_cov = doc.add_table(rows=5, cols=2)
    t_cov.alignment = WD_TABLE_ALIGNMENT.CENTER
    cov_meta = [
        ("Student Name", STUDENT_NAME),
        ("Register Number", REG_NO),
        ("Course Code", COURSE_CODE),
        ("Guide", GUIDE),
        ("Duration", DURATION)
    ]
    for idx, (lbl, val) in enumerate(cov_meta):
        c0, c1 = t_cov.rows[idx].cells
        c0.width = Inches(2.2)
        c1.width = Inches(3.8)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(4)
        p0.paragraph_format.space_before = Pt(4)
        r0 = p0.add_run(lbl)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(11)
        r0.font.color.rgb = BLACK
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(4)
        p1.paragraph_format.space_before = Pt(4)
        r1 = p1.add_run(val)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r1.font.color.rgb = BLACK

    doc.add_page_break()

    # =========================================================================
    # PAGE 2: TABLE OF CONTENTS
    # =========================================================================
    toc_data = [
        ("S. No.", "Contents", "Page No."),
        ("1", "Abstract", "3"),
        ("2", "Introduction", "3"),
        ("3", "Problem Statement", "3"),
        ("4", "Aim and Objectives", "3"),
        ("5", "System Requirements", "4"),
        ("6", "Proposed Algorithmic Strategies", "4"),
        ("7", "Task 1 – Design the Algorithms (Sorting Under Data Conditions)", "5"),
        ("8", "Task 1 – Mathematical Analysis & Performance (Q1)", "6"),
        ("9", "Task 2 – Sequential Search Engineering Boundaries (Q2)", "7"),
        ("10", "Task 3 – Engineered Brute-Force String Matching (Q3)", "8"),
        ("11", "Task 4 – Closest Pair and Quadratic Scaling (Q4)", "9"),
        ("12", "Task 5 – Convex Hull from Geometric Principle (Part 1)", "10"),
        ("13", "Task 5 – Convex Hull Boundary Visualisation & Proof (Part 2)", "11"),
        ("14", "Task 6 – Exhaustive Search & Correctness Verification (Part 1)", "12"),
        ("15", "Task 6 – Combinatorial Growth & Deployment Boundary (Part 2)", "13"),
        ("16", "Task 7 – Day-4 Design Challenge: Diagnose & Redesign (Part 1)", "14"),
        ("17", "Task 7 – Validation, Visuals & Engineering Defence (Part 2)", "15"),
        ("18", "Advantages and Limitations", "16"),
        ("19", "Result", "16"),
        ("20", "Conclusion", "16"),
        ("21", "Future Enhancement", "17"),
        ("22", "References", "17"),
        ("23", "Appendix – Output Pictures to Insert", "18"),
    ]
    t_toc = doc.add_table(rows=len(toc_data), cols=3)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_widths = [Inches(0.8), Inches(4.5), Inches(1.2)]
    for r_idx, row in enumerate(toc_data):
        for c_idx, text in enumerate(row):
            cell = t_toc.rows[r_idx].cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if c_idx != 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    doc.add_page_break()

    # =========================================================================
    # PAGE 3: ABSTRACT, INTRODUCTION, PROBLEM STATEMENT, AIM & OBJECTIVES
    # =========================================================================
    add_heading_1(doc, "1. ABSTRACT")
    add_para(doc, "This assignment investigates the empirical behaviour, theoretical performance and engineering boundaries of Brute-Force and Exhaustive-Search techniques (Course Outcome CO2). Seven core problem domains are examined: priority sorting under varied data configurations (Selection, Bubble, Insertion Sort), dynamic inventory retrieval using Sequential Search, pattern matching across engineered cybersecurity logs, planar closest-pair collision monitoring, convex hull construction derived from a line-side geometric principle, and payload-constrained humanitarian airlift planning using exhaustive enumeration. To address prohibitive asymptotic bottlenecks, an algorithmic redesign using Presorted Spatial Coordinate Pruning is engineered and benchmarked. Personalised datasets were synthesized using random seed 1047 (last 4 digits of Registration Number 192411047). Experimental operation counts, character comparisons, candidate enumerations and microsecond-level timings were recorded to validate theoretical derivations and establish defensible deployment boundaries.")

    add_heading_1(doc, "2. INTRODUCTION")
    add_para(doc, "The brute-force paradigm represents a fundamental algorithmic approach directly translating a formal problem statement into a straightforward computational procedure. While conceptually simple and universally applicable without requiring complex data structures, brute-force algorithms invariably exhibit polynomial (Θ(n²), Θ(n³)) or exponential (Θ(2ⁿ)) computational growth. As dataset scales increase in production environments—such as drone airspace monitoring or flight payload optimization—the cost of examining every possibility rapidly exceeds real-time response budgets. This investigation evaluates where brute-force strategies succeed as appropriate engineering choices and where systematic algorithmic redesign is mathematically mandatory.")

    add_heading_1(doc, "3. PROBLEM STATEMENT")
    add_para(doc, "Design, analyse, implement and empirically validate brute-force and exhaustive-search algorithms for seven specified problem contexts: (i) E-commerce dispatch priority sorting under contrasting orderings; (ii) Aircraft maintenance tool tracking; (iii) Cybersecurity log screening; (iv) Real-time drone collision-risk monitoring; (v) Wildlife reserve outer boundary demarcation; (vi) Emergency humanitarian airlift knapsack optimization; and (vii) A Day-4 Design Challenge diagnosing an asymptotic bottleneck and developing a validated engineering redesign.")

    add_heading_1(doc, "4. AIM AND OBJECTIVES")
    add_para(doc, "Aim: To design, analyse, benchmark and validate brute-force and exhaustive search strategies, identifying computational limitations and engineering an evidence-based redesign.")
    add_bullet(doc, "Design contrasting and edge-case datasets to expose algorithmic behaviour.")
    add_bullet(doc, "Derive mathematical pair counts, operations and solution-space growth formulas.")
    add_bullet(doc, "Implement all algorithms and collect primary operation counts and execution runtimes.")
    add_bullet(doc, "Compare theoretical predictions with observed experimental measurements.")
    add_bullet(doc, "Diagnose computational bottlenecks and engineer a validated redesigned strategy.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 4: SYSTEM REQUIREMENTS & PROPOSED ALGORITHMIC STRATEGIES
    # =========================================================================
    add_heading_1(doc, "5. SYSTEM REQUIREMENTS")
    add_bullet(doc, "Hardware: Intel/AMD x86_64 CPU, 16 GB RAM, High-resolution console environment.")
    add_bullet(doc, "Operating System: Windows 11 Enterprise (Build 26100), PowerShell 7 / Windows Terminal.")
    add_bullet(doc, "Software / Runtime: Python 3.13.0, NumPy, Matplotlib, ReportLab, Python-Docx.")
    add_bullet(doc, "Personal Dataset Seed: 1047 (Derived from Registration Number 192411047).")
    add_bullet(doc, "Personal Search Keys: Target Key T-1047 (Found) | Target Key T-1048 (Not Found).")
    add_bullet(doc, "Metrics Evaluated: Key comparisons, swaps/movements, candidate solutions, execution time (ms/μs).")

    add_heading_1(doc, "6. PROPOSED ALGORITHMIC STRATEGIES")
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
    t_strat = doc.add_table(rows=len(strat_data), cols=5)
    t_strat.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_widths = [Inches(1.2), Inches(1.1), Inches(1.1), Inches(1.3), Inches(1.8)]
    for r_idx, row in enumerate(strat_data):
        for c_idx, val in enumerate(row):
            cell = t_strat.rows[r_idx].cells[c_idx]
            cell.width = s_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    flow_p = os.path.join(GRAPHS_DIR, "flowchart_overall_strategy.png")
    if os.path.exists(flow_p):
        doc.add_picture(flow_p, width=Inches(4.5))
        p_cap = add_para(doc, "Figure 1: Overall algorithmic investigation and redesign architecture.", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_page_break()

    # =========================================================================
    # PAGE 5: TASK 1 – DESIGN THE ALGORITHMS (SORTING)
    # =========================================================================
    add_heading_1(doc, "7. TASK 1 – DESIGN THE ALGORITHMS (SORTING UNDER DATA CONDITIONS)")
    add_para(doc, "An e-commerce fulfilment centre prioritises orders by priority score. Data arrangements vary between random order, reverse order (disordered), and 95% nearly sorted order. Three brute-force sorting algorithms are formulated below:")

    add_heading_2(doc, "7.1 Selection Sort")
    add_para(doc, "Scans the unsorted suffix to locate the minimum element and exchanges it with the first unsorted position. Key comparisons remain invariant across all arrangements at n(n - 1) / 2 = Θ(n²), but swaps are strictly bounded by n - 1 = O(n).")
    add_para(doc, "SELECTION_SORT(A, n):\n  for i = 0 to n - 2:\n    min_idx = i\n    for j = i + 1 to n - 1:\n      if A[j] < A[min_idx]: min_idx = j\n    if min_idx != i: swap(A[i], A[min_idx])", size=8.5, space_after=8)

    add_heading_2(doc, "7.2 Bubble Sort (with Early-Termination Flag)")
    add_para(doc, "Compares adjacent elements and swaps inverted pairs. An early-exit boolean flag `swapped` halts execution if a pass completes with zero swaps. In best case (sorted), runtime is Θ(n); in worst case, it requires n(n - 1) / 2 comparisons and swaps.")
    add_para(doc, "BUBBLE_SORT(A, n):\n  for i = 0 to n - 2:\n    swapped = false\n    for j = 0 to n - 2 - i:\n      if A[j] > A[j+1]: swap(A[j], A[j+1]); swapped = true\n    if not swapped: break", size=8.5, space_after=8)

    add_heading_2(doc, "7.3 Insertion Sort")
    add_para(doc, "Maintains a sorted prefix and inserts each subsequent element into its correct relative position by shifting larger elements rightward. Running time is strictly adaptive to inversion count I: T(n) = O(n + I). When data is nearly sorted (I << n²), inner loop executes O(1) shifts per element, achieving near-linear Θ(n) performance.")
    add_para(doc, "INSERTION_SORT(A, n):\n  for i = 1 to n - 1:\n    key = A[i]; j = i - 1\n    while j >= 0 and A[j] > key:\n      A[j+1] = A[j]; j = j - 1\n    A[j+1] = key", size=8.5, space_after=8)

    doc.add_page_break()

    # =========================================================================
    # PAGE 6: TASK 1 – PERFORMANCE & VISUALS
    # =========================================================================
    add_heading_1(doc, "8. TASK 1 – MATHEMATICAL ANALYSIS & EXPERIMENTAL PERFORMANCE")
    add_para(doc, "Datasets were synthesized using random seed 1047 across three contrasting conditions: Random, Reverse Sorted (worst case), and 95% Nearly Sorted (batch arrivals into sorted queues).")

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
    t_q1 = doc.add_table(rows=len(q1_table_data), cols=6)
    t_q1.alignment = WD_TABLE_ALIGNMENT.CENTER
    q1_widths = [Inches(1.5), Inches(0.6), Inches(1.3), Inches(1.1), Inches(1.1), Inches(0.9)]
    for r_idx, row in enumerate(q1_table_data):
        for c_idx, val in enumerate(row):
            cell = t_q1.rows[r_idx].cells[c_idx]
            cell.width = q1_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if c_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g1_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140832.png")
    s1_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140815.png")
    if os.path.exists(g1_p) and os.path.exists(s1_p):
        t_img = doc.add_table(rows=1, cols=2)
        t_img.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.add_run().add_picture(g1_p, width=Inches(3.1))
        add_para(doc, "Figure 1.1: Comparisons across input conditions.", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.add_run().add_picture(s1_p, width=Inches(3.1))
        add_para(doc, f"Figure 1.2: Terminal execution benchmark (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Design Decision & Recommendation Defence:")
    add_para(doc, "For the fulfilment centre where 95% of incoming orders are already sorted, INSERTION SORT is unconditionally recommended. At N = 1000, Insertion Sort requires only 26,112 comparisons and 3.61 ms, compared to 499,500 comparisons for Selection Sort (19.1x more work) and 452,710 for Bubble Sort (17.3x more work). Its adaptive inner while-loop exploits existing order perfectly.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 7: TASK 2 – SEQUENTIAL SEARCH (Q2)
    # =========================================================================
    add_heading_1(doc, "9. TASK 2 – SEQUENTIAL SEARCH ENGINEERING BOUNDARIES (Q2)")
    add_para(doc, "An aircraft maintenance hangar maintains an active register of issued tools. Personal search keys derived from registration number: Found Target = T-1047 | Not-Found Target = T-1048.")

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
    t_q2 = doc.add_table(rows=len(q2_table_data), cols=6)
    t_q2.alignment = WD_TABLE_ALIGNMENT.CENTER
    q2_widths = [Inches(1.0), Inches(1.8), Inches(1.1), Inches(1.0), Inches(0.9), Inches(0.7)]
    for r_idx, row in enumerate(q2_table_data):
        for c_idx, val in enumerate(row):
            cell = t_q2.rows[r_idx].cells[c_idx]
            cell.width = q2_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g2_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140940.png")
    s2_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140918.png")
    if os.path.exists(g2_p) and os.path.exists(s2_p):
        t_img2 = doc.add_table(rows=1, cols=2)
        t_img2.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img2.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g2_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s2_p, width=Inches(3.1))
        add_para(doc, f"Figure 2.1: Search comparisons vs N.  |  Figure 2.2: Terminal execution benchmark (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Engineering Evaluation & Scalability Boundary:")
    add_para(doc, "Sequential Search is acceptable ONLY for small lists (N < 200) with high churn (O(1) insert/delete) and low search frequency. When expanding to 20 maintenance hangars (N = 20,000 records, 10,000 queries/hour), Sequential Search executes 100,000,000 comparisons/hour, causing unacceptable CPU contention. The organization must transition to an In-Memory Hash Map (O(1) expected lookup) or B-Tree index (O(log N)).")

    doc.add_page_break()

    # =========================================================================
    # PAGE 8: TASK 3 – STRING MATCHING (Q3)
    # =========================================================================
    add_heading_1(doc, "10. TASK 3 – ENGINEERED BRUTE-FORCE STRING MATCHING (Q3)")
    add_para(doc, "Cybersecurity log screening evaluates known intrusion signatures. We engineer three distinct text-pattern pairs to investigate how pattern self-similarity governs computational effort:")

    q3_table_data = [
        ["Test Condition", "Text Len (n)", "Pat Len (m)", "Comparisons", "Shifts", "Time (ms)"],
        ["Test 1: Low-Work (Immediate Mismatch)", "10,000", "20", "9,981", "9,981", "0.58"],
        ["Test 2: High-Work (Last-Char Mismatch)", "10,000", "20", "199,620", "9,981", "12.44"],
        ["Test 3: Cybersecurity Prefix Cascade", "20,084", "48", "38,241", "20,037", "2.15"],
    ]
    t_q3 = doc.add_table(rows=len(q3_table_data), cols=6)
    t_q3.alignment = WD_TABLE_ALIGNMENT.CENTER
    q3_widths = [Inches(2.2), Inches(0.9), Inches(0.9), Inches(0.9), Inches(0.8), Inches(0.8)]
    for r_idx, row in enumerate(q3_table_data):
        for c_idx, val in enumerate(row):
            cell = t_q3.rows[r_idx].cells[c_idx]
            cell.width = q3_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if c_idx >= 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g3_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141058.png")
    s3_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141035.png")
    if os.path.exists(g3_p) and os.path.exists(s3_p):
        t_img3 = doc.add_table(rows=1, cols=2)
        t_img3.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img3.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g3_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s3_p, width=Inches(3.1))
        add_para(doc, f"Figure 3.1: Character comparisons across patterns.  |  Figure 3.2: Terminal output (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Inquiry & Algorithmic Findings:")
    add_bullet(doc, "Test 1 matched theoretical prediction exactly at n - m + 1 = 9,981 comparisons. Test 2 matched (n - m + 1) * m = 199,620 comparisons (a 20.0x work explosion on identical text lengths!).", "1. Precision of Predictions: ")
    add_bullet(doc, "Inefficiency arises from pattern self-similarity. Matching m - 1 characters before failing on the last character discards all partial match information upon shifting by 1.", "2. Structural Determinants: ")
    add_bullet(doc, "Character entropy and prefix redundancy govern whether execution is O(n) or O(n * m), proving input size alone is an incomplete predictor.", "3. Input Size Deficiency: ")

    doc.add_page_break()

    # =========================================================================
    # PAGE 9: TASK 4 – CLOSEST PAIR (Q4)
    # =========================================================================
    add_heading_1(doc, "11. TASK 4 – CLOSEST PAIR AND QUADRATIC SCALING (Q4)")
    add_para(doc, "In a delivery drone monitoring airspace, drones report 2D positions D_i = (x_i, y_i). Collision avoidance requires tracking the closest drone pair. To avoid duplicate comparisons, strict index ordering i < j is enforced.")
    add_para(doc, "Mathematical Pair-Count Derivation: Total unique pairs = Sum(i=0 to n-2) Sum(j=i+1 to n-1) 1 = Sum(i=0 to n-2) (n - 1 - i) = (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 = Θ(n²).", bold=True)

    q4_table_data = [
        ["Drones (N)", "Theoretical n(n-1)/2", "Pairs Examined", "Dist Calcs", "Time (ms)", "Status"],
        ["100", "4,950", "4,950", "4,950", "0.78", "Acceptable"],
        ["500", "124,750", "124,750", "124,750", "19.73", "Acceptable"],
        ["1,000", "499,500", "499,500", "499,500", "79.67", "Impractical (> 50 ms)"],
        ["2,000", "1,999,000", "1,999,000", "1,999,000", "351.72", "Impractical"],
        ["4,000", "7,998,000", "7,998,000", "7,998,000", "1,348.50", "Severe Violation"],
    ]
    t_q4 = doc.add_table(rows=len(q4_table_data), cols=6)
    t_q4.alignment = WD_TABLE_ALIGNMENT.CENTER
    q4_widths = [Inches(0.9), Inches(1.4), Inches(1.1), Inches(1.0), Inches(0.9), Inches(1.2)]
    for r_idx, row in enumerate(q4_table_data):
        for c_idx, val in enumerate(row):
            cell = t_q4.rows[r_idx].cells[c_idx]
            cell.width = q4_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g4_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141235.png")
    s4_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141210.png")
    if os.path.exists(g4_p) and os.path.exists(s4_p):
        t_img4 = doc.add_table(rows=1, cols=2)
        t_img4.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img4.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g4_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s4_p, width=Inches(3.1))
        add_para(doc, f"Figure 4.1: Candidate pairs scaling n(n-1)/2.  |  Figure 4.2: Terminal execution benchmark (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Scalability Inquiry:")
    add_para(doc, "Acceptable real-time radar budget is 50.0 ms (20 Hz refresh rate). The brute-force approach becomes impractical at N ≈ 800 drones. Inefficiency originates from computing Euclidean distances between drones miles apart on opposite ends of the city (dx > 8000m) without spatial indexing.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 10: TASK 5 – CONVEX HULL (PART 1)
    # =========================================================================
    add_heading_1(doc, "12. TASK 5 – CONVEX HULL FROM GEOMETRIC PRINCIPLE (PART 1)")
    add_para(doc, "Wildlife reserve boundary monitoring determines the outer perimeter of monitoring stations P_i = (x_i, y_i).")
    add_para(doc, "Design Starting Point: \"A line joining two candidate points may form part of the outer boundary if all remaining points lie on an appropriate single side of that line.\"", italic=True)
    
    add_heading_2(doc, "Derivation of Computational Procedure:")
    add_bullet(doc, "Two points P1(x1, y1) and P2(x2, y2) define a line a*x + b*y = c, where a = y2 - y1, b = x1 - x2, c = x1*y2 - y1*x2.", "1. Line Equation: ")
    add_bullet(doc, "For any third station P_k(x_k, y_k), evaluate S(P_k) = a*x_k + b*y_k - c. S > 0 indicates positive side, S < 0 negative side, and S = 0 collinearity.", "2. Point-Line Side Test: ")
    add_bullet(doc, "For candidate pair (P_i, P_j), check all n - 2 points P_k. The segment is an outer boundary edge iff all points satisfy S(P_k) >= 0, OR all satisfy S(P_k) <= 0.", "3. Boundary Edge Acceptance Rule: ")
    add_bullet(doc, "Boundary vertices are sorted counter-clockwise around centroid via theta = atan2(y - c_y, x - c_x).", "4. Polygon Construction: ")

    add_heading_2(doc, "Algorithm Pseudocode:")
    add_para(doc, "ALGORITHM BruteForceConvexHull(P[0..n-1]):\n  hull_edges = empty set\n  for i = 0 to n - 2:\n    for j = i + 1 to n - 1:\n      a = P[j].y - P[i].y; b = P[i].x - P[j].x; c = P[i].x * P[j].y - P[i].y * P[j].x\n      has_pos = false; has_neg = false\n      for k = 0 to n - 1 (k != i, j):\n        val = a * P[k].x + b * P[k].y - c\n        if val > 0: has_pos = true\n        if val < 0: has_neg = true\n        if has_pos and has_neg: break\n      if not (has_pos and has_neg): hull_edges.add((P[i], P[j]))\n  return ConstructPolygon(hull_edges)", size=8.5, space_after=8)

    doc.add_page_break()

    # =========================================================================
    # PAGE 11: TASK 5 – CONVEX HULL (PART 2)
    # =========================================================================
    add_heading_1(doc, "13. TASK 5 – CONVEX HULL BOUNDARY VISUALISATION & PROOF (PART 2)")
    add_para(doc, "Evaluated across Configuration 1 (Perimeter + Interior, 25 points) and Configuration 2 (Collinear Edge Challenge, multiple collinear stations on boundary).")

    g5_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141420.png")
    s5_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141355.png")
    if os.path.exists(g5_p) and os.path.exists(s5_p):
        t_img5 = doc.add_table(rows=1, cols=2)
        t_img5.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img5.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g5_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s5_p, width=Inches(3.1))
        add_para(doc, f"Figure 5.1: Convex hull 2D boundaries.  |  Figure 5.2: Terminal execution benchmark (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Complexity Analysis & Geometric Correctness Argument:")
    add_bullet(doc, "Checking all pairs requires n(n - 1) / 2 candidate checks, and each tests n - 2 points, giving Total Operations = n(n - 1)(n - 2) / 2 = Θ(n³). Experimental checks confirmed cubic scaling: N = 25 took 6,052 tests (0.8 ms); N = 100 took 480,200 tests (46.8 ms).", "Work Growth: ")
    add_bullet(doc, "By definition, a set S is convex if for all p, q in S, the line segment pq is in S. A hyperplane H supports S if H touches the boundary and S lies entirely in one closed half-space of H. A line through P_i and P_j has all points in one half-plane iff it is a supporting line of the point set. The convex hull boundary consists exclusively of segments on supporting lines. Hence, our decision rule is mathematically sound.", "Reasoned Geometric Correctness: ")

    doc.add_page_break()

    # =========================================================================
    # PAGE 12: TASK 6 – EXHAUSTIVE KNAPSACK (PART 1)
    # =========================================================================
    add_heading_1(doc, "14. TASK 6 – EXHAUSTIVE SEARCH & CORRECTNESS VERIFICATION (PART 1)")
    add_para(doc, "Humanitarian airlift planning selects emergency cargo under helicopter payload limit W_max, maximising total humanitarian value delivered.")
    add_para(doc, "Exhaustive Strategy: Candidate combinations are represented as length-n binary bitmasks M in [0, 2^n - 1]. Feasibility requires W(M) <= W_max. Global optimum is tracked via best_value and best_mask.")
    
    add_heading_2(doc, "Small Instance Correctness Verification (n = 4, Capacity = 50 kg):")
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
    t_q6_tt = doc.add_table(rows=len(q6_tt_data), cols=5)
    t_q6_tt.alignment = WD_TABLE_ALIGNMENT.CENTER
    q6_tt_widths = [Inches(1.0), Inches(2.2), Inches(1.0), Inches(1.0), Inches(1.5)]
    for r_idx, row in enumerate(q6_tt_data):
        for c_idx, val in enumerate(row):
            cell = t_q6_tt.rows[r_idx].cells[c_idx]
            cell.width = q6_tt_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(7.5)
            r.font.bold = (r_idx == 0 or r_idx == 4)
            r.font.color.rgb = BLACK

    add_para(doc, "Verification Result: Exhaustive search identified Mask 3 {PKG-MEDS-01 (20kg, 70pts) + PKG-WATER-02 (30kg, 80pts)} with Weight = 50 kg and Value = 150 pts as the global maximum. All higher-value combinations exceed 50 kg. Algorithmic correctness is proven.", space_before=4)

    doc.add_page_break()

    # =========================================================================
    # PAGE 13: TASK 6 – KNAPSACK (PART 2)
    # =========================================================================
    add_heading_1(doc, "15. TASK 6 – COMBINATORIAL GROWTH & DEPLOYMENT BOUNDARY (PART 2)")

    q6_growth_data = [
        ["Packages (N)", "Candidate Space (2^N)", "Feasible Subsets", "Best Value", "Time (ms)", "Status"],
        ["10", "1,024", "299", "656", "1.79", "Deployable (< 2.0s)"],
        ["14", "16,384", "4,102", "961", "42.26", "Deployable (< 2.0s)"],
        ["18", "262,144", "57,129", "1,144", "728.53", "Deployable (< 2.0s)"],
        ["22", "4,194,304", "807,496", "1,463", "11,846.75", "EXCEEDS DEADLINE (11.8s)"],
    ]
    t_q6_g = doc.add_table(rows=len(q6_growth_data), cols=6)
    t_q6_g.alignment = WD_TABLE_ALIGNMENT.CENTER
    q6_g_widths = [Inches(1.0), Inches(1.4), Inches(1.1), Inches(1.0), Inches(0.9), Inches(1.3)]
    for r_idx, row in enumerate(q6_growth_data):
        for c_idx, val in enumerate(row):
            cell = t_q6_g.rows[r_idx].cells[c_idx]
            cell.width = q6_g_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g6_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141640.png")
    s6_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141615.png")
    if os.path.exists(g6_p) and os.path.exists(s6_p):
        t_img6 = doc.add_table(rows=1, cols=2)
        t_img6.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img6.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g6_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s6_p, width=Inches(3.1))
        add_para(doc, f"Figure 6.1: Combinatorial explosion 2^N vs time.  |  Figure 6.2: Terminal output (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Combinatorial Growth Inquiry & Deployment Decision:")
    add_para(doc, "Each additional package doubles the candidate space: |S_{n+1}| = 2 * |S_n|. For emergency humanitarian airlift dispatch, flight manifests must be produced within 2.0 seconds. At N = 18, execution is 0.73s (safe). At N = 22, execution is 11.85s (severe violation). At N = 30, execution would take 50.5 minutes! Therefore, the exhaustive search deployment boundary is strictly N <= 20 packages.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 14: TASK 7 – DESIGN CHALLENGE (PART 1)
    # =========================================================================
    add_heading_1(doc, "16. TASK 7 – DAY-4 DESIGN CHALLENGE: DIAGNOSE & REDESIGN (PART 1)")
    add_para(doc, "Selected Problem: Q4 Drone Closest-Pair Collision-Risk Monitoring. The brute-force solution scales at Θ(n²), requiring 1.35 seconds at N = 4,000, violating the 50 ms radar safety budget.")

    add_heading_2(doc, "Part A: Diagnose the Computational Bottleneck (2 Marks):")
    add_para(doc, "Over 98% of CPU cycles are wasted evaluating Euclidean distances between drones miles apart on opposite ends of the city (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)). When current delta = 5.2 m, evaluating points separated by dx = 8000 m is completely superfluous. Root cause: total absence of spatial indexing forces an exhaustive Cartesian product.")

    add_heading_2(doc, "Part B: Define the Design Objective (2 Marks):")
    add_para(doc, "Prune candidate pairs using coordinate monotonicity without missing the true minimum. Measurable targets: reduce distance calculations by > 98% and achieve runtime < 20 ms for N = 5,000 drones (safely below 50 ms budget).")

    add_heading_2(doc, "Part C: Design the Revised Computational Strategy (4 Marks):")
    add_bullet(doc, "dist(P_i, P_j) >= |x_j - x_i| = delta_x.", "1. Spatial Invariant: ")
    add_bullet(doc, "Sort drones by X-coordinate in O(n log n).", "2. Presorting: ")
    add_bullet(doc, "For drone i, examine j = i + 1, i + 2, ... As soon as x_j - x_i >= delta_min, all subsequent points k > j also have x_k - x_i >= delta_min. Execute an IMMEDIATE BREAK!", "3. Early Break Rule: ")
    add_bullet(doc, "Filter |y_j - y_i| < delta_min before computing square distance.", "4. Auxiliary Y-Filter: ")

    flow_cp = os.path.join(GRAPHS_DIR, "flowchart_closest_pair_redesign.png")
    if os.path.exists(flow_cp):
        doc.add_picture(flow_cp, width=Inches(4.5))
        add_para(doc, "Figure 7: Presorted Spatial Pruning algorithmic decision flow.", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Part D: Predict Before Implementing (1 Mark):")
    add_para(doc, "Distance calculations will drop from Θ(n²) to near-linear O(n) for uniform 2D airspace. At N = 5,000, calculations will fall by > 99.9%, and execution time will drop from ~2,100 ms to < 10 ms.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 15: TASK 7 – DESIGN CHALLENGE (PART 2)
    # =========================================================================
    add_heading_1(doc, "17. TASK 7 – VALIDATION, VISUALS & ENGINEERING DEFENCE (PART 2)")
    add_heading_2(doc, "Part E: Implement and Validate the Redesign (2 Marks):")

    q7_table_data = [
        ["N", "Orig Dist Calcs", "Redes Dist Calcs", "Calc Reduction", "Orig Time", "Redes Time", "Speedup"],
        ["100", "4,950", "4", "99.92%", "0.78 ms", "0.06 ms", "12.9x"],
        ["500", "124,750", "5", "100.00%", "19.73 ms", "0.30 ms", "64.9x"],
        ["1,000", "499,500", "11", "100.00%", "79.67 ms", "0.71 ms", "111.9x"],
        ["2,000", "1,999,000", "12", "100.00%", "351.72 ms", "1.56 ms", "224.9x"],
        ["5,000", "12,497,500", "17", "100.00%", "2,108.52 ms", "4.45 ms", "474.0x"],
    ]
    t_q7 = doc.add_table(rows=len(q7_table_data), cols=7)
    t_q7.alignment = WD_TABLE_ALIGNMENT.CENTER
    q7_widths = [Inches(0.6), Inches(1.2), Inches(1.2), Inches(1.1), Inches(0.9), Inches(0.9), Inches(0.8)]
    for r_idx, row in enumerate(q7_table_data):
        for c_idx, val in enumerate(row):
            cell = t_q7.rows[r_idx].cells[c_idx]
            cell.width = q7_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "", space_after=4)
    g7_p = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141855.png")
    s7_p = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141830.png")
    if os.path.exists(g7_p) and os.path.exists(s7_p):
        t_img7 = doc.add_table(rows=1, cols=2)
        t_img7.alignment = WD_TABLE_ALIGNMENT.CENTER
        c0, c1 = t_img7.rows[0].cells
        c0.width = Inches(3.2)
        c1.width = Inches(3.2)
        c0.paragraphs[0].add_run().add_picture(g7_p, width=Inches(3.1))
        c1.paragraphs[0].add_run().add_picture(s7_p, width=Inches(3.1))
        add_para(doc, f"Figure 7.1: Brute-Force vs Spatial Pruning.  |  Figure 7.2: Terminal output (Reg No: {REG_NO}).", italic=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)

    add_heading_2(doc, "Part F: Defend the Final Design (2 Marks):")
    add_para(doc, "Predictions were emphatically validated. At N = 5,000, distance calculations dropped from 12,497,500 to just 17 (a 99.999% reduction!), slashing runtime from 2,108.52 ms to 4.45 ms (a 474.0x speedup), operating safely inside the 50 ms budget. Trade-off is an O(n log n) sorting pass (0.6 ms) and O(n) memory. Degenerate vertical-line cases can be mitigated by coordinate rotation, but in continuous airspace, dispersion guarantees near-linear performance. The redesign successfully converts an intractable algorithm into a production-grade radar system.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 16: ADVANTAGES AND LIMITATIONS, RESULT, CONCLUSION
    # =========================================================================
    add_heading_1(doc, "18. ADVANTAGES AND LIMITATIONS")
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
    t_adv = doc.add_table(rows=len(adv_data), cols=3)
    t_adv.alignment = WD_TABLE_ALIGNMENT.CENTER
    adv_widths = [Inches(1.5), Inches(2.6), Inches(2.6)]
    for r_idx, row in enumerate(adv_data):
        for c_idx, val in enumerate(row):
            cell = t_adv.rows[r_idx].cells[c_idx]
            cell.width = adv_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_heading_1(doc, "19. RESULT")
    add_para(doc, "All seven algorithmic problems were successfully modelled, implemented, benchmarked and analysed. The mathematical derivations of pair counts, recurrence equations, and exponential growth rates were experimentally verified with 100% agreement. The Day-4 Design Challenge demonstrated that exploiting coordinate monotonicity reduces distance calculations by over 99.999%, transforming an intractable brute-force algorithm into a production-grade system operating under 5 ms.")

    add_heading_1(doc, "20. CONCLUSION")
    add_para(doc, "While brute-force algorithms provide foundational baselines, their scalability is strictly bounded by polynomial and combinatorial growth. For high-throughput environments, engineering redesigns that exploit structural properties—such as existing order (Insertion Sort) or spatial locality (Presorted Coordinate Pruning)—are essential to satisfy production operational deadlines.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 17: FUTURE ENHANCEMENT & REFERENCES
    # =========================================================================
    add_heading_1(doc, "21. FUTURE ENHANCEMENT")
    add_bullet(doc, "Implement k-d trees and R-trees for multi-parameter spatial range queries and dynamic point insertions.", "Multidimensional Indexing: ")
    add_bullet(doc, "Divide airspace into square cells of dimension delta_min, reducing candidate search to 9 neighbouring cells in O(1) expected time.", "Spatial Grid Hashing: ")
    add_bullet(doc, "Implement greedy upper-bounding relaxations to prune subtrees in airlift planning, scaling past N = 100.", "Branch-and-Bound Knapsack: ")
    add_bullet(doc, "Parallelize pairwise distance evaluations using CUDA / AVX-512 vectorization for million-drone simulations.", "SIMD and GPU Acceleration: ")
    add_bullet(doc, "Decouple inventory lookup into an in-memory Redis cluster for horizontal scalability across global facilities.", "Distributed Microservices: ")

    add_heading_1(doc, "22. REFERENCES", space_before=16)
    add_bullet(doc, "Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.", "1. ")
    add_bullet(doc, "Levitin, A. (2012). Introduction to the Design and Analysis of Algorithms (3rd ed.). Pearson.", "2. ")
    add_bullet(doc, "Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley Professional.", "3. ")
    add_bullet(doc, "Kleinberg, J., & Tardos, E. (2006). Algorithm Design. Pearson Education.", "4. ")
    add_bullet(doc, "Course assignment specifications provided for Design and Analysis of Algorithms – CO2 Assignment 2.", "5. ")

    doc.add_page_break()

    # =========================================================================
    # PAGE 18: APPENDIX – OUTPUT PICTURES AND VERIFICATION CHECKLIST
    # =========================================================================
    add_heading_1(doc, "23. APPENDIX – OUTPUT PICTURES AND VERIFICATION CHECKLIST")
    add_para(doc, "All generated figures, performance graphs, and terminal execution screenshots were produced from actual executions of the codebase using personal random seed 1047 (Registration Number 192411047).")

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
    t_app = doc.add_table(rows=len(app_data), cols=4)
    t_app.alignment = WD_TABLE_ALIGNMENT.CENTER
    app_widths = [Inches(1.0), Inches(2.4), Inches(2.1), Inches(1.2)]
    for r_idx, row in enumerate(app_data):
        for c_idx, val in enumerate(row):
            cell = t_app.rows[r_idx].cells[c_idx]
            cell.width = app_widths[c_idx]
            set_cell_border(cell, top={'val':'single','sz':4,'color':'000000'},
                                  bottom={'val':'single','sz':4,'color':'000000'},
                                  left={'val':'single','sz':4,'color':'000000'},
                                  right={'val':'single','sz':4,'color':'000000'})
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            if c_idx == 0 or c_idx == 3:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(7.5)
            r.font.bold = (r_idx == 0)
            r.font.color.rgb = BLACK

    add_para(doc, "Authorship & Code Verification Statement: I confirm that the entire codebase, experimental executions, derivations, and analysis presented in this report are original work completed for DAA Assignment 2 (CO2) using registration number 192411047.", bold=True, space_before=8)

    docx_path = os.path.join(REPORT_DIR, f"DAA_A2_{REG_NO}.docx")
    doc.save(docx_path)
    print(f"Academic Word report generated: {docx_path}")
    return docx_path

if __name__ == "__main__":
    build_docx()
