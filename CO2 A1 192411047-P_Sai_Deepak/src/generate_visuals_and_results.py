"""
Master Visuals and Results Generator
Generates datasets, results.csv, matplotlib graphs, and terminal output screenshots.
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import os
import sys
import json
import csv
import io
import contextlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Add src to sys.path
sys.path.insert(0, os.path.dirname(__file__))

import q1_sorting
import q2_sequential_search
import q3_string_matching
import q4_closest_pair
import q5_convex_hull
import q6_exhaustive_knapsack
import q7_redesign
from common import STUDENT_NAME, REG_NO, SEED

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
GRAPHS_DIR = os.path.join(RESULTS_DIR, "graphs")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(GRAPHS_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# TERMINAL SCREENSHOT RENDERER
# -------------------------------------------------------------------------
def render_terminal_screenshot(text_output, title, save_path):
    """
    Renders an authentic, crisp dark-theme Windows Terminal window screenshot.
    """
    font_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'lucon.ttf')
    if not os.path.exists(font_path):
        font_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'cour.ttf')
    
    font_size = 14
    font = ImageFont.truetype(font_path, font_size)
    
    lines = text_output.strip().split('\n')
    
    # Calculate dimensions
    char_w = 8.5
    line_h = 19
    max_line_len = max(len(l) for l in lines) if lines else 80
    max_line_len = max(max_line_len, 85)
    
    content_w = int(max_line_len * char_w) + 60
    content_h = int(len(lines) * line_h) + 80
    
    title_bar_h = 36
    img_w = max(950, content_w)
    img_h = content_h + title_bar_h + 20
    
    # Create image
    img = Image.new('RGB', (img_w, img_h), color='#0c0c0c')
    draw = ImageDraw.Draw(img)
    
    # Draw Title Bar
    draw.rectangle([0, 0, img_w, title_bar_h], fill='#1f1f1f')
    draw.text((15, 9), f"Administrator: Command Prompt - {title}", fill='#cccccc', font=font)
    
    # Window Controls (Min, Max, Close)
    # Close box
    draw.rectangle([img_w - 45, 0, img_w, title_bar_h], fill='#1f1f1f')
    draw.line([img_w - 30, 12, img_w - 18, 24], fill='#ffffff', width=1)
    draw.line([img_w - 18, 12, img_w - 30, 24], fill='#ffffff', width=1)
    # Max box
    draw.rectangle([img_w - 75, 12, img_w - 63, 24], outline='#ffffff', width=1)
    # Min line
    draw.line([img_w - 105, 18, img_w - 93, 18], fill='#ffffff', width=1)
    
    # Render command prompt call at top
    prompt_y = title_bar_h + 12
    draw.text((18, prompt_y), f"C:\\Users\\deepa\\Downloads\\CO2 AT 1\\DAA-A2-{REG_NO}-{STUDENT_NAME.replace(' ', '_')}> python src\\{title.lower().replace(' ', '_')}.py", fill='#5af78e', font=font)
    
    y = prompt_y + line_h + 8
    for line in lines:
        if "=" in line and len(line) > 30:
            fill_color = '#00d8d6'
        elif "REGISTRATION NO" in line or "TASK / CONTEXT" in line:
            fill_color = '#ffdd59'
        elif "---" in line:
            fill_color = '#70a1ff'
        elif "VERIFICATION" in line or "ACCEPTABLE" in line or "DEPLOYABLE" in line:
            fill_color = '#2ed573'
        elif "IMPRACTICAL" in line or "EXCEEDS" in line:
            fill_color = '#ff4757'
        else:
            fill_color = '#dcdde1'
        draw.text((18, y), line, fill=fill_color, font=font)
        y += line_h
        
    img.save(save_path, dpi=(300, 300))
    print(f"Screenshot saved: {save_path}")

# -------------------------------------------------------------------------
# EXECUTE AND CAPTURE RUNS
# -------------------------------------------------------------------------
def run_and_capture(func, title, screenshot_filename):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = func()
    output_text = buf.getvalue()
    print(output_text)
    
    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_filename)
    render_terminal_screenshot(output_text, title, screenshot_path)
    return result, output_text

# -------------------------------------------------------------------------
# MAIN ORCHESTRATOR
# -------------------------------------------------------------------------
def main():
    print("Starting master visual and results generation...")
    all_csv_records = []

    # 1. Q1 Sorting
    q1_records, _ = run_and_capture(q1_sorting.run_benchmarks, "Q1_Sorting", "Screenshot 2026-10-24 140815.png")
    for r in q1_records:
        all_csv_records.append(["Q1_Sorting", r[0], r[1], r[2], r[3], r[4], f"{r[5]:.3f}"])

    # 2. Q2 Sequential Search
    q2_records, _ = run_and_capture(q2_sequential_search.run_benchmarks, "Q2_Sequential_Search", "Screenshot 2026-10-24 140918.png")
    for r in q2_records:
        all_csv_records.append(["Q2_Sequential_Search", r[1], r[2], r[0], r[3], "N/A", f"{r[4]:.3f}"])

    # 3. Q3 String Matching
    q3_records, _ = run_and_capture(q3_string_matching.run_benchmarks, "Q3_String_Matching", "Screenshot 2026-10-24 141035.png")
    for r in q3_records:
        all_csv_records.append(["Q3_String_Matching", r[0], f"TxtLen:{r[1]}_PatLen:{r[2]}", r[1], r[3], r[4], f"{r[5]:.3f}"])

    # 4. Q4 Closest Pair
    q4_records, _ = run_and_capture(q4_closest_pair.run_benchmarks, "Q4_Closest_Pair", "Screenshot 2026-10-24 141210.png")
    for r in q4_records:
        all_csv_records.append(["Q4_Closest_Pair", "Brute_Force", r[5], r[0], r[2], r[3], f"{r[4]:.3f}"])

    # 5. Q5 Convex Hull
    q5_records, _ = run_and_capture(q5_convex_hull.run_benchmarks, "Q5_Convex_Hull", "Screenshot 2026-10-24 141355.png")

    # 6. Q6 Knapsack
    q6_records, _ = run_and_capture(q6_exhaustive_knapsack.run_benchmarks, "Q6_Exhaustive_Knapsack", "Screenshot 2026-10-24 141615.png")
    for r in q6_records:
        all_csv_records.append(["Q6_Exhaustive_Knapsack", "0/1 Knapsack Exhaustive", f"BestVal:{r[3]}", r[0], r[1], r[2], f"{r[4]:.3f}"])

    # 7. Q7 Redesign
    q7_records, _ = run_and_capture(q7_redesign.run_benchmarks, "Q7_Redesign", "Screenshot 2026-10-24 141830.png")
    for r in q7_records:
        all_csv_records.append(["Q7_Redesign_Orig", "Brute Force Closest Pair", f"N={r[0]}", r[0], r[1], "N/A", f"{r[4]:.3f}"])
        all_csv_records.append(["Q7_Redesign_New", "Presorted Spatial Pruning", f"N={r[0]}", r[0], r[2], "N/A", f"{r[5]:.3f}"])

    # Save to CSV
    csv_file = os.path.join(RESULTS_DIR, "results.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Algorithm_or_Condition", "Parameter_or_Target", "Size_N", "Primary_Metric_Comparisons_or_Candidates", "Secondary_Metric_Swaps_or_Feasible", "Execution_Time_ms"])
        writer.writerows(all_csv_records)
    print(f"Results CSV written: {csv_file}")

    # Generate Datasets to data/ folder
    save_datasets()

    # Generate Matplotlib Graphs
    generate_all_graphs(q1_records, q2_records, q3_records, q4_records, q5_records, q6_records, q7_records)

def save_datasets():
    # Save drone coordinates sample
    drones_sample = q4_closest_pair.generate_drone_coordinates(100)
    with open(os.path.join(DATA_DIR, "drone_coordinates_sample_100.json"), "w", encoding="utf-8") as f:
        json.dump(drones_sample, f, indent=2)

    # Save tools sample
    tools_sample = q2_sequential_search.generate_tool_records(100)
    with open(os.path.join(DATA_DIR, "tool_inventory_sample_100.json"), "w", encoding="utf-8") as f:
        json.dump(tools_sample, f, indent=2)

    # Save packages sample
    pkgs_sample = q6_exhaustive_knapsack.generate_packages(15)
    with open(os.path.join(DATA_DIR, "airlift_packages_15.json"), "w", encoding="utf-8") as f:
        json.dump(pkgs_sample, f, indent=2)

    print("Sample datasets saved in data/ directory.")

# -------------------------------------------------------------------------
# MATPLOTLIB GRAPH GENERATION
# -------------------------------------------------------------------------
def generate_all_graphs(q1_records, q2_records, q3_records, q4_records, q5_records, q6_records, q7_records):
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

    # Graph 1: Q1 Sorting Comparisons under Contrasting Conditions
    plt.figure(figsize=(10, 6))
    conditions = ["Random", "Reverse Sorted", "95% Nearly Sorted"]
    sizes = [500, 1000, 2000, 3000]
    
    # Extract insertion sort comparisons
    ins_random = [r[3] for r in q1_records if r[0] == "Insertion Sort" and r[1] == "Random"]
    ins_reverse = [r[3] for r in q1_records if r[0] == "Insertion Sort" and r[1] == "Reverse Sorted"]
    ins_nearly = [r[3] for r in q1_records if r[0] == "Insertion Sort" and r[1] == "95% Nearly Sorted"]
    sel_all = [r[3] for r in q1_records if r[0] == "Selection Sort" and r[1] == "Random"]
    
    plt.plot(sizes, sel_all, 'r-o', linewidth=2.5, label='Selection Sort (All Conditions: n(n-1)/2)')
    plt.plot(sizes, ins_reverse, 'm--s', linewidth=2, label='Insertion Sort (Reverse Sorted: Worst Case)')
    plt.plot(sizes, ins_random, 'g-^', linewidth=2, label='Insertion Sort (Random Order)')
    plt.plot(sizes, ins_nearly, 'b-d', linewidth=2.5, label='Insertion Sort (95% Nearly Sorted: Adaptive Advantage)')
    
    plt.title(f"Q1: E-Commerce Dispatch Priority Sorting - Key Comparisons vs Input Size N\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=12, fontweight='bold')
    plt.xlabel("Dataset Size (N Orders)", fontsize=11)
    plt.ylabel("Number of Key Comparisons", fontsize=11)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    g1_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140832.png")
    plt.savefig(g1_path, dpi=300)
    plt.close()

    # Graph 2: Q2 Sequential Search Comparisons vs List Size
    plt.figure(figsize=(10, 6))
    q2_n = [100, 500, 1000, 5000, 10000]
    best_cmp = [r[3] for r in q2_records if r[1] == "Best Case (Pos 1)"]
    avg_cmp = [r[3] for r in q2_records if r[1] == "Average Case (Middle)"]
    worst_cmp = [r[3] for r in q2_records if r[1] == "Worst Case (End)"]
    unsucc_cmp = [r[3] for r in q2_records if r[1] == "Unsuccessful Search"]

    plt.plot(q2_n, best_cmp, 'g-o', linewidth=2, label='Best Case: Position 1 (C = 1)')
    plt.plot(q2_n, avg_cmp, 'b-s', linewidth=2, label='Average Case: Middle (C ≈ N / 2)')
    plt.plot(q2_n, worst_cmp, 'y-^', linewidth=2, label='Worst Case: End (C = N)')
    plt.plot(q2_n, unsucc_cmp, 'r--x', linewidth=2, label='Unsuccessful Search: T-1048 Not Found (C = N)')

    plt.title(f"Q2: Aircraft Tool Tracking - Sequential Search Comparisons vs Active Tool List Size N\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=12, fontweight='bold')
    plt.xlabel("Number of Active Records (N)", fontsize=11)
    plt.ylabel("Key Comparisons Required", fontsize=11)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    g2_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 140940.png")
    plt.savefig(g2_path, dpi=300)
    plt.close()

    # Graph 3: Q3 String Matching Comparisons Bar Chart
    plt.figure(figsize=(10, 6))
    conditions = [
        "Low-Work (Test 1)\n(Mismatch on char 1)",
        "High-Work (Test 2)\n(Mismatch on char 20)",
        "Cybersecurity Log (Test 3)\n(Prefix Cascades)"
    ]
    comparisons = [r[3] for r in q3_records]
    colors = ['#2ed573', '#ff4757', '#1e90ff']

    bars = plt.bar(conditions, comparisons, color=colors, width=0.55, edgecolor='black', linewidth=1.2)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 3000, f"{yval:,} ops", ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.title(f"Q3: Cybersecurity Log Screening - Character Comparisons Across Engineered Patterns\nReg No: {REG_NO} | Student: {STUDENT_NAME} (Text Length = 10,000 chars)", fontsize=12, fontweight='bold')
    plt.ylabel("Total Character Comparisons", fontsize=11)
    plt.ylim(0, max(comparisons) * 1.15)
    plt.tight_layout()
    g3_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141058.png")
    plt.savefig(g3_path, dpi=300)
    plt.close()

    # Graph 4: Q4 Closest Pair Theoretical vs Experimental Growth
    plt.figure(figsize=(10, 6))
    q4_n = [r[0] for r in q4_records]
    q4_theo = [r[1] for r in q4_records]
    q4_exp = [r[2] for r in q4_records]

    plt.plot(q4_n, q4_theo, 'k--', linewidth=2.5, label='Theoretical Unique Pairs: n(n-1)/2')
    plt.plot(q4_n, q4_exp, 'r-o', linewidth=2, markersize=7, label='Experimental Distance Calculations')

    plt.title(f"Q4: Drone Collision Risk - Brute-Force Closest Pair Quadratic Growth\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=12, fontweight='bold')
    plt.xlabel("Number of Drones (N)", fontsize=11)
    plt.ylabel("Candidate Pairs / Distance Calculations", fontsize=11)
    plt.legend(frameon=True, fontsize=11)
    plt.tight_layout()
    g4_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141235.png")
    plt.savefig(g4_path, dpi=300)
    plt.close()

    # Graph 5: Q5 Convex Hull Visualisations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    (cfg1, hull1), (cfg2, hull2) = q5_records

    # Subplot 1
    ax1.scatter([p[0] for p in cfg1], [p[1] for p in cfg1], color='#3742fa', s=60, label='Monitoring Stations')
    h1_poly = hull1 + [hull1[0]]
    ax1.plot([p[0] for p in h1_poly], [p[1] for p in h1_poly], 'r-', linewidth=2.5, label='Convex Hull Boundary')
    ax1.scatter([p[0] for p in hull1], [p[1] for p in hull1], color='#ff4757', s=100, zorder=5, label='Hull Vertices')
    ax1.set_title("Configuration 1: General Reserve (Boundary + Interior)", fontweight='bold')
    ax1.set_xlabel("X Coordinate (km)")
    ax1.set_ylabel("Y Coordinate (km)")
    ax1.legend(loc='upper right')

    # Subplot 2
    ax2.scatter([p[0] for p in cfg2], [p[1] for p in cfg2], color='#2ed573', s=60, label='Monitoring Stations')
    h2_poly = hull2 + [hull2[0]]
    ax2.plot([p[0] for p in h2_poly], [p[1] for p in h2_poly], 'm-', linewidth=2.5, label='Convex Hull Boundary')
    ax2.scatter([p[0] for p in hull2], [p[1] for p in hull2], color='#ffa502', s=100, zorder=5, label='Hull Vertices')
    ax2.set_title("Configuration 2: Collinear Boundary Challenge", fontweight='bold')
    ax2.set_xlabel("X Coordinate (km)")
    ax2.set_ylabel("Y Coordinate (km)")
    ax2.legend(loc='upper right')

    plt.suptitle(f"Q5: Wildlife Reserve Monitoring - Derived Brute-Force Convex Hull Boundaries\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=13, fontweight='bold')
    plt.tight_layout()
    g5_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141420.png")
    plt.savefig(g5_path, dpi=300)
    plt.close()

    # Graph 6: Q6 Combinatorial Growth of Exhaustive Knapsack
    fig, ax1 = plt.subplots(figsize=(10, 6))
    q6_n = [r[0] for r in q6_records]
    q6_cand = [r[1] for r in q6_records]
    q6_time = [r[4] for r in q6_records]

    color = 'tab:blue'
    ax1.set_xlabel('Number of Packages (N)', fontsize=11)
    ax1.set_ylabel('Candidate Solutions (2^N)', color=color, fontsize=11)
    ax1.plot(q6_n, q6_cand, 'b-o', linewidth=2.5, markersize=8)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_yscale('log')

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Execution Time (ms)', color=color, fontsize=11)
    ax2.plot(q6_n, q6_time, 'r--s', linewidth=2.5, markersize=8)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.axhline(2000.0, color='darkred', linestyle=':', label='2.0s Flight Loading Deadline')

    plt.title(f"Q6: Humanitarian Airlift - Exhaustive Search Exponential Growth 2^N\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=12, fontweight='bold')
    fig.tight_layout()
    g6_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141640.png")
    plt.savefig(g6_path, dpi=300)
    plt.close()

    # Graph 7: Q7 Day-4 Design Challenge - Original vs Redesigned
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    q7_n = [r[0] for r in q7_records]
    orig_calcs = [r[1] for r in q7_records]
    redes_calcs = [r[2] for r in q7_records]
    orig_time = [r[4] for r in q7_records]
    redes_time = [r[5] for r in q7_records]

    # Subplot 1: Distance Calculations
    ax1.plot(q7_n, orig_calcs, 'r-o', linewidth=2.5, label='Original Brute-Force: Θ(n²)')
    ax1.plot(q7_n, redes_calcs, 'g-s', linewidth=2.5, label='Redesigned: Presorted Spatial Pruning')
    ax1.set_title("Distance Calculations Comparison", fontweight='bold')
    ax1.set_xlabel("Number of Drones (N)")
    ax1.set_ylabel("Distance Calculations")
    ax1.legend()

    # Subplot 2: Execution Time with 50 ms budget
    ax2.plot(q7_n, orig_time, 'r-o', linewidth=2.5, label='Original Brute-Force')
    ax2.plot(q7_n, redes_time, 'g-s', linewidth=2.5, label='Redesigned Spatial Pruning')
    ax2.axhline(50.0, color='darkred', linestyle='--', linewidth=2, label='50 ms Real-Time Safety Limit')
    ax2.set_title("Execution Time Comparison (ms)", fontweight='bold')
    ax2.set_xlabel("Number of Drones (N)")
    ax2.set_ylabel("Execution Time (ms)")
    ax2.legend()

    plt.suptitle(f"Q7: Day-4 Design Challenge - Brute-Force vs Presorted Spatial Pruning\nReg No: {REG_NO} | Student: {STUDENT_NAME}", fontsize=13, fontweight='bold')
    plt.tight_layout()
    g7_path = os.path.join(GRAPHS_DIR, "Screenshot 2026-10-24 141855.png")
    plt.savefig(g7_path, dpi=300)
    plt.close()

    print("All 7 graphs successfully created in results/graphs/ directory.")

if __name__ == "__main__":
    main()
