"""
Experiment 4: Dijkstra's Shortest Path Algorithm

This program implements Dijkstra's Algorithm using a
Min-Heap (Priority Queue) to find the shortest paths
from a given source vertex to all other vertices in a
weighted graph with non-negative edge weights.

Author: Your Name
"""

import heapq


def dijkstra(graph, source):
    """
    Compute the shortest path from the source vertex
    to all other vertices using Dijkstra's Algorithm.

    Time Complexity:
        O((V + E) log V)

    Space Complexity:
        O(V)

    Args:
        graph (dict): Adjacency list of the graph in the form
                      {vertex: [(neighbor, weight), ...]}
        source (int): Source vertex

    Returns:
        tuple:
            distances (list): Shortest distance from source
            previous (list): Parent of each vertex in the shortest path tree
    """
    num_vertices = len(graph)

    distances = [float("inf")] * num_vertices
    previous = [None] * num_vertices

    distances[source] = 0

    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor),
                )

    return distances, previous


def reconstruct_path(previous, source, target):
    """
    Reconstruct the shortest path from the source
    to the target vertex.

    Args:
        previous (list): Parent array
        source (int): Source vertex
        target (int): Destination vertex

    Returns:
        list: Shortest path from source to target
    """
    path = []

    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


def print_shortest_paths(source, distances, previous):
    """
    Display the shortest distance and path
    from the source to every vertex.
    """
    print(f"Shortest Paths from Vertex {source}")
    print("-" * 60)

    print(f"{'Vertex':>8} {'Distance':>10} {'Path':>30}")
    print("-" * 60)

    for vertex in range(len(distances)):
        path = reconstruct_path(previous, source, vertex)

        path_string = " -> ".join(map(str, path)) if path else "No Path"

        distance = (
            distances[vertex]
            if distances[vertex] != float("inf")
            else "INF"
        )

        print(f"{vertex:>8} {str(distance):>10} {path_string:>30}")


def main():
    """Main function."""

    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: [],
    }

    source = 0

    distances, previous = dijkstra(graph, source)

    print_shortest_paths(source, distances, previous)


if __name__ == "__main__":
    main()