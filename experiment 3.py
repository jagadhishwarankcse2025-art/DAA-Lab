import heapq


# ---------- Union-Find (Disjoint Set) ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


# ---------- Kruskal Algorithm ----------
def kruskal(n, edges):
    edges = sorted(edges)
    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_cost += w

            if len(mst) == n - 1:
                break

    return mst, total_cost


# ---------- Prim Algorithm ----------
def prim(n, adj):
    visited = [False] * n
    pq = [(0, 0, -1)]  # (weight, current, parent)

    mst = []
    total_cost = 0

    while pq:
        weight, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight

        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))

    return mst, total_cost


# ---------- Graph ----------
n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

adj = {i: [] for i in range(n)}

for w, u, v in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))


# ---------- Run Algorithms ----------
k_mst, k_cost = kruskal(n, edges)
p_mst, p_cost = prim(n, adj)


# ---------- Output ----------
print("=== Kruskal's MST ===")
for u, v, w in k_mst:
    print(f" Edge ({u} - {v}) Weight: {w}")
print(f" Total MST Cost: {k_cost}")

print("\n=== Prim's MST ===")
for u, v, w in p_mst:
    print(f" Edge ({u} - {v}) Weight: {w}")
print(f" Total MST Cost: {p_cost}")
