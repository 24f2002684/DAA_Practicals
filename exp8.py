"""
Experiment 8: Travelling Salesman Problem (TSP)

Objective:
    Find the minimum-cost tour that visits every city exactly once
    and returns to the starting city.

Method Used:
    Brute Force (Permutation-Based Search)

Time Complexity:
    O(n!)

Space Complexity:
    O(n)

Note:
    A matrix reduction function (used in Branch and Bound) is included
    for reference but is not used in this implementation.
"""

from itertools import permutations

INF = float("inf")


def reduce_matrix(matrix: list[list[float]]):
    """
    Reduces the cost matrix using row and column reduction.

    This function is commonly used in the Branch and Bound
    approach for solving TSP. It is not used in this experiment.

    Args:
        matrix: Cost matrix.

    Returns:
        Reduced matrix and reduction cost.
    """

    reduced = [row[:] for row in matrix]
    n = len(reduced)
    reduction_cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(reduced[i])

        if row_min != INF and row_min > 0:
            reduction_cost += row_min

            for j in range(n):
                if reduced[i][j] != INF:
                    reduced[i][j] -= row_min

    # Column reduction
    for j in range(n):
        col_min = min(reduced[i][j] for i in range(n))

        if col_min != INF and col_min > 0:
            reduction_cost += col_min

            for i in range(n):
                if reduced[i][j] != INF:
                    reduced[i][j] -= col_min

    return reduced, reduction_cost


def tsp_brute_force(cost: list[list[float]], n: int):
    """
    Solves the Travelling Salesman Problem using Brute Force.

    Args:
        cost: Cost matrix.
        n: Number of cities.

    Returns:
        Optimal tour and its minimum cost.
    """

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        total_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


def print_cost_matrix(cost: list[list[float]], city_names: list[str]):
    """
    Displays the TSP cost matrix.
    """

    print("Cost Matrix\n")

    print(f'{"":>5}', end="")
    for city in city_names:
        print(f"{city:>6}", end="")
    print()

    for i, row in enumerate(cost):
        print(f"{city_names[i]:>5}", end="")

        for value in row:
            if value == INF:
                print(f"{'INF':>6}", end="")
            else:
                print(f"{int(value):>6}", end="")

        print()


def main():
    """
    Driver function.
    """

    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF],
    ]

    city_names = ["A", "B", "C", "D", "E"]
    n = len(cost)

    best_path, best_cost = tsp_brute_force(cost, n)

    print("Travelling Salesman Problem (TSP)")
    print("=" * 40)

    print_cost_matrix(cost, city_names)

    print("\nOptimal Tour")
    print("-" * 40)
    print(" -> ".join(city_names[i] for i in best_path))

    print(f"\nMinimum Cost : {best_cost}")

    print("\nPath Verification")
    print("-" * 40)

    for i in range(n):
        source = best_path[i]
        destination = best_path[i + 1]

        print(
            f"{city_names[source]} -> {city_names[destination]}"
            f" : {cost[source][destination]}"
        )


if __name__ == "__main__":
    main()