"""
Experiment 5: Finding Minimum and Maximum Using Divide and Conquer

This program compares two approaches for finding the
minimum and maximum elements in an array:

1. Divide and Conquer Method
2. Naive Linear Scan Method

It also compares the number of element comparisons
performed by both approaches.

Author: Suhail Akthar S M (IT-C, 210425205166)
"""

import random


def min_max_divide_conquer(arr, low, high):
    """
    Find the minimum and maximum elements using
    the Divide and Conquer approach.

    Time Complexity:
        O(n)

    Space Complexity:
        O(log n) (recursive stack)

    Returns:
        tuple:
            (minimum, maximum, comparisons)
    """

    # Base case: one element
    if low == high:
        return arr[low], arr[low], 0

    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high], 1
        return arr[high], arr[low], 1

    # Divide
    mid = (low + high) // 2

    left_min, left_max, left_comp = min_max_divide_conquer(
        arr, low, mid
    )
    right_min, right_max, right_comp = min_max_divide_conquer(
        arr, mid + 1, high
    )

    # Combine
    comparisons = left_comp + right_comp + 2

    overall_min = (
        left_min
        if left_min < right_min
        else right_min
    )

    overall_max = (
        left_max
        if left_max > right_max
        else right_max
    )

    return overall_min, overall_max, comparisons


def min_max_naive(arr):
    """
    Find the minimum and maximum elements
    using a simple linear scan.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)

    Returns:
        tuple:
            (minimum, maximum, comparisons)
    """
    minimum = arr[0]
    maximum = arr[0]

    comparisons = 0

    for value in arr[1:]:

        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


def performance_analysis():
    """
    Compare Divide & Conquer and Naive methods
    for different input sizes.
    """
    print("\nPerformance Analysis")
    print("-" * 60)

    print(
        f"{'Size':>8}"
        f"{'D&C Comparisons':>18}"
        f"{'Naive Comparisons':>20}"
        f"{'3n/2 - 2':>14}"
    )

    print("-" * 60)

    for size in [10, 100, 1000, 10000]:

        arr = [
            random.randint(1, 10000)
            for _ in range(size)
        ]

        _, _, dc_comparisons = min_max_divide_conquer(
            arr,
            0,
            len(arr) - 1,
        )

        _, _, naive_comparisons = min_max_naive(arr)

        theoretical = (3 * size) // 2 - 2

        print(
            f"{size:>8}"
            f"{dc_comparisons:>18}"
            f"{naive_comparisons:>20}"
            f"{theoretical:>14}"
        )


def main():
    """Main function."""

    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    minimum, maximum, dc_comparisons = min_max_divide_conquer(
        arr,
        0,
        len(arr) - 1,
    )

    _, _, naive_comparisons = min_max_naive(arr)

    print("Divide and Conquer Demo")
    print("-" * 30)
    print(f"Array              : {arr}")
    print(f"Minimum Element    : {minimum}")
    print(f"Maximum Element    : {maximum}")
    print(f"D&C Comparisons    : {dc_comparisons}")
    print(f"Naive Comparisons  : {naive_comparisons}")

    performance_analysis()


if __name__ == "__main__":
    main()