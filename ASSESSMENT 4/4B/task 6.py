# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 6: Travelling Salesperson Problem using DP

from itertools import permutations
from time import perf_counter
import tracemalloc


def held_karp(cost, display=True):
    n = len(cost) - 1

    dp = {}
    parent = {}
    states = 0

    for mask in range(1, 1 << n):
        for j in range(1, n + 1):

            bit = 1 << (j - 1)

            if not (mask & bit):
                continue

            previous_mask = mask ^ bit

            if previous_mask == 0:
                dp[(mask, j)] = cost[0][j]
                parent[(mask, j)] = 0

            else:
                best = float("inf")
                best_previous = None

                for i in range(1, n + 1):
                    if previous_mask & (1 << (i - 1)):
                        candidate = (
                            dp[(previous_mask, i)] + cost[i][j]
                        )

                        if candidate < best:
                            best = candidate
                            best_previous = i

                dp[(mask, j)] = best
                parent[(mask, j)] = best_previous

            states += 1

    full_mask = (1 << n) - 1

    minimum = float("inf")
    last = None

    for j in range(1, n + 1):
        total = dp[(full_mask, j)] + cost[j][0]

        if total < minimum:
            minimum = total
            last = j

    route = []
    mask = full_mask
    current = last

    while current != 0:
        route.append(current)
        previous = parent[(mask, current)]
        mask ^= 1 << (current - 1)
        current = previous

    route.reverse()
    route = [0] + route + [0]

    if display:
        print("\nDP STATES EVALUATED:", states)
        print("Minimum travel cost:", minimum)
        print("Optimal route:", " -> ".join(map(str, route)))

    return minimum, route, states


def exhaustive_tsp(cost):
    n = len(cost) - 1

    best_cost = float("inf")
    best_route = None

    for order in permutations(range(1, n + 1)):
        route = (0,) + order + (0,)

        total = 0

        for i in range(len(route) - 1):
            total += cost[route[i]][route[i + 1]]

        if total < best_cost:
            best_cost = total
            best_route = route

    return best_cost, best_route


print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

cost_matrix = [
    [0, 10, 15, 20, 18, 12, 25],
    [10, 0, 35, 25, 17, 28, 20],
    [15, 35, 0, 30, 22, 16, 24],
    [20, 25, 30, 0, 19, 23, 14],
    [18, 17, 22, 19, 0, 27, 21],
    [12, 28, 16, 23, 27, 0, 26],
    [25, 20, 24, 14, 21, 26, 0]
]

print("\n========== SIX DELIVERY LOCATIONS ==========")
held_karp(cost_matrix)

print("\n========== FOUR LOCATION VALIDATION ==========")

small_matrix = [
    row[:5] for row in cost_matrix[:5]
]

dp_result = held_karp(small_matrix)

brute_cost, brute_route = exhaustive_tsp(small_matrix)

print("Exhaustive minimum cost:", brute_cost)
print("Exhaustive route:", brute_route)

if dp_result[0] == brute_cost:
    print("Validation successful: Both results match.")
else:
    print("Validation failed: Results do not match.")

print("\n========== STATE SPACE EXPERIMENT ==========")

for locations in range(4, 9):

    sample = [
        row[:locations + 1]
        for row in cost_matrix[:locations + 1]
    ]

    tracemalloc.start()
    start = perf_counter()

    result = held_karp(sample, False)

    elapsed = perf_counter() - start

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nDelivery locations:", locations)
    print("DP states:", result[2])
    print("Execution time:", round(elapsed, 6), "seconds")
    print("Peak memory:", peak_memory, "bytes")

print("\nBUSINESS REQUIREMENT CHANGE")
print("For 200 delivery locations, exact DP is impractical")
print("because the number of subsets grows exponentially.")
print("A heuristic such as Nearest Neighbour with 2-opt")
print("can be investigated for faster approximate routes.")