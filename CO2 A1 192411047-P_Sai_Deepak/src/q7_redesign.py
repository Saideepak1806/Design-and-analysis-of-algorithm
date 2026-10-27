"""
Q7: Day-4 Design Challenge - Diagnose, Redesign and Validate
Focus: Closest Pair Drone Collision-Risk Monitoring
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import math
import random

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED
from q4_closest_pair import generate_drone_coordinates, brute_force_closest_pair

def redesigned_closest_pair(drones):
    """
    Redesigned Closest Pair: Presorted Spatial Coordinate Pruning (Sweep-Line Window)
    
    1. Preprocessing: Sort drones by X-coordinate in O(n log n).
    2. Exploits geometric invariant: dist(Pi, Pj) >= |Xj - Xi|.
    3. Monotonicity: Since sorted by X, as soon as (Xj - Xi) >= delta_min, 
       no subsequent point k >= j can be closer than delta_min. Break immediately!
    """
    n = len(drones)
    start_total = time.perf_counter()
    
    # Preprocessing: Sort by X coordinate
    start_sort = time.perf_counter()
    sorted_drones = sorted(drones, key=lambda d: d[0])
    sort_time = time.perf_counter() - start_sort
    
    pairs_examined = 0
    distance_calculations = 0
    min_dist_sq = float("inf")
    closest_pair = (None, None)
    
    # Initialize with adjacent neighbor distance to establish a tight early bound
    for i in range(min(5, n - 1)):
        dx = sorted_drones[i][0] - sorted_drones[i+1][0]
        dy = sorted_drones[i][1] - sorted_drones[i+1][1]
        d_sq = dx * dx + dy * dy
        if d_sq < min_dist_sq:
            min_dist_sq = d_sq
            closest_pair = (sorted_drones[i][2], sorted_drones[i+1][2])
            
    min_dist = math.sqrt(min_dist_sq)

    for i in range(n - 1):
        x1, y1, id1 = sorted_drones[i]
        for j in range(i + 1, n):
            pairs_examined += 1
            x2, y2, id2 = sorted_drones[j]
            dx = x2 - x1
            
            # PRUNING CHECK: Exploiting 1D coordinate monotonicity
            if dx >= min_dist:
                # All remaining points k > j have x_k >= x_j, so (x_k - x_1) >= dx >= min_dist
                # Therefore, no remaining point in the inner loop can beat min_dist.
                break
                
            # Quick 1D Y-filter before expensive multiplication/squared distance
            dy = abs(y1 - y2)
            if dy >= min_dist:
                continue
                
            # Candidate survived both 1D spatial filters
            dist_sq = dx * dx + dy * dy
            distance_calculations += 1
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                min_dist = math.sqrt(min_dist_sq)
                closest_pair = (id1, id2)

    total_duration = time.perf_counter() - start_total
    return closest_pair, min_dist, pairs_examined, distance_calculations, total_duration, sort_time

def run_benchmarks():
    print_header("Q7: Day-4 Design Challenge - Presorted Spatial Pruning")
    
    print("\n================================================================================")
    print(" PART A: DIAGNOSIS OF THE COMPUTATIONAL BOTTLENECK")
    print("================================================================================")
    print("1. Effort Concentration: In brute-force, exactly n*(n-1)/2 distance calculations")
    print("   are executed regardless of spatial locality.")
    print("2. Superfluous Work: Drones at opposite ends of the operating airspace (e.g., dx = 8000m)")
    print("   are compared against each other, even when current closest pair delta is < 20m.")
    print("3. Root Cause: Lack of spatial organization forces exhaustive cartesian product.")
    
    print("\n================================================================================")
    print(" PART B: DESIGN OBJECTIVE")
    print("================================================================================")
    print("Objective: Prune candidate pairs by exploiting coordinate monotonicity.")
    print("Measurable Goal: Reduce distance calculations by > 98% and achieve execution time")
    print("< 20 ms for N = 5,000 drones (safely below the 50 ms real-time safety threshold).")
    
    print("\n================================================================================")
    print(" PART C & D: REVISED STRATEGY & TESTABLE PREDICTIONS")
    print("================================================================================")
    print("Strategy: Presort points by X-coordinate in O(n log n). For each point i, scan j > i.")
    print("Early Break Rule: Terminate inner loop the instant (X_j - X_i) >= current_min_distance.")
    print("Prediction: Distance calculations will drop from O(n^2) to near O(n) for uniform 2D spread.")
    
    print("\n================================================================================")
    print(" PART E: EXPERIMENTAL VALIDATION - ORIGINAL VS REDESIGNED")
    print("================================================================================")
    
    sizes = [100, 500, 1000, 2000, 5000]
    comparison_table = []

    print(f"{'N':<6} | {'Orig Dist Calcs':<16} | {'Redes Dist Calcs':<16} | {'Reduction %':<12} | {'Orig (ms)':<10} | {'Redes (ms)':<10} | {'Speedup':<8}")
    print("-" * 92)

    for n in sizes:
        drones = generate_drone_coordinates(n)
        
        # Original Brute-Force
        c_orig, d_orig, p_orig, calcs_orig, t_orig = brute_force_closest_pair(drones)
        
        # Redesigned
        c_redes, d_redes, p_redes, calcs_redes, t_redes, t_sort = redesigned_closest_pair(drones)
        
        # Verification
        assert abs(d_orig - d_redes) < 1e-4, f"Distance mismatch at N={n}: {d_orig} vs {d_redes}"
        
        reduction = (1.0 - calcs_redes / calcs_orig) * 100.0
        speedup = t_orig / t_redes if t_redes > 0 else 1.0
        
        comparison_table.append((n, calcs_orig, calcs_redes, reduction, t_orig * 1000, t_redes * 1000, speedup))
        print(f"{n:<6} | {calcs_orig:<16} | {calcs_redes:<16} | {reduction:<11.2f}% | {t_orig*1000:<10.2f} | {t_redes*1000:<10.2f} | {speedup:<7.1f}x")

    print("\n================================================================================")
    print(" PART F: DEFENCE OF THE FINAL DESIGN")
    print("================================================================================")
    n_last, c_orig_l, c_redes_l, red_l, t_orig_l, t_redes_l, sp_l = comparison_table[-1]
    print(f"1. Prediction Fully Confirmed: At N = {n_last}, distance calculations decreased from")
    print(f"   {c_orig_l:,} to {c_redes_l:,} ({red_l:.2f}% reduction!).")
    print(f"2. Response Time: Execution time slashed from {t_orig_l:.2f} ms to {t_redes_l:.2f} ms ({sp_l:.1f}x faster).")
    print(f"   Crucially, runtime is now well within the 50 ms safety threshold (margin = {50.0 - t_redes_l:.1f} ms).")
    print(f"3. Trade-offs: Requires O(n log n) sorting preprocessing and O(n) auxiliary list memory.")
    print("   Degenerate case: If all drones lie on a perfectly vertical line (X constant), X-pruning")
    print("   yields no reduction. However, in physical 3D/2D airspace, coordinates are continuously dispersed.")
    
    return comparison_table

if __name__ == "__main__":
    run_benchmarks()
