"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=3 ; task=1)
"""

import sys


def main():
    dirs = {
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
        "U": (0, 1),
    }

    x, y, s = 0, 0, 0
    grid = {(0, 0): 0}
    for move in sys.stdin.readline().split(","):
        dx, dy = dirs[move[0]]
        for _ in range(1, int(move[1:]) + 1):
            x += dx
            y += dy
            s += 1
            if (x, y) not in grid:
                grid[(x, y)] = s

    x, y = 0, 0
    ans = 10**9
    for move in sys.stdin.readline().split(","):
        dx, dy = dirs[move[0]]
        for _ in range(1, int(move[1:]) + 1):
            x += dx
            y += dy
            if (x, y) != (0, 0) and (x, y) in grid:
                ans = min(ans, abs(x) + abs(y))

    print(ans)


if __name__ == "__main__":
    main()
