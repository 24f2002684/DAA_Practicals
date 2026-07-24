"""
Experiment 6: Matrix Chain Multiplication (Dynamic Programming)

Objective:
    Find the minimum number of scalar multiplications required
    to multiply a chain of matrices efficiently.

Time Complexity:
    O(n³)

Space Complexity:
    O(n²)
"""


def matrix_chain_order(dims: list[int]):
    """
    Computes the minimum multiplication cost for Matrix Chain Multiplication.

    Args:
        dims: List of matrix dimensions.
              Matrix Ai has dimensions dims[i-1] × dims[i].

    Returns:
        m: DP table storing minimum multiplication costs.
        s: Table storing optimal split positions.
    """

    n = len(dims) - 1

    # DP table for minimum multiplication cost
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # Table to store split positions
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1
            m[i][j] = float("inf")

            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i: int, j: int) -> str:
    """
    Recursively constructs the optimal parenthesization.
    """

    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} × {right})"


def print_dp_table(m, n: int):
    """
    Prints the Dynamic Programming cost table.
    """

    print("\nDP Cost Table (m[i][j])")

    print(f'{"":>6}', end="")
    for j in range(1, n + 1):
        print(f"A{j:>8}", end="")
    print()

    for i in range(1, n + 1):
        print(f"A{i:<5}", end="")

        for j in range(1, n + 1):

            if j < i:
                print(f'{"---":>9}', end="")
            else:
                print(f"{m[i][j]:>9}", end="")

        print()


def main():
    """
    Driver function.
    """

    # Matrix dimensions:
    # A1 = 10×30
    # A2 = 30×5
    # A3 = 5×60
    # A4 = 60×10

    dims = [10, 30, 5, 60, 10]
    n = len(dims) - 1

    print("Matrix Dimensions")

    for i in range(n):
        print(f"A{i + 1}: {dims[i]} × {dims[i + 1]}")

    m, s = matrix_chain_order(dims)

    print("\nResults")
    print("-" * 40)
    print(f"Minimum Scalar Multiplications : {m[1][n]}")
    print(f"Optimal Parenthesization       : {print_optimal_parens(s, 1, n)}")

    print_dp_table(m, n)


if __name__ == "__main__":
    main()