"""
Q6: Exhaustive Search and Combinatorial Growth
Problem Context: Humanitarian Airlift Planning (0/1 Knapsack)
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import random

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED

def generate_packages(n):
    set_seed()
    packages = []
    # Package categories: Meds, Water, High-calorie rations, Shelter, Communications
    types = ["MEDS", "WATER", "RATION", "SHELTER", "COMMS"]
    for i in range(n):
        pkg_id = f"PKG-{types[i % len(types)]}-{i+1:02d}"
        weight = random.randint(10, 80)        # kg
        value = random.randint(20, 200)        # humanitarian priority points
        packages.append({"id": pkg_id, "weight": weight, "value": value})
    return packages

def exhaustive_knapsack(packages, capacity):
    n = len(packages)
    total_candidates = 1 << n
    best_value = -1
    best_weight = 0
    best_subset = []
    feasible_count = 0

    start = time.perf_counter()
    for mask in range(total_candidates):
        cur_weight = 0
        cur_value = 0
        cur_subset = []
        is_feasible = True

        for i in range(n):
            if (mask >> i) & 1:
                cur_weight += packages[i]["weight"]
                if cur_weight > capacity:
                    is_feasible = False
                    break
                cur_value += packages[i]["value"]
                cur_subset.append(packages[i])

        if is_feasible:
            feasible_count += 1
            if cur_value > best_value:
                best_value = cur_value
                best_weight = cur_weight
                best_subset = cur_subset

    duration = time.perf_counter() - start
    return best_subset, best_value, best_weight, total_candidates, feasible_count, duration

def verify_small_instance():
    print("\n--- CORRECTNESS CHECK: SMALL 4-PACKAGE INSTANCE TRUTH TABLE ---")
    small_pkgs = [
        {"id": "PKG-MEDS-01", "weight": 20, "value": 70},
        {"id": "PKG-WATER-02", "weight": 30, "value": 80},
        {"id": "PKG-RATION-03", "weight": 40, "value": 90},
        {"id": "PKG-COMMS-04", "weight": 15, "value": 60}
    ]
    cap = 50
    print(f"Payload Capacity: {cap} kg\nAvailable Packages:")
    for p in small_pkgs:
        print(f"  {p['id']:<14} | Weight: {p['weight']} kg | Value: {p['value']} pts")

    print(f"\n{'Mask':<6} | {'Binary':<6} | {'Selected Items':<35} | {'Weight (kg)':<12} | {'Value (pts)':<12} | {'Feasible?':<10}")
    print("-" * 90)

    best_val = -1
    best_mask = -1
    for m in range(16):
        w = sum(small_pkgs[i]["weight"] for i in range(4) if (m >> i) & 1)
        v = sum(small_pkgs[i]["value"] for i in range(4) if (m >> i) & 1)
        items = [small_pkgs[i]["id"] for i in range(4) if (m >> i) & 1]
        items_str = ", ".join(items) if items else "None (Empty)"
        feas = "YES" if w <= cap else "NO (Overweight)"
        if w <= cap and v > best_val:
            best_val = v
            best_mask = m
        print(f"{m:<6} | {m:04b} | {items_str:<35} | {w:<12} | {v:<12} | {feas:<10}")

    print("-" * 90)
    print(f"Exhaustive Search Optimum Identified: Mask {best_mask} ({best_mask:04b}) with Value = {best_val} pts.")
    print("Independent Manual Verification: Combination {PKG-MEDS-01, PKG-COMMS-04, PKG-WATER-02} has weight 20+15+30=65>50 (Invalid).")
    print("Combination {PKG-MEDS-01, PKG-COMMS-04} weight 35 kg, value 130 pts. Combination {PKG-RATION-03, PKG-COMMS-04} weight 55>50.")
    print("Combination {PKG-WATER-02, PKG-COMMS-04} weight 45 kg, value 140 pts.")
    print("Combination {PKG-MEDS-01, PKG-WATER-02} weight 50 kg, value 70+80 = 150 pts. (Optimum verified!)")

def run_benchmarks():
    print_header("Q6: Humanitarian Airlift Planning - Exhaustive Search")
    verify_small_instance()

    print("\n--- COMBINATORIAL GROWTH EXPERIMENT ---")
    print(f"{'Packages (N)':<14} | {'Candidate Space (2^N)':<24} | {'Feasible Subsets':<18} | {'Best Value':<12} | {'Time (ms)':<12} | {'Ops/sec':<14}")
    print("-" * 102)

    sizes = [10, 14, 18, 22]
    growth_data = []

    for n in sizes:
        pkgs = generate_packages(n)
        cap = int(sum(p["weight"] for p in pkgs) * 0.4) # 40% of total available weight
        best_sub, best_v, best_w, total_cand, feas_cnt, dur = exhaustive_knapsack(pkgs, cap)
        ops_per_sec = total_cand / dur if dur > 0 else 0
        growth_data.append((n, total_cand, feas_cnt, best_v, dur * 1000, ops_per_sec))
        print(f"{n:<14} | {total_cand:<24} | {feas_cnt:<18} | {best_v:<12} | {dur*1000:<12.2f} | {ops_per_sec:<14.0f}")

    print("\n--- DEPLOYMENT DECISION & OPERATIONAL BOUNDARY ---")
    print("Airlift Operational Deadline : 2000.0 ms (2.0 seconds emergency flight loading decision)")
    for n, cand, _, _, t_ms, _ in growth_data:
        status = "DEPLOYABLE" if t_ms <= 2000.0 else "EXCEEDS DEADLINE (NOT DEPLOYABLE)"
        print(f"N = {n:2d} ({cand:>10} candidates) -> Execution Time = {t_ms:9.2f} ms --> {status}")
    
    print("\nExtrapolation to N = 30 packages:")
    print("Theoretical Candidates = 2^30 = 1,073,741,824")
    estimated_sec = 1073741824 / growth_data[-1][5]
    print(f"Estimated Execution Time = {estimated_sec:.1f} seconds ({estimated_sec/60:.2f} minutes) on standard CPU.")
    print("Conclusion: Exhaustive search deployment boundary is strictly N <= 22.")

    return growth_data

if __name__ == "__main__":
    run_benchmarks()
