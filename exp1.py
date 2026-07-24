"""
Experiment 1: Interpolation Search vs Binary Search

This program:
1. Implements Interpolation Search.
2. Implements Binary Search.
3. Compares their execution time and number of comparisons.
4. Performs performance analysis on different input sizes.

Author: Suhail Akthar S M (IT-C, 210425205166)
"""

import random
import time


def interpolation_search(arr, target):
    """
    Perform Interpolation Search.

    Time Complexity:
        Average: O(log log n)
        Worst:   O(n)

    Space Complexity:
        O(1)

    Returns:
        tuple: (index, comparisons)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Avoid division by zero
        if arr[high] == arr[low]:
            break

        pos = low + (
            (target - arr[low]) * (high - low)
        ) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Perform Binary Search.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)

    Returns:
        tuple: (index, comparisons)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    """
    Compare Interpolation Search and Binary Search
    using different array sizes.
    """
    sizes = [1000, 5000, 10000, 50000, 100000]

    print("\nPerformance Analysis")
    print("-" * 78)
    print(
        f"{'Size':>10} "
        f"{'IS Time (ms)':>15} "
        f"{'BS Time (ms)':>15} "
        f"{'IS Comparisons':>18} "
        f"{'BS Comparisons':>18}"
    )
    print("-" * 78)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        # Interpolation Search timing
        start = time.perf_counter()
        for _ in range(100):
            _, is_comp = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search timing
        start = time.perf_counter()
        for _ in range(100):
            _, bs_comp = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(
            f"{size:>10}"
            f"{is_time:>15.4f}"
            f"{bs_time:>15.4f}"
            f"{is_comp:>18}"
            f"{bs_comp:>18}"
        )


def main():
    """Main function."""

    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    index, comparisons = interpolation_search(arr, target)

    print("Interpolation Search Demo")
    print("-" * 30)
    print(f"Array      : {arr}")
    print(f"Target     : {target}")
    print(f"Index      : {index}")
    print(f"Comparisons: {comparisons}")

    performance_analysis()


if __name__ == "__main__":
    main()