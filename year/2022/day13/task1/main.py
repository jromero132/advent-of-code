"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=13 ; task=1)
"""

import sys


def compare(p1: list | int, p2: list | int) -> int:
    """
    Compare two elements, which can be either integers or lists, for ordering.

    This function recursively compares two inputs, returning an integer that indicates their relative order. It handles
    comparisons between integers and lists, allowing for nested structures, and determines whether the first input is
    less than, greater than, or equal to the second.

    Args:
        p1 (list | int): The first element to compare, which can be an integer or a list.
        p2 (list | int): The second element to compare, which can be an integer or a list.

    Returns:
        int: -1 if p1 is less than p2, 1 if p1 is greater than p2, and 0 if they are equal.

    """
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if isinstance(p1[i], int) and isinstance(p2[j], int):
            if p1[i] != p2[j]:
                return -1 if p1[i] < p2[j] else 1

        elif isinstance(p1[i], list) and isinstance(p2[j], list):
            if (result := compare(p1[i], p2[j])) != 0:
                return result

        else:
            l1 = p1[i] if isinstance(p1[i], list) else [p1[i]]
            l2 = p2[j] if isinstance(p2[j], list) else [p2[j]]
            if (result := compare(l1, l2)) != 0:
                return result

        i += 1
        j += 1

    return 0 if i == len(p1) and j == len(p2) else (-1 if i == len(p1) else 1)


def main() -> None:
    data = sys.stdin.read().strip().split("\n\n")
    packages = [[eval(x) for x in pair.split("\n")] for pair in data]
    print(sum(i for i, pair in enumerate(packages, 1) if compare(pair[0], pair[1]) == -1))


if __name__ == "__main__":
    main()
