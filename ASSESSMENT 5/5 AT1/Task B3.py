
from itertools import combinations


def exact_set_cover(universe, centres):
    names = list(centres.keys())
    operations = 0

    for size in range(1, len(names) + 1):
        for combo in combinations(names, size):
            operations += 1
            covered = set()

            for centre in combo:
                covered.update(centres[centre])

            if set(universe).issubset(covered):
                return list(combo), operations

    return None, operations


def greedy_set_cover(universe, centres):
    uncovered = set(universe)
    selected = []
    operations = 0

    while uncovered:
        best = None
        best_coverage = set()

        for centre, zones in centres.items():
            operations += 1
            new_zones = zones & uncovered

            if len(new_zones) > len(best_coverage):
                best = centre
                best_coverage = new_zones

        if best is None:
            return None, operations

        selected.append(best)
        uncovered -= best_coverage

    return selected, operations


# Three normal instances

tests = [
    (
        {1, 2, 3, 4},
        {
            "A": {1, 2},
            "B": {3, 4},
            "C": {1, 2, 3},
            "D": {4}
        }
    ),
    (
        {1, 2, 3, 4, 5, 6},
        {
            "A": {1, 2, 3},
            "B": {4, 5, 6},
            "C": {1, 4, 5},
            "D": {2, 3, 6}
        }
    ),
    (
        {1, 2, 3, 4, 5},
        {
            "A": {1, 2, 3},
            "B": {3, 4},
            "C": {4, 5},
            "D": {1, 5}
        }
    )
]

for i, (universe, centres) in enumerate(tests, 1):
    exact, e_ops = exact_set_cover(universe, centres)
    greedy, g_ops = greedy_set_cover(universe, centres)

    print("\nINSTANCE", i)
    print("Exact:", exact)
    print("Greedy:", greedy)
    print("Exact size:", len(exact) if exact else None)
    print("Greedy size:", len(greedy) if greedy else None)
    print("Exact operations:", e_ops)
    print("Greedy operations:", g_ops)


# Counterexample

universe = {1, 2, 3, 4, 5, 6}

centres = {
    "A": {1, 2, 3, 4},
    "B": {1, 2, 5},
    "C": {3, 4, 6},
    "D": {5},
    "E": {6}
}

exact, e_ops = exact_set_cover(universe, centres)
greedy, g_ops = greedy_set_cover(universe, centres)

print("\nCOUNTEREXAMPLE")
print("Exact solution:", exact)
print("Greedy solution:", greedy)
print("Exact size:", len(exact))
print("Greedy size:", len(greedy))
print("Exact operations:", e_ops)
print("Greedy operations:", g_ops)


# Larger instance

large_universe = set(range(1, 21))

large_centres = {
    "C1": set(range(1, 6)),
    "C2": set(range(4, 9)),
    "C3": set(range(8, 13)),
    "C4": set(range(12, 17)),
    "C5": set(range(16, 21)),
    "C6": {1, 6, 11, 16},
    "C7": {2, 7, 12, 17},
    "C8": {3, 8, 13, 18}
}

exact, e_ops = exact_set_cover(
    large_universe, large_centres
)

greedy, g_ops = greedy_set_cover(
    large_universe, large_centres
)

print("\nLARGE INSTANCE")
print("Exact solution:", exact)
print("Greedy solution:", greedy)
print("Exact operations:", e_ops)
print("Greedy operations:", g_ops)
