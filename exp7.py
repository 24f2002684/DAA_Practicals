"""
Experiment 7: N-Queens Problem (Backtracking)

Objective:
    Place N queens on an N×N chessboard such that no two queens
    attack each other.

Algorithm:
    - Use backtracking to place one queen per row.
    - Check if a position is safe before placing a queen.
    - Backtrack when no valid position exists.

Time Complexity:
    O(N!)

Space Complexity:
    O(N)
"""


from traitlets import All


def is_safe(board: list[int], row: int, col: int) -> bool:
    """
    Checks whether a queen can be safely placed at (row, col).

    Args:
        board: Current board configuration.
        row: Current row.
        col: Current column.

    Returns:
        True if the position is safe, otherwise False.
    """

    for prev_row in range(row):
        placed_col = board[prev_row]

        # Same column
        if placed_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


def solve_n_queens(n: int):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        n: Size of the chessboard.

    Returns:
        solutions: List of all valid board configurations.
        backtrack_count: Number of backtracking operations performed.
    """

    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row: int):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col

                backtrack(row + 1)

                # Undo placement (Backtrack)
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


def display_board(solution: list[int], n: int):
    """
    Displays a chessboard with queen placements.
    """

    print(" +" + "---+" * n)

    for row in range(n):
        print(" |", end="")

        for col in range(n):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(" +" + "---+" * n)


def main():
    """
    Driver function.
    """

    for n in [4, 6, 8]:
        solutions, backtracks = solve_n_queens(n)

        print(f"\nN = {n}")
        print("-" * 35)
        print(f"Total Solutions : {len(solutions)}")
        print(f"Backtracks      : {backtracks}")

        # Display all solutions only for N = 4
        if n == 4:
            print(f"\nAll Solutions for {n}-Queens\n")

            for index, solution in enumerate(solutions, start=1):
                print(f"Solution {index}: {solution}")
                display_board(solution, n)


if __name__ == "__main__":
    main()

# N = 4
# -----------------------------------
# Total Solutions : 2
# Backtracks      : 16

# All Solutions for 4-Queens
# Solution 1: [1, 3, 0, 2]

#  +---+---+---+---+
#  | . | Q | . | . |
#  +---+---+---+---+
#  | . | . | . | Q |
#  +---+---+---+---+
#  | Q | . | . | . |
#  +---+---+---+---+
#  | . | . | Q | . |
#  +---+---+---+---+

# Solution 2: [2, 0, 3, 1]
# ...