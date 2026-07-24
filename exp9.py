"""
Experiment 9: Bin Packing Problem (Greedy Algorithms)

Objective:
    Pack a set of items into the minimum number of bins using
    different greedy strategies.

Algorithms:
    1. First Fit (FF)
    2. First Fit Decreasing (FFD)
    3. Best Fit Decreasing (BFD)

Time Complexity:
    First Fit (FF):          O(n²)
    First Fit Decreasing:    O(n log n + n²)
    Best Fit Decreasing:     O(n log n + n²)

Space Complexity:
    O(n)
"""


def first_fit(items: list[float], capacity: float = 1.0):
    """
    First Fit Bin Packing Algorithm.

    Places each item into the first bin that has enough space.
    """

    remaining_space = []
    bin_contents = []

    for item in items:
        placed = False

        for i, space in enumerate(remaining_space):
            if space >= item:
                remaining_space[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            remaining_space.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items: list[float], capacity: float = 1.0):
    """
    First Fit Decreasing Algorithm.

    Sorts items in descending order before applying First Fit.
    """

    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items: list[float], capacity: float = 1.0):
    """
    Best Fit Decreasing Algorithm.

    Places each item into the bin that leaves the least remaining
    space after placement.
    """

    sorted_items = sorted(items, reverse=True)

    remaining_space = []
    bin_contents = []

    for item in sorted_items:

        best_index = -1
        minimum_remaining = float("inf")

        for i, space in enumerate(remaining_space):

            if space >= item and (space - item) < minimum_remaining:
                minimum_remaining = space - item
                best_index = i

        if best_index != -1:
            remaining_space[best_index] -= item
            bin_contents[best_index].append(item)
        else:
            remaining_space.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def display_bins(title: str, bins: list[list[float]]):
    """
    Displays the contents of each bin.
    """

    print(f"\n{title}")
    print("-" * 45)
    print(f"Total Bins Used: {len(bins)}\n")

    for index, current_bin in enumerate(bins, start=1):

        used = sum(current_bin)
        bar = "#" * int(used * 20)

        print(
            f"Bin {index:<2}: "
            f"{[round(item, 1) for item in current_bin]} "
            f"| Used: {used:.1f} "
            f"[{bar:<20}]"
        )


def main():
    """
    Driver function.
    """

    items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
    capacity = 1.0

    total_size = sum(items)

    # Lower bound on the minimum number of bins
    lower_bound = int(-(-total_size // capacity))

    print("Bin Packing Problem")
    print("=" * 45)

    print(f"Items            : {items}")
    print(f"Bin Capacity     : {capacity}")
    print(f"Total Item Size  : {total_size:.1f}")
    print(f"Lower Bound      : {lower_bound}")

    ff_bins = first_fit(items, capacity)
    ffd_bins = first_fit_decreasing(items, capacity)
    bfd_bins = best_fit_decreasing(items, capacity)

    display_bins("First Fit (FF)", ff_bins)
    display_bins("First Fit Decreasing (FFD)", ffd_bins)
    display_bins("Best Fit Decreasing (BFD)", bfd_bins)

    print("\nSummary")
    print("-" * 45)
    print(f"Lower Bound : {lower_bound}")
    print(f"First Fit   : {len(ff_bins)} bins")
    print(f"FFD         : {len(ffd_bins)} bins")
    print(f"BFD         : {len(bfd_bins)} bins")


if __name__ == "__main__":
    main()