"""
Experiment 2: String Pattern Matching Algorithms

This program implements and compares:
1. Naive String Matching
2. Knuth-Morris-Pratt (KMP) Algorithm
3. Rabin-Karp Algorithm

It also compares the number of character comparisons
performed by each algorithm on different pattern lengths.

Author: Suhail Akthar S M (IT-C, 210425205166)
"""

import random


def naive_search(text, pattern):
    """
    Perform Naive String Matching.

    Time Complexity:
        Worst: O(n * m)

    Returns:
        tuple: (matches, comparisons)
    """
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array
    used by the KMP algorithm.

    Time Complexity:
        O(m)
    """
    m = len(pattern)

    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt (KMP) String Matching.

    Time Complexity:
        O(n + m)

    Returns:
        tuple: (matches, comparisons)
    """
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        elif i < n:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, prime=101):
    """
    Perform Rabin-Karp String Matching.

    Time Complexity:
        Average: O(n + m)
        Worst:   O(n * m)

    Returns:
        tuple: (matches, comparisons)
    """
    n = len(text)
    m = len(pattern)

    d = 256

    h = pow(d, m - 1, prime)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    # Initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Sliding window
    for start in range(n - m + 1):

        if pattern_hash == text_hash:

            for j in range(m):
                comparisons += 1

                if text[start + j] != pattern[j]:
                    break
            else:
                matches.append(start)

        if start < n - m:
            text_hash = (
                d * (text_hash - ord(text[start]) * h)
                + ord(text[start + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return matches, comparisons


def performance_analysis():
    """
    Compare the algorithms on randomly generated text.
    """
    text = "".join(random.choices("ABCD", k=10000))
    patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

    print("\nPerformance Comparison")
    print("-" * 50)
    print(f"{'Pattern':>12} {'Naive':>10} {'KMP':>10} {'RK':>10}")
    print("-" * 50)

    for pattern in patterns:
        _, naive_comp = naive_search(text, pattern)
        _, kmp_comp = kmp_search(text, pattern)
        _, rk_comp = rabin_karp(text, pattern)

        print(
            f"{pattern:>12}"
            f"{naive_comp:>10}"
            f"{kmp_comp:>10}"
            f"{rk_comp:>10}"
        )


def main():
    """Main function."""

    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("String Pattern Matching Demo")
    print("-" * 35)
    print(f"Text    : {text}")
    print(f"Pattern : {pattern}")

    naive_matches, naive_comp = naive_search(text, pattern)
    kmp_matches, kmp_comp = kmp_search(text, pattern)
    rk_matches, rk_comp = rabin_karp(text, pattern)

    print("\nResults")
    print("-" * 35)
    print(f"Naive Search : Matches = {naive_matches}, Comparisons = {naive_comp}")
    print(f"KMP Search   : Matches = {kmp_matches}, Comparisons = {kmp_comp}")
    print(f"Rabin-Karp   : Matches = {rk_matches}, Comparisons = {rk_comp}")

    performance_analysis()


if __name__ == "__main__":
    main()