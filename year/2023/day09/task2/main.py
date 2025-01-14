"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=9 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        arrays = [[int(x) for x in line.strip().split()]]
        while any(x != 0 for x in arrays[-1]):
            arrays.append([b - a for a, b in zip(arrays[-1], arrays[-1][1:])])

        a = 0
        for i in range(len(arrays) - 1, -1, -1):
            a = arrays[i][0] - a

        ans += a
    print(ans)


if __name__ == "__main__":
    main()
