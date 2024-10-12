"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=6 ; task=1)
"""

import sys


def main():  # This can be done with a 2D Fenwick tree or segment tree, but not worth it tbh :)
    N = 1000
    grid = [[False] * N for _ in range(N)]
    funcs = [
        (
            "turn on",
            lambda _: 1,
        ),
        (
            "turn off",
            lambda _: 0,
        ),
        (
            "toggle",
            lambda x: 1 - x,
        ),
    ]
    for line in sys.stdin:
        line_parts = line.split()
        x1, y1 = (int(n) for n in line_parts[-3].split(","))
        x2, y2 = (int(n) for n in line_parts[-1].split(","))
        func = next(funcs[i][1] for i in range(len(funcs)) if line.startswith(funcs[i][0]))
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = func(grid[i][j])

    print(sum(x for row in grid for x in row))


if __name__ == "__main__":
    main()
