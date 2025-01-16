"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=13 ; task=1)
"""

import sys


def is_vertical_reflection(grid: list[str], column: int) -> bool:
    c1, c2 = column - 1, column
    while c1 >= 0 and c2 < len(grid[0]):
        for i in range(len(grid)):
            if grid[i][c1] != grid[i][c2]:
                return False
        c1 -= 1
        c2 += 1
    return True


def is_horizontal_reflection(grid: list[str], row: int) -> bool:
    r1, r2 = row - 1, row
    while r1 >= 0 and r2 < len(grid):
        for j in range(len(grid[0])):
            if grid[r1][j] != grid[r2][j]:
                return False
        r1 -= 1
        r2 += 1
    return True


def main() -> None:
    patterns = sys.stdin.read().strip().split("\n\n")
    cols, rows = 0, 0
    for pattern in patterns:
        grid = pattern.split("\n")
        for c in range(1, len(grid[0])):
            if is_vertical_reflection(grid, c):
                cols += c
                break

        for r in range(1, len(grid)):
            if is_horizontal_reflection(grid, r):
                rows += r
                break

    print(100 * rows + cols)


if __name__ == "__main__":
    main()
