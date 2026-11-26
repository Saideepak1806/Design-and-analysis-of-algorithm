# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 2: Greedy vs Dynamic Programming

def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1],
                   reverse=True)

    total = 0
    selected = []
    operations = 0

    for name, weight, value in items:
        operations += 1

        if capacity == 0:
            break

        fraction = min(1, capacity / weight)
        taken_weight = weight * fraction
        taken_value = value * fraction

        selected.append((name, fraction, taken_weight, taken_value))

        capacity -= taken_weight
        total += taken_value

    print("\nFRACTIONAL GREEDY SELECTION")
    for item in selected:
        print(item)

    print("Maximum value:", round(total, 2))
    print("Items examined:", operations)


def greedy_zero_one(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1],
                   reverse=True)

    selected = []
    total_weight = 0
    total_value = 0

    for name, weight, value in items:
        if total_weight + weight <= capacity:
            selected.append((name, weight, value))
            total_weight += weight
            total_value += value

    print("\n0/1 GREEDY SELECTION")
    print("Selected items:", selected)
    print("Total weight:", total_weight)
    print("Total value:", total_value)


def zero_one_knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    operations = 0

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]

        for c in range(capacity + 1):
            operations += 1
            dp[i][c] = dp[i - 1][c]

            if weight <= c:
                dp[i][c] = max(
                    dp[i][c],
                    value + dp[i - 1][c - weight]
                )

    selected = []
    c = capacity

    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            name, weight, value = items[i - 1]
            selected.append((name, weight, value))
            c -= weight

    selected.reverse()

    print("\n0/1 DYNAMIC PROGRAMMING TABLE")
    for row in dp:
        print(row)

    print("Selected items:", selected)
    print("Maximum value:", dp[n][capacity])
    print("DP operations:", operations)


print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

items = [
    ("A", 10, 60),
    ("B", 20, 100),
    ("C", 30, 120)
]

capacity = 50

print("\n========== NORMAL CASE ==========")
fractional_knapsack(items, capacity)

print("\n========== GREEDY COUNTEREXAMPLE ==========")
greedy_zero_one(items, capacity)

print("\n========== EXACT 0/1 DP RESULT ==========")
zero_one_knapsack(items, capacity)