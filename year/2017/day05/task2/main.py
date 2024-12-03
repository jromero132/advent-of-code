"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=5 ; task=2)
"""

import sys


def main() -> None:
    grid = [int(x) for x in sys.stdin]
    idx, steps = 0, 0
    while 0 <= idx < len(grid):
        tmp = grid[idx]

        if grid[idx] >= 3:
            grid[idx] -= 1

        else:
            grid[idx] += 1

        idx += tmp
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
