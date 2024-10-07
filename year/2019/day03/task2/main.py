"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=3 ; task=2)
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
    grid1 = {(0, 0): 0}
    for move in sys.stdin.readline().split(","):
        dx, dy = dirs[move[0]]
        for _ in range(1, int(move[1:]) + 1):
            x += dx
            y += dy
            s += 1
            if (x, y) not in grid1:
                grid1[(x, y)] = s

    ans = 10**9
    x, y, s = 0, 0, 0
    grid2 = {(0, 0): 0}
    for move in sys.stdin.readline().split(","):
        dx, dy = dirs[move[0]]
        for _ in range(1, int(move[1:]) + 1):
            x += dx
            y += dy
            s += 1
            if (x, y) not in grid2:
                grid2[(x, y)] = s

            if (x, y) in grid1:
                ans = min(ans, grid1[(x, y)] + grid2[(x, y)])

    print(ans)


if __name__ == "__main__":
    main()
