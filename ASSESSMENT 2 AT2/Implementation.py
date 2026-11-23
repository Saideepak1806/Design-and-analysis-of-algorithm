
"""
CSA06 - Design and Analysis of Algorithms
CO2 - Debugging and Optimisation Task

Student Name: PINDIBOINA SAI DEEPAK
Register Number: 192411047

Project: SentinelOps SOC Alert-Triage Module
"""

import math
import random
import time


def sort_alerts(alerts):
    """Sort alerts by descending severity using stable Timsort."""
    return sorted(alerts, key=lambda x: -x[1])


def prepare_blocklist(blocklist):
    """Convert the blocklist into a set for faster searching."""
    return set(blocklist)


def is_blocked(blocklist, ip):
    """Check whether an IP address exists in the blocklist."""
    return ip in blocklist


def find_signature(log, pattern):
    """Find all occurrences of a pattern using KMP."""

    n = len(log)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            i += 1

    hits = []
    i = 0
    j = 0

    while i < n:
        if log[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                hits.append(i - m)
                j = lps[j - 1]

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return hits


def closest_logins(events):
    """Find the closest login locations using pruning."""

    n = len(events)

    if n < 2:
        return None, math.inf

    points = sorted(
        [(x, y, index) for index, (x, y) in enumerate(events)],
        key=lambda p: (p[0], p[1], p[2])
    )

    best_sq = math.inf
    best_pair = None

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
            pair = tuple(sorted((index1, index2)))

            if d2 < best_sq or (
                d2 == best_sq and
                (best_pair is None or pair < best_pair)
            ):
                best_sq = d2
                best_pair = pair

    return best_pair, math.sqrt(best_sq)


def brute_force_closest(events):
    """Calculate the closest pair using brute force."""

    n = len(events)
    min_sq = math.inf
    pair = None
    count = 0

    for i in range(n):
        for j in range(n):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]

            d2 = dx * dx + dy * dy
            count += 1

            if i != j:
                current = tuple(sorted((i, j)))

                if d2 < min_sq or (
                    d2 == min_sq and
                    (pair is None or current < pair)
                ):
                    min_sq = d2
                    pair = current

    return pair, math.sqrt(min_sq), count


def optimised_closest_count(events):
    """Count full distance evaluations after pruning."""

    n = len(events)

    if n < 2:
        return 0

    points = sorted(
        events,
        key=lambda p: (p[0], p[1])
    )

    best_sq = math.inf
    count = 0

    for i in range(n):
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]

            dx = x2 - x1

            if dx * dx > best_sq:
                break

            dy = y2 - y1

            if dy * dy > best_sq:
                continue

            d2 = dx * dx + dy * dy
            count += 1

            if d2 < best_sq:
                best_sq = d2

    return count


def insertion_sort_count(alerts):
    """Count comparisons performed by insertion sort."""

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


def run_tests():
    """Test all functions and boundary conditions."""

    alerts = [
        ("A1", 3), ("A2", 9), ("A3", 5),
        ("A4", 9), ("A5", 1)
    ]

    expected = [
        ("A2", 9), ("A4", 9), ("A3", 5),
        ("A1", 3), ("A5", 1)
    ]

    assert sort_alerts(alerts) == expected
    assert sort_alerts([]) == []

    blocked_ips = prepare_blocklist([
        "10.0.0.5",
        "10.0.0.9",
        "172.16.4.2"
    ])

    assert is_blocked(blocked_ips, "10.0.0.9") is True
    assert is_blocked(blocked_ips, "8.8.8.8") is False
    assert is_blocked(prepare_blocklist([]), "8.8.8.8") is False

    assert find_signature("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert find_signature("ABC", "LONG") == []
    assert find_signature("ABC", "C") == [2]
    assert find_signature("ABABA", "ABA") == [0, 2]
    assert find_signature("ABC", "") == [0, 1, 2, 3]
    assert find_signature("", "A") == []

    events = [
        (2, 3), (12, 30), (40, 50),
        (5, 1), (12, 10), (3, 4)
    ]

    pair, distance = closest_logins(events)

    assert pair == (0, 5)
    assert math.isclose(distance, math.sqrt(2))

    assert closest_logins([]) == (None, math.inf)
    assert closest_logins([(2, 3)]) == (None, math.inf)

    assert closest_logins([(0, 0), (0, 0)])[0] == (0, 1)

    print("All functional and boundary tests passed.")


def run_benchmarks():
    """Measure closest-pair and insertion-sort performance."""

    print("\nCLOSEST PAIR PERFORMANCE")

    for n in [1000, 4000, 8000]:

        rng = random.Random(42)

        events = [
            (rng.random() * 10000, rng.random() * 10000)
            for _ in range(n)
        ]

        start = time.perf_counter()
        _, brute_distance, brute_count = brute_force_closest(events)
        brute_time = time.perf_counter() - start

        start = time.perf_counter()
        _, opt_distance = closest_logins(events)
        opt_time = time.perf_counter() - start

        opt_count = optimised_closest_count(events)

        assert math.isclose(brute_distance, opt_distance)

        print("\nEvents:", n)
        print("Brute-force evaluations:", brute_count)
        print("Optimised evaluations:", opt_count)
        print("Brute-force time:", round(brute_time, 6), "seconds")
        print("Optimised time:", round(opt_time, 6), "seconds")

    print("\nINSERTION SORT COMPARISON")

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

    random_count = insertion_sort_count(random_alerts)
    nearly_count = insertion_sort_count(nearly_sorted)

    print("Random alert comparisons:", random_count)
    print("Nearly sorted comparisons:", nearly_count)


if __name__ == "__main__":

    print("SENTINELOPS - ALERT TRIAGE SYSTEM")
    print("Student Name: PINDIBOINA SAI DEEPAK")
    print("Register Number: 192411047")

    run_tests()
    run_benchmarks()

    print("\nProgram execution completed successfully.")
