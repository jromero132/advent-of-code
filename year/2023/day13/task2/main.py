"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=13 ; task=2)
"""

import sys


def is_vertical_reflection(grid: list[str], column: int) -> int:
    c1, c2 = column - 1, column
    cnt = 0
    while c1 >= 0 and c2 < len(grid[0]):
        for i in range(len(grid)):
            cnt += grid[i][c1] != grid[i][c2]
        c1 -= 1
        c2 += 1
    return cnt


def is_horizontal_reflection(grid: list[str], row: int) -> int:
    r1, r2 = row - 1, row
    cnt = 0
    while r1 >= 0 and r2 < len(grid):
        for j in range(len(grid[0])):
            cnt += grid[r1][j] != grid[r2][j]
        r1 -= 1
        r2 += 1
    return cnt


def main() -> None:
    patterns = sys.stdin.read().strip().split("\n\n")
    cols, rows = 0, 0
    for pattern in patterns:
        grid = pattern.split("\n")
        for c in range(1, len(grid[0])):
            if is_vertical_reflection(grid, c) == 1:
                cols += c
                break

        for r in range(1, len(grid)):
            if is_horizontal_reflection(grid, r) == 1:
                rows += r
                break

    print(100 * rows + cols)


if __name__ == "__main__":
    main()
