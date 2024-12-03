"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=1 ; task=1)
"""

import sys


def main() -> None:
    group1, group2 = [], []
    for line in sys.stdin:
        n1, n2 = (int(x) for x in line.split())
        group1.append(n1)
        group2.append(n2)

    print(sum(abs(x - y) for x, y in zip(sorted(group1), sorted(group2))))


if __name__ == "__main__":
    main()
