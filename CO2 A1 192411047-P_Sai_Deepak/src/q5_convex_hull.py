"""
Q5: Derive a Convex Hull Algorithm from a Geometric Principle
Problem Context: Wildlife Reserve Boundary Monitoring
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import math
import random

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED

def cross_product(p1, p2, p3):
    """
    Computes (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1).
    > 0 : p3 is to the left of directed line p1->p2
    < 0 : p3 is to the right of directed line p1->p2
    = 0 : collinear
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def brute_force_convex_hull(points):
    """
    Brute-force convex hull derived directly from the geometric principle:
    A line joining two candidate points forms part of the outer boundary 
    if all remaining points lie on an appropriate single side of that line.
    """
    n = len(points)
    hull_edges = set()
    pairs_examined = 0
    point_line_tests = 0

    start = time.perf_counter()
    for i in range(n):
        for j in range(i + 1, n):
            pairs_examined += 1
            p1 = points[i]
            p2 = points[j]
            
            # Line equation coefficients: a*x + b*y = c
            # a = y2 - y1, b = x1 - x2, c = x1*y2 - y1*x2
            a = p2[1] - p1[1]
            b = p1[0] - p2[0]
            c = p1[0] * p2[1] - p1[1] * p2[0]

            has_positive = False
            has_negative = False

            for k in range(n):
                if k == i or k == j:
                    continue
                point_line_tests += 1
                val = a * points[k][0] + b * points[k][1] - c
                
                # Tolerating tiny floating precision
                if val > 1e-7:
                    has_positive = True
                elif val < -1e-7:
                    has_negative = True

                # If points exist on both sides, this edge cannot be on the outer boundary
                if has_positive and has_negative:
                    break

            if not (has_positive and has_negative):
                # All remaining points lie on one side (or collinear)
                hull_edges.add((p1, p2))

    duration = time.perf_counter() - start

    # Extract unique vertices from hull edges
    hull_vertices = set()
    for p1, p2 in hull_edges:
        hull_vertices.add(p1)
        hull_vertices.add(p2)

    # Sort hull vertices counter-clockwise around centroid to form a closed polygon
    if hull_vertices:
        cx = sum(p[0] for p in hull_vertices) / len(hull_vertices)
        cy = sum(p[1] for p in hull_vertices) / len(hull_vertices)
        ordered_hull = sorted(list(hull_vertices), key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    else:
        ordered_hull = []

    return ordered_hull, list(hull_edges), pairs_examined, point_line_tests, duration

def generate_wildlife_reserve_datasets():
    set_seed()
    # Configuration 1: General Reserve with interior stations & exterior boundary
    # Elliptical ring of outer stations + uniformly scattered interior stations
    pts_config1 = []
    # 10 outer perimeter points
    for theta in [i * (2 * math.pi / 10) for i in range(10)]:
        x = round(50.0 + 40.0 * math.cos(theta) + random.uniform(-2, 2), 2)
        y = round(50.0 + 35.0 * math.sin(theta) + random.uniform(-2, 2), 2)
        pts_config1.append((x, y))
    # 15 interior stations
    for _ in range(15):
        r = random.uniform(5.0, 25.0)
        ang = random.uniform(0, 2 * math.pi)
        pts_config1.append((round(50.0 + r * math.cos(ang), 2), round(50.0 + r * math.sin(ang), 2)))

    # Configuration 2: Deliberately challenging dataset
    # Collinear boundary points along a rectangle + interior dense cluster
    pts_config2 = [
        # Collinear points along bottom boundary
        (10.0, 10.0), (30.0, 10.0), (50.0, 10.0), (70.0, 10.0), (90.0, 10.0),
        # Right boundary
        (90.0, 40.0), (90.0, 80.0),
        # Top boundary collinear
        (90.0, 90.0), (50.0, 90.0), (10.0, 90.0),
        # Left boundary
        (10.0, 50.0),
        # Interior points
        (35.0, 45.0), (50.0, 50.0), (65.0, 55.0), (40.0, 60.0), (60.0, 35.0)
    ]

    return pts_config1, pts_config2

def run_benchmarks():
    print_header("Q5: Wildlife Reserve Boundary Monitoring - Brute-Force Convex Hull")
    cfg1, cfg2 = generate_wildlife_reserve_datasets()

    print("\n--- TEST EXECUTION: CONFIGURATION 1 (Boundary & Interior Stations) ---")
    hull1, edges1, pairs1, tests1, t1 = brute_force_convex_hull(cfg1)
    print(f"Total Stations (N)      : {len(cfg1)}")
    print(f"Candidate Pairs Examined : {pairs1} (Theoretical n*(n-1)/2 = {len(cfg1)*(len(cfg1)-1)//2})")
    print(f"Point-Line Side Tests   : {tests1}")
    print(f"Boundary Edges Found    : {len(edges1)}")
    print(f"Hull Vertices Identified: {len(hull1)}")
    print(f"Execution Time          : {t1*1000:.3f} ms")
    print("Ordered Boundary Polygon Vertices:")
    for idx, pt in enumerate(hull1):
        print(f"  V{idx+1}: ({pt[0]:.2f}, {pt[1]:.2f})")

    print("\n--- TEST EXECUTION: CONFIGURATION 2 (Collinear Challenge Dataset) ---")
    hull2, edges2, pairs2, tests2, t2 = brute_force_convex_hull(cfg2)
    print(f"Total Stations (N)      : {len(cfg2)}")
    print(f"Candidate Pairs Examined : {pairs2}")
    print(f"Point-Line Side Tests   : {tests2}")
    print(f"Boundary Edges Found    : {len(edges2)}")
    print(f"Hull Vertices Identified: {len(hull2)}")
    print(f"Execution Time          : {t2*1000:.3f} ms")
    print("Ordered Boundary Polygon Vertices:")
    for idx, pt in enumerate(hull2):
        print(f"  V{idx+1}: ({pt[0]:.2f}, {pt[1]:.2f})")

    # Scalability study across N
    print("\n--- COMPUTATIONAL WORK GROWTH ANALYSIS ---")
    print(f"{'Stations (N)':<14} | {'Pairs Examined':<16} | {'Max Point Tests':<18} | {'Observed Tests':<16} | {'Time (ms)':<10}")
    print("-" * 80)
    for test_n in [15, 25, 40, 60, 100]:
        test_pts = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(test_n)]
        _, _, p_ex, pt_tests, dur = brute_force_convex_hull(test_pts)
        max_tests = p_ex * (test_n - 2)
        print(f"{test_n:<14} | {p_ex:<16} | {max_tests:<18} | {pt_tests:<16} | {dur*1000:<10.2f}")

    return (cfg1, hull1), (cfg2, hull2)

if __name__ == "__main__":
    run_benchmarks()
