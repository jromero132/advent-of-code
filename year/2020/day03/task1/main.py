"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=3 ; task=1)
"""

import sys


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    slope = (1, 3)
    ans, i, j = 0, 0, 0
    while i < len(grid):
        ans += grid[i][j] == "#"
        j = (j + slope[1]) % len(grid[i])
        i += slope[0]

    print(ans)


if __name__ == "__main__":
    main()
