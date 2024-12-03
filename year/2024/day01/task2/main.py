"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    group1, group2 = [], []
    for line in sys.stdin:
        n1, n2 = (int(x) for x in line.split())
        group1.append(n1)
        group2.append(n2)

    print(sum(x * group2.count(x) for x in group1))


if __name__ == "__main__":
    main()
