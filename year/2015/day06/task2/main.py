"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=6 ; task=2)
"""

import sys


def main() -> (
    None
):  # This can be done with a 2D Fenwick tree or segment tree, but not worth it tbh :)
    n = 1000
    grid = [[0] * n for _ in range(n)]
    function = [
        (
            "turn on",
            lambda x: x + 1,
        ),
        (
            "turn off",
            lambda x: max(0, x - 1),
        ),
        (
            "toggle",
            lambda x: x + 2,
        ),
    ]
    for line in sys.stdin:
        line_parts = line.split()
        x1, y1 = (int(n) for n in line_parts[-3].split(","))
        x2, y2 = (int(n) for n in line_parts[-1].split(","))
        func = next(function[i][1] for i in range(len(function)) if line.startswith(function[i][0]))
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = func(grid[i][j])

    print(sum(x for row in grid for x in row))


if __name__ == "__main__":
    main()
