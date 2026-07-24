"""
Experiment 10: Deterministic vs Randomized Quick Sort

Objective:
    Compare the performance of Deterministic Quick Sort (DQS)
    and Randomized Quick Sort (RQS) on different input datasets.

Input Cases:
    1. Random
    2. Sorted
    3. Reverse Sorted
    4. Nearly Sorted

Metrics:
    - Number of Comparisons
    - Execution Time (milliseconds)

Time Complexity:
    Best/Average Case : O(n log n)
    Worst Case        : O(n²)

Space Complexity:
    O(log n) (Recursion Stack)
"""

import random
import sys
import time

# Increase recursion limit for large sorted inputs
sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partitions the array around the pivot.

    Returns:
        Index of the pivot after partitioning.
    """

    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr: list[int], low: int, high: int):
    """
    Quick Sort using the last element as pivot.
    """

    if low < high:
        pivot_index = partition(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)


def randomized_quicksort(arr: list[int], low: int, high: int):
    """
    Quick Sort using a randomly selected pivot.
    """

    if low < high:

        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


def run_test(sort_function, arr: list[int]):
    """
    Runs a sorting algorithm and measures its performance.

    Returns:
        Number of comparisons and execution time.
    """

    global comparisons

    data = arr[:]
    comparisons = 0

    start = time.perf_counter()

    sort_function(data, 0, len(data) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


def main():
    """
    Driver function.
    """

    N = 5000

    test_cases = {
        "Random": [random.randint(1, 100000) for _ in range(N)],
        "Sorted": list(range(N)),
        "Reverse": list(range(N, 0, -1)),
        "Nearly Sorted": list(range(N)),
    }

    # Slightly shuffle the nearly sorted array
    nearly_sorted = test_cases["Nearly Sorted"]

    for _ in range(N // 20):
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        nearly_sorted[i], nearly_sorted[j] = (
            nearly_sorted[j],
            nearly_sorted[i],
        )

    print("Comparison of Deterministic and Randomized Quick Sort")
    print("=" * 80)

    print(
        f"{'Input Type':<16}"
        f"{'DQS Comparisons':>18}"
        f"{'DQS Time(ms)':>16}"
        f"{'RQS Comparisons':>18}"
        f"{'RQS Time(ms)':>16}"
    )

    print("-" * 84)

    for case, arr in test_cases.items():

        d_comparisons, d_time = run_test(
            deterministic_quicksort,
            arr,
        )

        r_comparisons, r_time = run_test(
            randomized_quicksort,
            arr,
        )

        print(
            f"{case:<16}"
            f"{d_comparisons:>18}"
            f"{d_time:>16.2f}"
            f"{r_comparisons:>18}"
            f"{r_time:>16.2f}"
        )


if __name__ == "__main__":
    main()