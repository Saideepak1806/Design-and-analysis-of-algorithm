"""
Q2: When Is Sequential Search an Appropriate Engineering Choice?
Problem Context: Aircraft Maintenance Tool Tracking
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import random

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED

def generate_tool_records(n, target_tool_id="T-1047"):
    set_seed()
    records = []
    technicians = [f"TECH-{1000 + i}" for i in range(50)]
    work_bays = [f"BAY-{chr(65 + i % 6)}-{i % 10 + 1}" for i in range(20)]
    
    # Generate unique tool IDs
    tool_ids = set()
    while len(tool_ids) < n - 1:
        tid = f"T-{random.randint(1000, 99999)}"
        if tid != target_tool_id and tid != f"T-{SEED + 1}":
            tool_ids.add(tid)
    tool_list = list(tool_ids)
    
    # Insert target tool at middle by default
    insert_pos = n // 2
    tool_list.insert(insert_pos, target_tool_id)
    
    for i, tid in enumerate(tool_list):
        records.append({
            "tool_id": tid,
            "technician_id": random.choice(technicians),
            "issue_time": f"{random.randint(6, 18):02d}:{random.randint(0, 59):02d} UTC",
            "work_bay": random.choice(work_bays)
        })
    return records

def sequential_search(records, target_tool_id):
    comparisons = 0
    start = time.perf_counter()
    found_record = None
    for rec in records:
        comparisons += 1
        if rec["tool_id"] == target_tool_id:
            found_record = rec
            break
    duration = time.perf_counter() - start
    return found_record, comparisons, duration

def run_benchmarks():
    print_header("Q2: Aircraft Maintenance Tool Tracking - Sequential Search")
    
    personal_found_key = f"T-{SEED}"         # T-1047 (Found)
    personal_not_found_key = f"T-{SEED + 1}" # T-1048 (Not Found)
    
    sizes = [100, 500, 1000, 5000, 10000]
    results = []

    print(f"Personal Search Keys: Found Target = {personal_found_key} | Not-Found Target = {personal_not_found_key}")
    print("\n--- EXPERIMENTAL RESULTS TABLE ---")
    print(f"{'List Size (N)':<14} | {'Search Scenario':<22} | {'Target ID':<10} | {'Comparisons':<12} | {'Time (us)':<10} | {'Found?':<8}")
    print("-" * 88)

    for n in sizes:
        records = generate_tool_records(n, personal_found_key)
        
        # 1. Best Case (Position 0)
        # Put target at index 0
        records[0]["tool_id"] = personal_found_key
        _, cmp_best, t_best = sequential_search(records, personal_found_key)
        results.append((n, "Best Case (Pos 1)", personal_found_key, cmp_best, t_best * 1e6, True))
        print(f"{n:<14} | {'Best Case (Pos 1)':<22} | {personal_found_key:<10} | {cmp_best:<12} | {t_best*1e6:<10.2f} | {'Yes':<8}")
        
        # 2. Average Case (Middle Position n // 2)
        records[0]["tool_id"] = "T-TEMP-001"
        records[n // 2]["tool_id"] = personal_found_key
        _, cmp_avg, t_avg = sequential_search(records, personal_found_key)
        results.append((n, "Average Case (Middle)", personal_found_key, cmp_avg, t_avg * 1e6, True))
        print(f"{n:<14} | {'Average Case (Middle)':<22} | {personal_found_key:<10} | {cmp_avg:<12} | {t_avg*1e6:<10.2f} | {'Yes':<8}")
        
        # 3. Worst Case (End Position n - 1)
        records[n // 2]["tool_id"] = "T-TEMP-002"
        records[n - 1]["tool_id"] = personal_found_key
        _, cmp_worst, t_worst = sequential_search(records, personal_found_key)
        results.append((n, "Worst Case (End)", personal_found_key, cmp_worst, t_worst * 1e6, True))
        print(f"{n:<14} | {'Worst Case (End)':<22} | {personal_found_key:<10} | {cmp_worst:<12} | {t_worst*1e6:<10.2f} | {'Yes':<8}")

        # 4. Unsuccessful Search
        records[n - 1]["tool_id"] = "T-TEMP-003" # target not in records
        _, cmp_unsucc, t_unsucc = sequential_search(records, personal_not_found_key)
        results.append((n, "Unsuccessful Search", personal_not_found_key, cmp_unsucc, t_unsucc * 1e6, False))
        print(f"{n:<14} | {'Unsuccessful Search':<22} | {personal_not_found_key:<10} | {cmp_unsucc:<12} | {t_unsucc*1e6:<10.2f} | {'No':<8}")
        print("-" * 88)

    return results

if __name__ == "__main__":
    run_benchmarks()
