
def graph_coloring(graph, k, heuristic=False):
    vertices = list(graph)

    if heuristic:
        vertices.sort(
            key=lambda v: len(graph[v]),
            reverse=True
        )

    colors = {v: 0 for v in vertices}

    stats = {
        "search_nodes": 0,
        "candidate_assignments": 0,
        "rejected_branches": 0,
        "backtracks": 0,
        "max_depth": 0
    }

    def backtrack(index):
        stats["search_nodes"] += 1
        stats["max_depth"] = max(
            stats["max_depth"], index
        )

        if index == len(vertices):
            return True

        v = vertices[index]

        for c in range(1, k + 1):
            stats["candidate_assignments"] += 1

            if all(colors[u] != c for u in graph[v]):
                colors[v] = c

                if backtrack(index + 1):
                    return True

                colors[v] = 0
                stats["backtracks"] += 1

            else:
                stats["rejected_branches"] += 1

        return False

    result = backtrack(0)

    return result, colors if result else None, stats


graph1 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [],
    4: []
}

graph3 = {
    0: [],
    1: [],
    2: []
}

tests = [
    ("Colourable", graph1, 3),
    ("Not Colourable", graph2, 2),
    ("Boundary Case", graph3, 1)
]

for name, graph, k in tests:
    print("\n", name)

    result, coloring, stats = graph_coloring(
        graph, k
    )

    print("Result:", result)
    print("Coloring:", coloring)
    print("Statistics:", stats)


print("\nHEURISTIC COMPARISON")

for name, graph, k in tests:
    print("\n", name)

    for heuristic in [False, True]:
        result, coloring, stats = graph_coloring(
            graph, k, heuristic
        )

        print(
            "Degree heuristic:", heuristic,
            "Statistics:", stats
        )
