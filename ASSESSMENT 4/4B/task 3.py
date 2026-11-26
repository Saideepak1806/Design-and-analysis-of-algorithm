# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 3: Graph Routing Algorithms

import heapq

vertices = ["A", "B", "C", "D", "E", "F", "G", "H"]

edges = [
    ("A", "B", 4),
    ("A", "C", 7),
    ("B", "C", 2),
    ("B", "D", 1),
    ("C", "D", 1),
    ("D", "E", 3),
    ("C", "E", 8),
    ("E", "F", 2),
    ("F", "G", 3),
    ("G", "H", 1),
    ("D", "G", 10),
    ("B", "F", 12)
]

INF = float("inf")


def dijkstra(source, graph_edges):
    graph = {v: [] for v in vertices}

    for u, v, w in graph_edges:
        if w < 0:
            print("Dijkstra cannot handle negative edges.")
            return
        graph[u].append((v, w))

    dist = {v: INF for v in vertices}
    parent = {v: None for v in vertices}

    dist[source] = 0
    heap = [(0, source)]
    visited = set()
    order = []

    while heap:
        d, u = heapq.heappop(heap)

        if u in visited:
            continue

        visited.add(u)
        order.append(u)

        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    print("\nDIJKSTRA DISTANCES")
    print(dist)
    print("Predecessors:", parent)
    print("Finalisation order:", order)

    for target in vertices:
        if dist[target] != INF:
            path = []
            current = target

            while current is not None:
                path.append(current)
                current = parent[current]

            print(source, "to", target, ":", path[::-1])


def bellman_ford(source, graph_edges):
    dist = {v: INF for v in vertices}
    parent = {v: None for v in vertices}

    dist[source] = 0

    for _ in range(len(vertices) - 1):
        changed = False

        for u, v, w in graph_edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                changed = True

        if not changed:
            break

    for u, v, w in graph_edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            print("Reachable negative-weight cycle detected.")
            return

    print("\nBELLMAN-FORD DISTANCES")
    print(dist)
    print("Predecessors:", parent)


def floyd_warshall(graph_edges):
    d = {
        u: {v: (0 if u == v else INF) for v in vertices}
        for u in vertices
    }

    for u, v, w in graph_edges:
        d[u][v] = min(d[u][v], w)

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if d[i][k] != INF and d[k][j] != INF:
                    d[i][j] = min(
                        d[i][j],
                        d[i][k] + d[k][j]
                    )

    print("\nFLOYD-WARSHALL DISTANCE MATRIX")
    print("   ", vertices)

    for i in vertices:
        print(i, [d[i][j] for j in vertices])


def warshall(graph_edges):
    reach = {
        i: {j: i == j for j in vertices}
        for i in vertices
    }

    for u, v, w in graph_edges:
        reach[u][v] = True

    for k in vertices:
        for i in vertices:
            for j in vertices:
                reach[i][j] = (
                    reach[i][j] or
                    (reach[i][k] and reach[k][j])
                )

    print("\nWARSHALL REACHABILITY MATRIX")
    print("   ", vertices)

    for i in vertices:
        print(i, [int(reach[i][j]) for j in vertices])


print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

print("\n========== STAGE A: DIJKSTRA ==========")
dijkstra("A", edges)

negative_edges = [
    (u, v, -4 if (u, v) == ("C", "D") else w)
    for u, v, w in edges
]

print("\n========== STAGE B: NEGATIVE EDGE ==========")
print("Prediction: The negative edge C to D may improve")
print("the distance to D after D has already been finalised.")
bellman_ford("A", negative_edges)

print("\n========== STAGE C: NEGATIVE CYCLE ==========")
cycle_edges = negative_edges + [("E", "B", -20)]
bellman_ford("A", cycle_edges)

print("\n========== STAGE D: FLOYD-WARSHALL ==========")
floyd_warshall(negative_edges)

print("\n========== WARSHALL ==========")
warshall(negative_edges)