"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=3 ; task=2)
"""

import sys


def main():
    grid = [line.strip() for line in sys.stdin.readlines()]
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ans = 1
    for si, sj in slopes:
        trees, i, j = 0, 0, 0
        while i < len(grid):
            trees += grid[i][j] == "#"
            j = (j + sj) % len(grid[i])
            i += si

        ans *= trees
    print(ans)


if __name__ == "__main__":
    main()
