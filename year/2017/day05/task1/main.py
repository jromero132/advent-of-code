"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=5 ; task=1)
"""

import sys


def main():
    grid = [int(x) for x in sys.stdin]
    idx, steps = 0, 0
    while 0 <= idx < len(grid):
        grid[idx] += 1
        idx += grid[idx] - 1
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
