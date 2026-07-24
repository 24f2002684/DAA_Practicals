"""
Experiment 3: Minimum Spanning Tree (MST)

This program implements two algorithms to find the
Minimum Spanning Tree (MST) of a weighted undirected graph:

1. Kruskal's Algorithm (using Union-Find)
2. Prim's Algorithm (using Min Heap)

Author: Suhail Akthar S M (IT-C, 210425205166)
"""

import heapq


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure
    with Path Compression and Union by Rank.

    Operations:
        - find(x)
        - union(x, y)
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        """
        Find the representative (root) of a set
        using path compression.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v):
        """
        Merge two sets using Union by Rank.

        Returns:
            bool: True if union was successful,
                  False if both vertices are already
                  in the same set.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u

        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1

        return True


def kruskal(num_vertices, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree.

    Time Complexity:
        O(E log E)

    Returns:
        tuple: (mst_edges, total_cost)
    """
    edges = sorted(edges)

    uf = UnionFind(num_vertices)

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == num_vertices - 1:
                break

    return mst, total_cost


def prim(num_vertices, adjacency_list, start=0):
    """
    Prim's Algorithm for Minimum Spanning Tree.

    Time Complexity:
        O(E log V)

    Returns:
        tuple: (mst_edges, total_cost)
    """
    key = [float("inf")] * num_vertices
    parent = [-1] * num_vertices
    in_mst = [False] * num_vertices

    key[start] = 0

    priority_queue = [(0, start)]

    mst = []
    total_cost = 0

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)

        if in_mst[u]:
            continue

        in_mst[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, edge_weight in adjacency_list.get(u, []):

            if not in_mst[v] and edge_weight < key[v]:
                key[v] = edge_weight
                parent[v] = u

                heapq.heappush(priority_queue, (edge_weight, v))

    return mst, total_cost


def build_adjacency_list(edges):
    """
    Build an adjacency list from the edge list.

    Returns:
        dict
    """
    adjacency_list = {}

    for weight, u, v in edges:
        adjacency_list.setdefault(u, []).append((v, weight))
        adjacency_list.setdefault(v, []).append((u, weight))

    return adjacency_list


def print_mst(title, mst, total_cost):
    """
    Display MST edges and total cost.
    """
    print(title)
    print("-" * len(title))

    for u, v, weight in mst:
        print(f"Edge ({u} - {v})  Weight = {weight}")

    print(f"\nTotal MST Cost = {total_cost}\n")


def main():
    """Main function."""

    num_vertices = 7

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
        (11, 5, 6),
    ]

    adjacency_list = build_adjacency_list(edges)

    kruskal_mst, kruskal_cost = kruskal(num_vertices, edges)
    prim_mst, prim_cost = prim(num_vertices, adjacency_list)

    print_mst("Kruskal's Minimum Spanning Tree", kruskal_mst, kruskal_cost)
    print_mst("Prim's Minimum Spanning Tree", prim_mst, prim_cost)


if __name__ == "__main__":
    main()