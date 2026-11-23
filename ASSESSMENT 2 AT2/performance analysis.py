
"""
CSA06 - Design and Analysis of Algorithms
Part D - Performance Analysis

Student Name: PINDIBOINA SAI DEEPAK
Register Number: 192411047
"""

import math
import random
import time


def brute_force_closest(events):
    n = len(events)
    min_dist = math.inf
    pair = None
    count = 0

    for i in range(n):
        for j in range(n):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            d = math.sqrt(dx * dx + dy * dy)
            count += 1

            if i != j and d < min_dist:
                min_dist = d
                pair = (i, j)

    return pair, min_dist, count


def optimised_closest(events):
    n = len(events)

    if n < 2:
        return None, math.inf, 0

    points = sorted(
        [(x, y, index) for index, (x, y) in enumerate(events)],
        key=lambda p: (p[0], p[1], p[2])
    )

    best_sq = math.inf
    best_pair = None
    count = 0

    for i in range(n):
        x1, y1, index1 = points[i]

        for j in range(i + 1, n):
            x2, y2, index2 = points[j]

            dx = x2 - x1

            if dx * dx > best_sq:
                break

            dy = y2 - y1

            if dy * dy > best_sq:
                continue

            d2 = dx * dx + dy * dy
            count += 1

            pair = tuple(sorted((index1, index2)))

            if d2 < best_sq or (
                d2 == best_sq and
                (best_pair is None or pair < best_pair)
            ):
                best_sq = d2
                best_pair = pair

    return best_pair, math.sqrt(best_sq), count


def insertion_sort_count(alerts):
    data = alerts.copy()
    comparisons = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if data[j][1] < key[1]:
                data[j + 1] = data[j]
                j -= 1
            else:
                break

        data[j + 1] = key

    return comparisons


def run_closest_pair_benchmark():

    print("\nCLOSEST PAIR PERFORMANCE ANALYSIS")

    for n in [1000, 4000, 8000]:

        rng = random.Random(42)

        events = [
            (rng.random() * 10000, rng.random() * 10000)
            for _ in range(n)
        ]

        start = time.perf_counter()
        brute_pair, brute_distance, brute_count = (
            brute_force_closest(events)
        )
        brute_time = time.perf_counter() - start

        start = time.perf_counter()
        opt_pair, opt_distance, opt_count = (
            optimised_closest(events)
        )
        opt_time = time.perf_counter() - start

        print("\nNumber of Events:", n)
        print("Brute Force Distance Calculations:", brute_count)
        print("Optimised Distance Calculations:", opt_count)
        print("Brute Force Execution Time:", round(brute_time, 6), "seconds")
        print("Optimised Execution Time:", round(opt_time, 6), "seconds")

        assert math.isclose(brute_distance, opt_distance)
        assert brute_pair is not None
        assert opt_pair is not None


def run_sort_benchmark():

    print("\nINSERTION SORT COMPARISON ANALYSIS")

    rng = random.Random(42)

    random_alerts = [
        (f"A{i}", rng.randint(1, 100))
        for i in range(1000)
    ]

    nearly_sorted = sorted(
        random_alerts,
        key=lambda x: -x[1]
    )

    nearly_sorted[100], nearly_sorted[101] = (
        nearly_sorted[101], nearly_sorted[100]
    )

    random_comparisons = insertion_sort_count(random_alerts)
    nearly_comparisons = insertion_sort_count(nearly_sorted)

    print("Random Alerts Comparisons:", random_comparisons)
    print("Nearly Sorted Alerts Comparisons:", nearly_comparisons)


if __name__ == "__main__":

    print("CSA06 - CO2 PERFORMANCE ANALYSIS")
    print("Name: PINDIBOINA SAI DEEPAK")
    print("Register Number: 192411047")

    run_closest_pair_benchmark()
    run_sort_benchmark()

    print("\nPerformance Analysis Completed.")
