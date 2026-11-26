# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 5: Kruskal, Prim and Boruvka MST


class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


def kruskal(vertices, edges):
    dsu = DSU(vertices)
    result = []
    total = 0

    print("\nKRUSKAL EDGE DECISIONS")

    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if dsu.union(u, v):
            result.append((u, v, w))
            total += w
            print("Accepted:", u, v, w)
        else:
            print("Rejected:", u, v, w)

        if len(result) == len(vertices) - 1:
            break

    print("Kruskal MST:", result)
    print("Total cost:", total)


def prim(vertices, edges, start):
    import heapq

    graph = {v: [] for v in vertices}

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = {start}
    heap = []

    for w, v in graph[start]:
        heapq.heappush(heap, (w, start, v))

    result = []
    total = 0

    print("\nPRIM EDGE DECISIONS")

    while heap and len(visited) < len(vertices):
        w, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        result.append((u, v, w))
        total += w

        print("Accepted:", u, v, w)

        for nw, nv in graph[v]:
            if nv not in visited:
                heapq.heappush(heap, (nw, v, nv))

    print("Prim MST:", result)
    print("Total cost:", total)


def boruvka(vertices, edges):
    dsu = DSU(vertices)
    components = len(vertices)

    result = []
    total = 0
    round_no = 1

    print("\nBORUVKA ROUNDS")

    while components > 1:
        cheapest = {}

        for u, v, w in edges:
            ru = dsu.find(u)
            rv = dsu.find(v)

            if ru != rv:
                if ru not in cheapest or w < cheapest[ru][2]:
                    cheapest[ru] = (u, v, w)

                if rv not in cheapest or w < cheapest[rv][2]:
                    cheapest[rv] = (u, v, w)

        print("\nRound", round_no)
        print("Candidate edges:", list(cheapest.values()))

        merged = False

        for edge in sorted(set(cheapest.values()),
                           key=lambda x: x[2]):
            u, v, w = edge

            if dsu.union(u, v):
                result.append(edge)
                total += w
                components -= 1
                merged = True

                print("Accepted:", edge)

        if not merged:
            break

        round_no += 1

    print("Boruvka MST:", result)
    print("Total cost:", total)


print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

vertices = ["A", "B", "C", "D", "E", "F"]

edges = [
    ("A", "B", 1),
    ("A", "C", 1),
    ("B", "C", 2),
    ("B", "D", 3),
    ("C", "D", 3),
    ("C", "E", 4),
    ("D", "E", 4),
    ("D", "F", 5),
    ("E", "F", 5),
    ("B", "E", 7),
    ("C", "F", 8)
]

print("\n========== KRUSKAL ==========")
kruskal(vertices, edges)

print("\n========== PRIM ==========")
prim(vertices, edges, "A")

print("\n========== BORUVKA ==========")
boruvka(vertices, edges)

print("\nMULTIPLE MST OBSERVATION")
print("Equal-weight edges create alternative MST choices.")
print("Different algorithms may select different edge sets.")
print("They are correct if they connect all vertices without")
print("cycles and have the same minimum total cost.")