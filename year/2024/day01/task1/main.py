"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=1 ; task=1)
"""

import sys


def main():
    group1, group2 = [], []
    for line in sys.stdin:
        line = [int(x) for x in line.split()]
        group1.append(line[0])
        group2.append(line[1])

    print(sum(abs(x - y) for x, y in zip(sorted(group1), sorted(group2))))


if __name__ == "__main__":
    main()
