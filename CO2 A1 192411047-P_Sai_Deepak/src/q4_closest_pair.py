"""
Q4: Closest Pair and the Cost of Examining Every Possibility
Problem Context: Drone Collision-Risk Monitoring
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import math
import random

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED

def generate_drone_coordinates(n, area_size=10000.0):
    set_seed()
    drones = []
    for i in range(n):
        x = round(random.uniform(0.0, area_size), 2)
        y = round(random.uniform(0.0, area_size), 2)
        drones.append((x, y, f"DRONE-{i+1}"))
    return drones

def brute_force_closest_pair(drones):
    n = len(drones)
    pairs_examined = 0
    distance_calculations = 0
    min_dist_sq = float("inf")
    closest_pair = (None, None)

    start = time.perf_counter()
    for i in range(n - 1):
        x1, y1, id1 = drones[i]
        for j in range(i + 1, n):
            pairs_examined += 1
            x2, y2, id2 = drones[j]
            dx = x1 - x2
            dy = y1 - y2
            dist_sq = dx * dx + dy * dy
            distance_calculations += 1
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                closest_pair = (id1, id2)

    min_dist = math.sqrt(min_dist_sq) if min_dist_sq != float("inf") else 0.0
    duration = time.perf_counter() - start
    return closest_pair, min_dist, pairs_examined, distance_calculations, duration

def run_benchmarks():
    print_header("Q4: Drone Collision-Risk Monitoring - Brute-Force Closest Pair")
    
    sizes = [100, 500, 1000, 2000, 4000]
    records = []

    print("\n--- EXPERIMENTAL RESULTS TABLE ---")
    print(f"{'Drones (N)':<11} | {'Theoretical Pairs':<18} | {'Pairs Examined':<15} | {'Dist Calcs':<12} | {'Time (ms)':<10} | {'Closest Drones':<24} | {'Min Dist (m)':<12}")
    print("-" * 110)

    for n in sizes:
        drones = generate_drone_coordinates(n)
        theoretical_pairs = n * (n - 1) // 2
        (d1, d2), min_d, p_exam, d_calcs, dur = brute_force_closest_pair(drones)
        records.append((n, theoretical_pairs, p_exam, d_calcs, dur * 1000, f"{d1} & {d2}", min_d))
        print(f"{n:<11} | {theoretical_pairs:<18} | {p_exam:<15} | {d_calcs:<12} | {dur*1000:<10.2f} | {f'{d1} & {d2}':<24} | {min_d:<12.2f}")

    print("\n--- THEORETICAL DERIVATION VERIFICATION ---")
    print("Formula: Unique Pairs = n * (n - 1) / 2")
    for n, theo, p_exam, _, _, _, _ in records:
        print(f"For N = {n:4d}: Theoretical = {theo:10d} | Experimental = {p_exam:10d} | Mismatch = {theo - p_exam}")

    print("\n--- SCALABILITY & ACCEPTABILITY INQUIRY ---")
    print("Acceptable Response Time Budget : 50.0 ms (20 Hz safety radar refresh rate)")
    for n, _, _, _, t_ms, _, _ in records:
        status = "ACCEPTABLE" if t_ms <= 50.0 else "IMPRACTICAL (EXCEEDS SAFETY BUDGET)"
        print(f"N = {n:4d} : Time = {t_ms:8.2f} ms --> {status}")

    return records

if __name__ == "__main__":
    run_benchmarks()
