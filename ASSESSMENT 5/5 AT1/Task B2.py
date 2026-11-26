
graph_A = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4]
}

graph_B = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [],
    4: [],
    5: []
}


def graph_coloring(graph, number_of_colours):
    """Return (success, colouring, statistics) for a graph colouring search."""
    colouring = {}
    statistics = {"assignments": 0, "backtracks": 0}

    def search():
        if len(colouring) == len(graph):
            return True

        uncoloured = [node for node in graph if node not in colouring]
        node = max(
            uncoloured,
            key=lambda candidate: (
                sum(colouring.get(neighbour) is not None for neighbour in graph[candidate]),
                len(graph[candidate])
            )
        )

        unavailable = {colouring[neighbour]
                       for neighbour in graph[node]
                       if neighbour in colouring}

        for colour in range(number_of_colours):
            if colour in unavailable:
                continue

            colouring[node] = colour
            statistics["assignments"] += 1

            if search():
                return True

            del colouring[node]
            statistics["backtracks"] += 1

        return False

    success = search() if number_of_colours > 0 else False
    if not success:
        colouring = {node: None for node in graph}

    return success, colouring, statistics


print("GRAPH A - EASY")

result_A = graph_coloring(graph_A, 2)

print("Result:", result_A[0])
print("Colouring:", result_A[1])
print("Statistics:", result_A[2])

print("\nGRAPH B - DIFFICULT")

result_B = graph_coloring(graph_B, 2)

print("Result:", result_B[0])
print("Colouring:", result_B[1])
print("Statistics:", result_B[2])
