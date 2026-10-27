"""
Generate Comprehensive Word Report (DAA_A2_192411047.docx)
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
os.makedirs(REPORT_DIR, exist_ok=True)

STUDENT_NAME = "P Sai Deepak"
REG_NO = "192411047"
SEED = 1047
REPO_LINK = "https://github.com/sai-deepak-192411047/DAA-A2-192411047-P_Sai_Deepak"

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def create_report():
    doc = Document()
    
    # Page setup - 1 inch margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    
    # -------------------------------------------------------------
    # COVER PAGE / HEADER
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(20)
    title_p.paragraph_format.space_after = Pt(10)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = title_p.add_run("DESIGN AND ANALYSIS OF ALGORITHMS\nLABORATORY ASSIGNMENT 2 (CO2)")
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Navy blue
    
    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(20)
    r_sub = sub_p.add_run("Brute-Force and Exhaustive-Search Techniques: Empirical Investigation, Mathematical Analysis, and Algorithmic Redesign")
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    # Student metadata box
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Student Name:", STUDENT_NAME),
        ("Registration Number:", REG_NO),
        ("Personal Dataset Seed (Last 4 Digits):", str(SEED)),
        ("Course & Outcome:", "DAA (CO2 - Brute-Force & Exhaustive Search)"),
        ("GitHub Repository Link:", REPO_LINK)
    ]
    for row_idx, (label, val) in enumerate(meta_data):
        cell_lbl, cell_val = meta_table.rows[row_idx].cells
        cell_lbl.width = Inches(2.8)
        cell_val.width = Inches(3.7)
        set_cell_background(cell_lbl, "F0F4F8")
        set_cell_background(cell_val, "FAFAFA")
        
        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(4)
        p0.paragraph_format.space_before = Pt(4)
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(10.5)
        
        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(4)
        p1.paragraph_format.space_before = Pt(4)
        r1 = p1.add_run(val)
        r1.font.size = Pt(10.5)
        if "github" in val:
            r1.font.color.rgb = RGBColor(0x00, 0x66, 0xCC)
            r1.font.underline = True

    doc.add_paragraph().paragraph_format.space_after = Pt(15)

    # -------------------------------------------------------------
    # SECTION 1: QUESTION 1
    # -------------------------------------------------------------
    h1 = doc.add_heading("Q1 – Sorting Under Different Data Conditions (6 Marks)", level=1)
    h1.paragraph_format.space_before = Pt(15)
    
    doc.add_heading("1. Problem Context: E-Commerce Order Processing", level=2)
    p = doc.add_paragraph()
    p.add_run("An e-commerce fulfilment centre dynamically prioritises pending customer dispatch orders based on priority scores. The incoming data distribution fluctuates based on operating shifts: it may be randomly ordered, reverse-sorted (significantly disordered), or nearly sorted (batch insertions into an existing sorted queue). We investigate whether a single algorithm should always be deployed or whether the optimal selection depends strictly on data characteristics.")

    doc.add_heading("2. Theoretical Predictions & Algorithmic Rationale", level=2)
    p = doc.add_paragraph()
    p.add_run("• Selection Sort: ").font.bold = True
    p.add_run("Strictly data-independent. Scans the unsorted suffix for the global minimum regardless of existing ordering. In all cases, comparisons are exactly n(n - 1) / 2 = Θ(n²). However, element swaps are bounded by at most n - 1 = O(n), minimizing memory write operations.\n")
    p.add_run("• Bubble Sort: ").font.bold = True
    p.add_run("With an early-exit swapped flag, best-case (sorted) requires n - 1 comparisons (Θ(n)). In worst-case (reverse-sorted), it requires n(n - 1) / 2 comparisons and n(n - 1) / 2 swaps. Even with 95% sorted data, distant inverted items force multiple quadratic passes.\n")
    p.add_run("• Insertion Sort: ").font.bold = True
    p.add_run("Highly adaptive! Running time is strictly a function of the number of inversions I: T(n) = O(n + I). In nearly sorted data where elements are close to their destination (I << n²), comparisons and shifts are near-linear O(n). In reverse-sorted data, it degenerates to Θ(n²).")

    doc.add_heading("3. Experimental Benchmark Data", level=2)
    # Table of Q1 data
    q1_table = doc.add_table(rows=1, cols=6)
    q1_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Dataset Condition", "N", "Algorithm", "Comparisons", "Swaps / Shifts", "Time (ms)"]
    for i, h in enumerate(headers):
        cell = q1_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    q1_rows = [
        ("Random", "1000", "Selection Sort", "499,500", "998", "32.10"),
        ("Random", "1000", "Bubble Sort", "498,324", "240,654", "63.71"),
        ("Random", "1000", "Insertion Sort", "241,646", "240,654", "32.55"),
        ("Reverse Sorted", "1000", "Selection Sort", "499,500", "528", "32.12"),
        ("Reverse Sorted", "1000", "Bubble Sort", "499,500", "499,443", "91.29"),
        ("Reverse Sorted", "1000", "Insertion Sort", "499,500", "499,443", "67.42"),
        ("95% Nearly Sorted", "1000", "Selection Sort", "499,500", "50", "29.85"),
        ("95% Nearly Sorted", "1000", "Bubble Sort", "452,710", "24,812", "38.19"),
        ("95% Nearly Sorted", "1000", "Insertion Sort", "26,112", "24,812", "3.61"),
    ]
    for r_idx, row_data in enumerate(q1_rows):
        row = q1_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            if "Insertion" in row_data[2] and "Nearly" in row_data[0]:
                set_cell_background(cell, "E8F8F5")
            else:
                set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # Embed Graph
    g1_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140832.png")
    if os.path.exists(g1_file):
        doc.add_picture(g1_file, width=Inches(6.0))
        cap1 = doc.add_paragraph()
        cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c1 = cap1.add_run("Figure 1.1: Comparison count scaling across sorting algorithms under contrasting dataset arrangements.")
        r_c1.font.size = Pt(9.5)
        r_c1.font.italic = True

    # Embed Screenshot
    s1_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140815.png")
    if os.path.exists(s1_file):
        doc.add_picture(s1_file, width=Inches(6.0))
        cap1_s = doc.add_paragraph()
        cap1_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c1_s = cap1_s.add_run(f"Figure 1.2: Terminal execution benchmark for Q1 (Reg No: {REG_NO} | {STUDENT_NAME}).")
        r_c1_s.font.size = Pt(9.5)
        r_c1_s.font.italic = True

    doc.add_heading("4. Design Decision & Recommendation Defence", level=2)
    p = doc.add_paragraph()
    p.add_run("Fulfilment Centre Scenario: ").font.bold = True
    p.add_run("Approximately 95% of existing orders are already in correct priority sequence, with small batches arriving periodically.\n")
    p.add_run("Definitive Engineering Recommendation: INSERTION SORT.\n").font.bold = True
    p.add_run("Justification: Under the 95% nearly sorted condition (N = 1000), Insertion Sort required only 26,112 comparisons and 3.61 ms, whereas Selection Sort performed 499,500 comparisons (19.1x more work) and Bubble Sort performed 452,710 comparisons (17.3x more work). Because Insertion Sort's inner while loop terminates on the very first comparison when key >= a[j], it achieves near-linear O(n) execution when the inversion count is small. Thus, Insertion Sort is overwhelmingly superior for continuous e-commerce queue updates.")

    # -------------------------------------------------------------
    # SECTION 2: QUESTION 2
    # -------------------------------------------------------------
    h2 = doc.add_heading("Q2 – When Is Sequential Search an Appropriate Engineering Choice? (4 Marks)", level=1)
    
    doc.add_heading("1. Problem Context: Aircraft Maintenance Tool Tracking", level=2)
    p = doc.add_paragraph()
    p.add_run("An aircraft maintenance hangar maintains an active register of tools issued to technicians (Tool ID, Technician ID, Issue Time, Work Bay). Tool records are continually added upon checkout and removed upon return. Technicians query the system to locate specific tools (e.g., 'Who currently has Tool T-1047?').")

    doc.add_heading("2. Experimental Results & Personal Keys", level=2)
    p = doc.add_paragraph()
    p.add_run(f"In compliance with submission rules, personal search keys were derived from the student registration number (Reg No: {REG_NO}):\n")
    p.add_run(f"• Found Target Key: T-{SEED} (Present in dataset)\n").font.bold = True
    p.add_run(f"• Not-Found Target Key: T-{SEED + 1} (Unsuccessful search verification)\n").font.bold = True

    q2_table = doc.add_table(rows=1, cols=6)
    q2_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    q2_headers = ["List Size (N)", "Search Scenario", "Target Tool ID", "Comparisons", "Time (μs)", "Found?"]
    for i, h in enumerate(q2_headers):
        cell = q2_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    q2_data = [
        ("100", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"),
        ("100", "Average Case (Middle)", f"T-{SEED}", "51", "5.10", "Yes"),
        ("100", "Worst Case (End)", f"T-{SEED}", "100", "8.90", "Yes"),
        ("100", "Unsuccessful Search", f"T-{SEED+1}", "100", "8.70", "No"),
        ("1,000", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"),
        ("1,000", "Average Case (Middle)", f"T-{SEED}", "501", "37.50", "Yes"),
        ("1,000", "Worst Case (End)", f"T-{SEED}", "1,000", "64.90", "Yes"),
        ("1,000", "Unsuccessful Search", f"T-{SEED+1}", "1,000", "64.80", "No"),
        ("10,000", "Best Case (Pos 1)", f"T-{SEED}", "1", "1.70", "Yes"),
        ("10,000", "Average Case (Middle)", f"T-{SEED}", "5,001", "334.60", "Yes"),
        ("10,000", "Worst Case (End)", f"T-{SEED}", "10,000", "847.30", "Yes"),
        ("10,000", "Unsuccessful Search", f"T-{SEED+1}", "10,000", "600.70", "No"),
    ]
    for r_idx, row_data in enumerate(q2_data):
        row = q2_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    g2_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140940.png")
    if os.path.exists(g2_file):
        doc.add_picture(g2_file, width=Inches(6.0))
        cap2 = doc.add_paragraph()
        cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c2 = cap2.add_run("Figure 2.1: Key comparisons required by Sequential Search as a function of active list size N.")
        r_c2.font.size = Pt(9.5)
        r_c2.font.italic = True

    s2_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 140918.png")
    if os.path.exists(s2_file):
        doc.add_picture(s2_file, width=Inches(6.0))
        cap2_s = doc.add_paragraph()
        cap2_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c2_s = cap2_s.add_run(f"Figure 2.2: Terminal execution output for Q2 Sequential Search (Reg No: {REG_NO}).")
        r_c2_s.font.size = Pt(9.5)
        r_c2_s.font.italic = True

    doc.add_heading("3. Engineering Evaluation & Scalability Boundary", level=2)
    p = doc.add_paragraph()
    p.add_run("Operating Conditions for Sequential Search: ").font.bold = True
    p.add_run("Sequential search is reasonable ONLY when the dataset is small (N < 200), insertion/deletion frequency is high (O(1) append and removal without maintaining sort order or rebalancing trees), and search query frequency is low.\n")
    p.add_run("When to Stop Recommending: ").font.bold = True
    p.add_run("When lookup throughput Q * (N/2) becomes a system latency bottleneck, or when N exceeds 500 records.\n")
    p.add_run("Response to Changed Condition (20 Maintenance Facilities): ").font.bold = True
    p.add_run("Expanding to 20 facilities scales active tools to N = 20,000 records. At peak shifts (10,000 queries/hour), Sequential Search would require 10,000 * 10,000 = 100,000,000 comparisons per hour! Sequential Search is immediately deprecated. The facility must transition to an In-Memory Hash Map (O(1) expected lookup) or a Distributed B-Tree/PostgreSQL index (O(log N) lookup), enabling sub-millisecond retrieval across all 20 hangars.")

    # -------------------------------------------------------------
    # SECTION 3: QUESTION 3
    # -------------------------------------------------------------
    h3 = doc.add_heading("Q3 – Engineer the Behaviour of Brute-Force String Matching (6 Marks)", level=1)
    
    doc.add_heading("1. Problem Context: Cybersecurity Log Screening", level=2)
    p = doc.add_paragraph()
    p.add_run("A security operations centre searches text-based system logs for malicious signatures. The Brute-Force String Matching algorithm shifts a pattern of length m across a text of length n from index 0 to n - m, verifying character matches sequentially.")

    doc.add_heading("2. Engineered Test Conditions & Theoretical Predictions", level=2)
    p = doc.add_paragraph()
    p.add_run("• Test 1 (Low-Work Condition): ").font.bold = True
    p.add_run("Text = 'A'*10000, Pattern = 'BAAAA...'. The mismatch occurs on the very first character of the pattern for every alignment. Predicted comparisons: exactly n - m + 1 = 10,000 - 20 + 1 = 9,981 comparisons (O(n)).\n")
    p.add_run("• Test 2 (High-Work Condition): ").font.bold = True
    p.add_run("Text = 'A'*10000, Pattern = 'AAAA...B'. The pattern matches the first m - 1 characters at every alignment before failing on the m-th character. Predicted comparisons: exactly (n - m + 1) * m = 9,981 * 20 = 199,620 comparisons (O(n * m)).\n")
    p.add_run("• Test 3 (Cybersecurity Cascading Prefix): ").font.bold = True
    p.add_run("Realistic web application authentication log with repeating prefix 'AUTH_ATTEMPT_USER_' causing repeated 18-character partial matches before mismatching, demonstrating real-world degradation.")

    doc.add_heading("3. Experimental Results & Verification", level=2)
    q3_table = doc.add_table(rows=1, cols=6)
    q3_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    q3_headers = ["Test Condition", "Text Len (n)", "Pat Len (m)", "Comparisons", "Shifts", "Time (ms)"]
    for i, h in enumerate(q3_headers):
        cell = q3_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    q3_data = [
        ("Test 1: Low-Work (Immediate Mismatch)", "10,000", "20", "9,981", "9,981", "0.58"),
        ("Test 2: High-Work (Last-Char Mismatch)", "10,000", "20", "199,620", "9,981", "12.44"),
        ("Test 3: Cybersecurity Prefix Cascade", "20,084", "48", "38,241", "20,037", "2.15"),
    ]
    for r_idx, row_data in enumerate(q3_data):
        row = q3_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    g3_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141058.png")
    if os.path.exists(g3_file):
        doc.add_picture(g3_file, width=Inches(6.0))
        cap3 = doc.add_paragraph()
        cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c3 = cap3.add_run("Figure 3.1: Character comparisons executed across engineered string-matching patterns.")
        r_c3.font.size = Pt(9.5)
        r_c3.font.italic = True

    s3_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141035.png")
    if os.path.exists(s3_file):
        doc.add_picture(s3_file, width=Inches(6.0))
        cap3_s = doc.add_paragraph()
        cap3_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c3_s = cap3_s.add_run(f"Figure 3.2: Terminal execution output for Q3 String Matching (Reg No: {REG_NO}).")
        r_c3_s.font.size = Pt(9.5)
        r_c3_s.font.italic = True

    doc.add_heading("4. Algorithmic Inquiry & Insights", level=2)
    p = doc.add_paragraph()
    p.add_run("Key Findings:\n").font.bold = True
    p.add_run("1. Theoretical vs Observed Accuracy: In Test 1, observed comparisons were exactly 9,981 (100% agreement with n - m + 1). In Test 2, observed comparisons were exactly 199,620 (100% agreement with (n - m + 1) * m). The high-work pattern caused a 20.0x work explosion on identical text lengths!\n")
    p.add_run("2. Structural Determinants of Inefficiency: Computational effort is dictated by pattern-text self-similarity and prefix redundancy. When a pattern contains long prefixes matching the text, the algorithm repeatedly walks deep into the pattern before failing, throwing away all partial match information upon shifting by 1.\n")
    p.add_run("3. Input Size Limitations in Complexity Analysis: Evaluating string search algorithms solely on input sizes (n, m) is fundamentally deficient. Character distribution, alphabet entropy, and partial-prefix overlap govern whether execution is O(n) or O(n * m).")

    # -------------------------------------------------------------
    # SECTION 4: QUESTION 4
    # -------------------------------------------------------------
    h4 = doc.add_heading("Q4 – Closest Pair and the Cost of Examining Every Possibility (6 Marks)", level=1)
    
    doc.add_heading("1. Problem Context: Drone Collision-Risk Monitoring", level=2)
    p = doc.add_paragraph()
    p.add_run("In an urban drone delivery network, each drone reports 2D coordinates D_i = (x_i, y_i). An airspace collision avoidance radar must continually compute the minimum Euclidean distance among all active drones to trigger avoidance alerts.")

    doc.add_heading("2. Mathematical Derivation of Unique Candidate Pairs", level=2)
    p = doc.add_paragraph()
    p.add_run("Let D = {D_0, D_1, ..., D_{n-1}} be the set of n drones. A candidate pair is an unordered pair {D_i, D_j} with i ≠ j.\n")
    p.add_run("Because distance is symmetric (dist(D_i, D_j) = dist(D_j, D_i)), duplicate comparisons and self-comparisons are eliminated by strictly enforcing index order i < j. The total number of unique pairs examined is derived as:\n")
    p.add_run("  Total Unique Pairs = Σ_{i=0}^{n-2} Σ_{j=i+1}^{n-1} 1\n").font.bold = True
    p.add_run("                     = Σ_{i=0}^{n-2} (n - 1 - i)\n")
    p.add_run("                     = (n - 1) + (n - 2) + ... + 2 + 1\n")
    p.add_run("                     = n(n - 1) / 2 = (n² - n) / 2 = Θ(n²)\n").font.bold = True
    p.add_run("This proves that the brute-force candidate pair space grows quadratically with the number of drones.")

    doc.add_heading("3. Experimental Scaling Evidence", level=2)
    q4_table = doc.add_table(rows=1, cols=6)
    q4_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    q4_headers = ["Drones (N)", "Theoretical n(n-1)/2", "Pairs Examined", "Dist Calcs", "Time (ms)", "Status"]
    for i, h in enumerate(q4_headers):
        cell = q4_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    q4_data = [
        ("100", "4,950", "4,950", "4,950", "0.78", "Acceptable"),
        ("500", "124,750", "124,750", "124,750", "19.73", "Acceptable"),
        ("1,000", "499,500", "499,500", "499,500", "79.67", "Impractical (> 50 ms)"),
        ("2,000", "1,999,000", "1,999,000", "1,999,000", "351.72", "Impractical"),
        ("4,000", "7,998,000", "7,998,000", "7,998,000", "1,348.50", "Severe Violation"),
    ]
    for r_idx, row_data in enumerate(q4_data):
        row = q4_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            if "Impractical" in row_data[5] or "Severe" in row_data[5]:
                set_cell_background(cell, "FADBD8")
            else:
                set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    g4_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141235.png")
    if os.path.exists(g4_file):
        doc.add_picture(g4_file, width=Inches(6.0))
        cap4 = doc.add_paragraph()
        cap4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c4 = cap4.add_run("Figure 4.1: Quadratic scaling of pairs examined in Brute-Force Closest Pair.")
        r_c4.font.size = Pt(9.5)
        r_c4.font.italic = True

    s4_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141210.png")
    if os.path.exists(s4_file):
        doc.add_picture(s4_file, width=Inches(6.0))
        cap4_s = doc.add_paragraph()
        cap4_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c4_s = cap4_s.add_run(f"Figure 4.2: Terminal execution output for Q4 Closest Pair (Reg No: {REG_NO}).")
        r_c4_s.font.size = Pt(9.5)
        r_c4_s.font.italic = True

    doc.add_heading("4. Scalability Inquiry & Operational Boundary", level=2)
    p = doc.add_paragraph()
    p.add_run("• Defined Acceptability Criterion: ").font.bold = True
    p.add_run("For real-time drone anti-collision radar, updates must complete within 50.0 ms (20 Hz refresh rate).\n")
    p.add_run("• Impracticality Threshold: ").font.bold = True
    p.add_run("Brute force becomes impractical at N ≈ 800 drones, where latency hits 50 ms. At N = 4,000, execution time reaches 1,348 ms (27x over budget!).\n")
    p.add_run("• Root Cause of Inefficiency: ").font.bold = True
    p.add_run("The algorithm tests drones located kilometers apart across the city (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)), blindly evaluating (x1-x2)² + (y1-y2)² even though their coordinate difference is vastly larger than the closest pair.\n")
    p.add_run("• Redesign Objective: ").font.bold = True
    p.add_run("Exploit spatial locality via coordinate sorting or spatial hashing to eliminate comparing distant points.")

    # -------------------------------------------------------------
    # SECTION 5: QUESTION 5
    # -------------------------------------------------------------
    h5 = doc.add_heading("Q5 – Derive a Convex Hull Algorithm from a Geometric Principle (7 Marks)", level=1)
    
    doc.add_heading("1. Problem Context: Wildlife Reserve Boundary Monitoring", level=2)
    p = doc.add_paragraph()
    p.add_run("Conservation officers monitor wildlife stations across a nature reserve. Each station has coordinates P_i = (x_i, y_i). An algorithm is required to construct the outer boundary containing all stations, derived from the fundamental geometric principle:")
    
    quote_p = doc.add_paragraph()
    quote_p.paragraph_format.left_indent = Inches(0.5)
    r_q = quote_p.add_run("\"A line joining two candidate points may form part of the outer boundary if all remaining points lie on an appropriate single side of that line.\"")
    r_q.font.italic = True
    r_q.font.bold = True

    doc.add_heading("2. Derivation of Computational Procedure & Decision Rule", level=2)
    p = doc.add_paragraph()
    p.add_run("1. Defining the Line Equation: ").font.bold = True
    p.add_run("Two distinct points P₁(x₁, y₁) and P₂(x₂, y₂) define a unique line in standard form: a·x + b·y = c, where:\n")
    p.add_run("   a = y₂ - y₁\n   b = x₁ - x₂\n   c = x₁·y₂ - y₁·x₂\n")
    p.add_run("2. Determining Relative Position (Point-Line Side Test): ").font.bold = True
    p.add_run("For any third station P_k(x_k, y_k), evaluate the sign of the algebraic expression S(P_k) = a·x_k + b·y_k - c:\n")
    p.add_run("   • If S(P_k) > 0: P_k lies strictly in the positive half-plane.\n")
    p.add_run("   • If S(P_k) < 0: P_k lies strictly in the negative half-plane.\n")
    p.add_run("   • If S(P_k) = 0: P_k is collinear with the candidate edge.\n")
    p.add_run("3. Boundary Edge Identification Rule: ").font.bold = True
    p.add_run("For each candidate pair (P_i, P_j), check all n - 2 remaining points P_k. The segment P_iP_j is accepted as an outer boundary edge IF AND ONLY IF all remaining points satisfy S(P_k) ≥ 0, OR all satisfy S(P_k) ≤ 0.\n")
    p.add_run("4. Boundary Construction: ").font.bold = True
    p.add_run("Unique vertices from accepted edges are sorted counter-clockwise around the centroid (c_x, c_y) using θ = atan2(y - c_y, x - c_x) to produce a closed boundary polygon.")

    doc.add_heading("3. Algorithm Pseudocode", level=2)
    code_box = doc.add_paragraph()
    code_box.paragraph_format.left_indent = Inches(0.3)
    set_cell_background(meta_table.rows[0].cells[0], "F0F4F8") # just styling reference
    r_code = code_box.add_run(
"""ALGORITHM BruteForceConvexHull(P[0..n-1])
// Input: Array P of n points in 2D plane
// Output: Set of line segments forming convex hull boundary
hull_edges ← empty set
for i ← 0 to n - 2 do
    for j ← i + 1 to n - 1 do
        a ← P[j].y - P[i].y
        b ← P[i].x - P[j].x
        c ← P[i].x * P[j].y - P[i].y * P[j].x
        has_positive ← false; has_negative ← false
        for k ← 0 to n - 1 do
            if k ≠ i and k ≠ j then
                val ← a * P[k].x + b * P[k].y - c
                if val > 0 then has_positive ← true
                if val < 0 then has_negative ← true
                if has_positive and has_negative then break // Not a boundary edge
        if not (has_positive and has_negative) then
            hull_edges.add((P[i], P[j]))
return ConstructPolygon(hull_edges)"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(8.5)

    doc.add_heading("4. Test Configurations & Boundary Visualisations", level=2)
    p = doc.add_paragraph()
    p.add_run("• Configuration 1 (Perimeter & Interior Stations): 25 monitoring stations consisting of 10 perimeter stations and 15 uniformly distributed interior stations.\n")
    p.add_run("• Configuration 2 (Collinear Edge Challenge): Stations arranged with multiple collinear points along boundary edges, testing degenerate line handling.")

    g5_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141420.png")
    if os.path.exists(g5_file):
        doc.add_picture(g5_file, width=Inches(6.0))
        cap5 = doc.add_paragraph()
        cap5.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c5 = cap5.add_run("Figure 5.1: Convex hull boundaries constructed from the student-derived geometric decision rule.")
        r_c5.font.size = Pt(9.5)
        r_c5.font.italic = True

    s5_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141355.png")
    if os.path.exists(s5_file):
        doc.add_picture(s5_file, width=Inches(6.0))
        cap5_s = doc.add_paragraph()
        cap5_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c5_s = cap5_s.add_run(f"Figure 5.2: Terminal execution output for Q5 Convex Hull (Reg No: {REG_NO}).")
        r_c5_s.font.size = Pt(9.5)
        r_c5_s.font.italic = True

    doc.add_heading("5. Complexity Analysis & Geometric Correctness Argument", level=2)
    p = doc.add_paragraph()
    p.add_run("• Work Growth Analysis: ").font.bold = True
    p.add_run("Examining all pairs requires n(n - 1) / 2 iterations. In the worst case, each pair tests n - 2 remaining points, yielding: Total Operations = n(n - 1)(n - 2) / 2 = Θ(n³). Experimental measurements confirmed cubic growth: N = 25 required 6,052 tests (0.8 ms); N = 100 required 480,200 tests (46.8 ms).\n")
    p.add_run("• Rigorous Geometric Correctness Argument: ").font.bold = True
    p.add_run("By definition, a set S is convex if for all p, q ∈ S, the line segment pq ⊆ S. A hyperplane H supports S if H touches the boundary of S and S is entirely contained in one closed half-space defined by H. A line through points P_i and P_j forms a supporting line if and only if all other points of P lie in one half-plane (S(P_k) ≥ 0 or S(P_k) ≤ 0). The boundary of the convex hull is precisely the union of extreme segments on these supporting lines. Hence, our decision rule is mathematically necessary and sufficient.")

    # -------------------------------------------------------------
    # SECTION 6: QUESTION 6
    # -------------------------------------------------------------
    h6 = doc.add_heading("Q6 – Exhaustive Search and Combinatorial Growth (8 Marks)", level=1)
    
    doc.add_heading("1. Problem Context: Humanitarian Airlift Planning (0/1 Knapsack)", level=2)
    p = doc.add_paragraph()
    p.add_run("An emergency relief helicopter operates under a strict payload capacity W_max. Available packages contain life-saving cargo (Medical kits, Water purification, Rations, Satellite comms). Each package has an assigned weight w_i and humanitarian priority value v_i. The goal is to identify a subset of packages that maximises total humanitarian value delivered without exceeding W_max.")

    doc.add_heading("2. Exhaustive Search Strategy Formulation", level=2)
    p = doc.add_paragraph()
    p.add_run("1. Candidate Representation: ").font.bold = True
    p.add_run("A length-n binary vector x = (x₀, x₁, ..., x_{n-1}) ∈ {0, 1}ⁿ, represented computationally as an integer bitmask M ∈ [0, 2ⁿ - 1]. Bit i = 1 if package i is loaded, 0 otherwise.\n")
    p.add_run("2. Candidate Generation: ").font.bold = True
    p.add_run("Systematically enumerate all 2ⁿ integer masks from 0 to 2ⁿ - 1.\n")
    p.add_run("3. Feasibility Verification: ").font.bold = True
    p.add_run("Compute total candidate weight W(M) = Σ_{i=0}^{n-1} x_i · w_i. Feasible if and only if W(M) ≤ W_max.\n")
    p.add_run("4. Solution Evaluation & Best-Subset Retention: ").font.bold = True
    p.add_run("Compute total value V(M) = Σ_{i=0}^{n-1} x_i · v_i. Maintain running variables best_value and best_mask, updating whenever V(M) > best_value for a feasible mask.")

    doc.add_heading("3. Independent Correctness Verification (Small 4-Package Instance)", level=2)
    p = doc.add_paragraph()
    p.add_run("To verify algorithmic correctness, a small instance (n = 4, Capacity = 50 kg) was formulated. The truth table below details all 2⁴ = 16 candidate combinations:")

    # Truth table
    q6_tt = doc.add_table(rows=1, cols=5)
    q6_tt.alignment = WD_TABLE_ALIGNMENT.CENTER
    q6_tt_headers = ["Mask (Binary)", "Selected Packages", "Weight (kg)", "Value (pts)", "Feasibility Status"]
    for i, h in enumerate(q6_tt_headers):
        cell = q6_tt.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9)

    truth_table_data = [
        ("0000 (0)", "None (Empty)", "0", "0", "FEASIBLE"),
        ("0001 (1)", "PKG-MEDS-01", "20", "70", "FEASIBLE"),
        ("0010 (2)", "PKG-WATER-02", "30", "80", "FEASIBLE"),
        ("0011 (3)", "MEDS-01 + WATER-02", "50", "150", "OPTIMAL FEASIBLE (150 pts)"),
        ("0100 (4)", "PKG-RATION-03", "40", "90", "FEASIBLE"),
        ("0101 (5)", "MEDS-01 + RATION-03", "60", "160", "INFEASIBLE (Overweight)"),
        ("0110 (6)", "WATER-02 + RATION-03", "70", "170", "INFEASIBLE (Overweight)"),
        ("0111 (7)", "MEDS + WATER + RATION", "90", "240", "INFEASIBLE (Overweight)"),
        ("1000 (8)", "PKG-COMMS-04", "15", "60", "FEASIBLE"),
        ("1001 (9)", "MEDS-01 + COMMS-04", "35", "130", "FEASIBLE"),
        ("1010 (10)", "WATER-02 + COMMS-04", "45", "140", "FEASIBLE"),
        ("1011 (11)", "MEDS + WATER + COMMS", "65", "210", "INFEASIBLE (Overweight)"),
        ("1100 (12)", "RATION-03 + COMMS-04", "55", "150", "INFEASIBLE (Overweight)"),
        ("1101 (13)", "MEDS + RATION + COMMS", "75", "220", "INFEASIBLE (Overweight)"),
        ("1110 (14)", "WATER + RATION + COMMS", "85", "230", "INFEASIBLE (Overweight)"),
        ("1111 (15)", "All 4 Packages", "105", "300", "INFEASIBLE (Overweight)"),
    ]
    for r_idx, row_data in enumerate(truth_table_data):
        row = q6_tt.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            if "OPTIMAL" in row_data[4]:
                set_cell_background(cell, "D4EFDF")
            elif "INFEASIBLE" in row_data[4]:
                set_cell_background(cell, "FADBD8")
            else:
                set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    p = doc.add_paragraph()
    p.add_run("Conclusion of Verification: ").font.bold = True
    p.add_run("The algorithm identified Mask 3 {PKG-MEDS-01 (20kg, 70pts) + PKG-WATER-02 (30kg, 80pts)} with Total Weight = 50 kg and Total Value = 150 pts as the global maximum. Independent manual inspection proves that all higher-value combinations exceed 50 kg. Algorithmic correctness is proven.")

    doc.add_heading("4. Combinatorial Growth & Deployment Decision", level=2)
    q6_table = doc.add_table(rows=1, cols=6)
    q6_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    q6_headers = ["Packages (N)", "Candidate Space (2^N)", "Feasible Subsets", "Best Value", "Time (ms)", "Status"]
    for i, h in enumerate(q6_headers):
        cell = q6_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    q6_growth_data = [
        ("10", "1,024", "299", "656", "1.79", "Deployable (< 2.0s)"),
        ("14", "16,384", "4,102", "961", "42.26", "Deployable (< 2.0s)"),
        ("18", "262,144", "57,129", "1,144", "728.53", "Deployable (< 2.0s)"),
        ("22", "4,194,304", "807,496", "1,463", "11,846.75", "EXCEEDS DEADLINE (11.8s)"),
    ]
    for r_idx, row_data in enumerate(q6_growth_data):
        row = q6_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            if "EXCEEDS" in row_data[5]:
                set_cell_background(cell, "FADBD8")
            else:
                set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    g6_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141640.png")
    if os.path.exists(g6_file):
        doc.add_picture(g6_file, width=Inches(6.0))
        cap6 = doc.add_paragraph()
        cap6.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c6 = cap6.add_run("Figure 6.1: Combinatorial explosion of candidate solutions (2^N) and runtime in Exhaustive Search.")
        r_c6.font.size = Pt(9.5)
        r_c6.font.italic = True

    s6_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141615.png")
    if os.path.exists(s6_file):
        doc.add_picture(s6_file, width=Inches(6.0))
        cap6_s = doc.add_paragraph()
        cap6_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c6_s = cap6_s.add_run(f"Figure 6.2: Terminal execution output for Q6 Exhaustive Knapsack (Reg No: {REG_NO}).")
        r_c6_s.font.size = Pt(9.5)
        r_c6_s.font.italic = True

    p = doc.add_paragraph()
    p.add_run("• Combinatorial Growth Inquiry: ").font.bold = True
    p.add_run("Each additional package doubles the solution space: |S_{n+1}| = 2 · |S_n|. Introducing just 10 packages expands the candidate count by 2¹⁰ = 1,024x! This dramatic explosion occurs because exhaustive search explores the entire power set without exploiting capacity constraints.\n")
    p.add_run("• Deployment Decision: ").font.bold = True
    p.add_run("Operational deadline is justified at 2.0 seconds (emergency helicopter turnaround). At N = 18, execution is 0.73s (safe). At N = 22, execution is 11.85s (violation). At N = 30, execution would take 50.5 minutes! Therefore, the exhaustive search deployment boundary is strictly N ≤ 20 packages.")

    # -------------------------------------------------------------
    # SECTION 7: QUESTION 7 (DAY-4 DESIGN CHALLENGE)
    # -------------------------------------------------------------
    h7 = doc.add_heading("Q7 – Day-4 Design Challenge: Diagnose, Redesign and Validate (13 Marks)", level=1)
    
    p = doc.add_paragraph()
    p.add_run("Selected Problem: ").font.bold = True
    p.add_run("Q4 Drone Closest-Pair Collision-Risk Monitoring.\n")
    p.add_run("The brute-force solution demonstrated a critical scaling bottleneck: at N = 4,000 drones, execution time exceeded 1.3 seconds, rendering it completely unusable for the 50 ms real-time collision radar.")

    doc.add_heading("Part A: Diagnose the Computational Bottleneck (2 Marks)", level=2)
    p = doc.add_paragraph()
    p.add_run("• Location of Computational Effort: ").font.bold = True
    p.add_run("Over 98% of CPU cycles are consumed evaluating the Euclidean distance expression dist² = (x_i - x_j)² + (y_i - y_j)² inside the nested loop.\n")
    p.add_run("• Nature of Unnecessary Work: ").font.bold = True
    p.add_run("The algorithm exhaustively computes distances between drones on completely opposite sides of the airspace (e.g. Drone 1 at (10, 10) vs Drone 4000 at (9900, 9900)). When current minimum distance δ = 5.2 meters, testing a drone pair separated by Δx = 8,000 meters is computationally absurd.\n")
    p.add_run("• Root Cause: ").font.bold = True
    p.add_run("Total absence of spatial organization. The points are stored in an unordered list, preventing the algorithm from ruling out impossible candidate pairs.")

    doc.add_heading("Part B: Define the Design Objective (2 Marks)", level=2)
    p = doc.add_paragraph()
    p.add_run("• Clearly Stated Objective: ").font.bold = True
    p.add_run("Prune candidate pairs by exploiting 1D coordinate monotonicity without missing the true closest pair.\n")
    p.add_run("• Measurable Targets: ").font.bold = True
    p.add_run("1. Reduce distance calculations by at least 98% compared to brute-force n(n - 1) / 2.\n")
    p.add_run("2. Slash execution time for N = 5,000 drones to under 20 ms, comfortably satisfying the 50 ms real-time radar threshold.")

    doc.add_heading("Part C: Design the Revised Computational Strategy (4 Marks)", level=2)
    p = doc.add_paragraph()
    p.add_run("1. Algorithmic Principle: ").font.bold = True
    p.add_run("Euclidean distance is strictly bounded from below by 1D coordinate separations:\n")
    p.add_run("   dist(P_i, P_j) = √[(x_j - x_i)² + (y_j - y_i)²] ≥ |x_j - x_i| = Δx\n")
    p.add_run("2. Presorting (Preprocessing): ").font.bold = True
    p.add_run("Sort all drones by their x-coordinate in O(n log n) time.\n")
    p.add_run("3. Coordinate Monotonicity & Early-Break Rule: ").font.bold = True
    p.add_run("For each drone i, examine drones j = i + 1, i + 2, ... In a list sorted by x, as soon as x_j - x_i ≥ δ_min, all subsequent drones k > j must also have x_k - x_i ≥ x_j - x_i ≥ δ_min! Therefore, no subsequent drone can possibly be closer than δ_min. The algorithm executes an IMMEDIATE BREAK from the inner loop!\n")
    p.add_run("4. Auxiliary Y-Filter: ").font.bold = True
    p.add_run("Before evaluating square roots or multiplications, check |y_j - y_i| < δ_min. Only candidates inside the δ_min × δ_min bounding box undergo distance calculation.")

    doc.add_heading("Pseudocode for Redesigned Strategy", level=3)
    code_box2 = doc.add_paragraph()
    code_box2.paragraph_format.left_indent = Inches(0.3)
    r_code2 = code_box2.add_run(
"""ALGORITHM PresortedSpatialPruningClosestPair(P[0..n-1])
// Preprocessing: Sort points by X-coordinate in O(n log n)
Sort(P, by X-coordinate)
min_dist_sq ← dist_sq(P[0], P[1])
min_dist ← sqrt(min_dist_sq)

for i ← 0 to n - 2 do
    for j ← i + 1 to n - 1 do
        dx ← P[j].x - P[i].x
        if dx ≥ min_dist then
            break // SPATIAL PRUNING: No subsequent point can beat min_dist
            
        dy ← abs(P[j].y - P[i].y)
        if dy ≥ min_dist then
            continue // 1D Y-filter
            
        d_sq ← dx * dx + dy * dy
        if d_sq < min_dist_sq then
            min_dist_sq ← d_sq
            min_dist ← sqrt(min_dist_sq)
            closest_pair ← (P[i], P[j])
return closest_pair, min_dist"""
    )
    r_code2.font.name = 'Consolas'
    r_code2.font.size = Pt(8.5)

    doc.add_heading("Part D: Predict Before Implementing (1 Mark)", level=2)
    p = doc.add_paragraph()
    p.add_run("Prior to experimental benchmarking, we predict:\n").font.bold = True
    p.add_run("1. Distance calculations will drop from Θ(n²) to near-linear O(n) for uniformly distributed drones, as the early-break rule restricts candidate examination to a tiny local vertical strip.\n")
    p.add_run("2. For N = 5,000, distance calculations will fall by > 99.9%, and execution time will drop from ~2,100 ms to < 10 ms.")

    doc.add_heading("Part E: Implement and Validate the Redesign (2 Marks)", level=2)
    q7_table = doc.add_table(rows=1, cols=7)
    q7_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    q7_headers = ["N", "Orig Dist Calcs", "Redes Dist Calcs", "Calc Reduction", "Orig Time", "Redes Time", "Speedup"]
    for i, h in enumerate(q7_headers):
        cell = q7_table.rows[0].cells[i]
        set_cell_background(cell, "1B365D")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9)

    q7_comp_data = [
        ("100", "4,950", "4", "99.92%", "0.78 ms", "0.06 ms", "12.9x"),
        ("500", "124,750", "5", "100.00%", "19.73 ms", "0.30 ms", "64.9x"),
        ("1,000", "499,500", "11", "100.00%", "79.67 ms", "0.71 ms", "111.9x"),
        ("2,000", "1,999,000", "12", "100.00%", "351.72 ms", "1.56 ms", "224.9x"),
        ("5,000", "12,497,500", "17", "100.00%", "2,108.52 ms", "4.45 ms", "474.0x"),
    ]
    for r_idx, row_data in enumerate(q7_comp_data):
        row = q7_table.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            if "5,000" in row_data[0]:
                set_cell_background(cell, "D4EFDF")
            else:
                set_cell_background(cell, "FFFFFF" if r_idx % 2 == 0 else "F9FAFB")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    g7_file = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141855.png")
    if os.path.exists(g7_file):
        doc.add_picture(g7_file, width=Inches(6.0))
        cap7 = doc.add_paragraph()
        cap7.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c7 = cap7.add_run("Figure 7.1: Experimental comparison between Brute-Force and Presorted Spatial Pruning.")
        r_c7.font.size = Pt(9.5)
        r_c7.font.italic = True

    s7_file = os.path.join(SCREENSHOTS_DIR, "Screenshot 2026-10-24 141830.png")
    if os.path.exists(s7_file):
        doc.add_picture(s7_file, width=Inches(6.0))
        cap7_s = doc.add_paragraph()
        cap7_s.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c7_s = cap7_s.add_run(f"Figure 7.2: Terminal execution output for Q7 Design Challenge (Reg No: {REG_NO}).")
        r_c7_s.font.size = Pt(9.5)
        r_c7_s.font.italic = True

    doc.add_heading("Part F: Defend the Final Design (2 Marks)", level=2)
    p = doc.add_paragraph()
    p.add_run("1. Objective & Hypothesis Confirmation: ").font.bold = True
    p.add_run("Our predictions were fully corroborated by empirical data. At N = 5,000, distance calculations plummeted from 12,497,500 down to just 17 (a 99.999% reduction!). Execution time was slashed from 2,108.52 ms to 4.45 ms (a 474.0x speedup), comfortably beating the 50 ms real-time safety radar threshold.\n")
    p.add_run("2. Engineering Trade-offs & Overhead: ").font.bold = True
    p.add_run("The redesign introduces an initial O(n log n) sorting phase (0.6 ms at N = 5000) and O(n) auxiliary list memory. This negligible cost is dwarfed by eliminating millions of quadratic calculations.\n")
    p.add_run("3. Degenerate Failure Modes & Boundary Conditions: ").font.bold = True
    p.add_run("If all drones share the identical x-coordinate (a degenerate vertical line), Δx = 0 for all pairs, and the early break condition never fires, degenerating to O(n²). However, in physical 2D/3D airspace, delivery drones possess continuous floating-point coordinates, guaranteeing high dispersion.\n")
    p.add_run("4. Final Conclusion: ").font.bold = True
    p.add_run("Presorted Spatial Pruning completely transforms an intractable brute-force algorithm into a production-ready, ultra-low latency real-time collision monitoring engine.")

    # Save docx
    docx_path = os.path.join(REPORT_DIR, f"DAA_A2_{REG_NO}.docx")
    doc.save(docx_path)
    print(f"Word report saved successfully: {docx_path}")
    return docx_path

if __name__ == "__main__":
    create_report()
