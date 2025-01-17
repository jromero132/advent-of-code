"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=14 ; task=1)
"""

import sys


def main() -> None:
    grid = sys.stdin.read().strip().split("\n")
    ans, rocks = 0, [-1] * len(grid[0])
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                rocks[j] = i

            elif c == "O":
                ans += len(grid) - rocks[j] - 1
                rocks[j] += 1

    print(ans)


if __name__ == "__main__":
    main()
