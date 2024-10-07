"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=3 ; task=1)
"""

import itertools
import sys


def main():
    max_x, max_y = 0, 0
    rectangles = []
    for line in sys.stdin:
        desc = line.split()
        x, y = (int(n) for n in desc[2].strip(":").split(","))
        len_x, len_y = (int(n) for n in desc[3].split("x"))
        rectangles.append(((x, y), (x + len_x, y + len_y)))
        max_x = max(max_x, x + len_x)
        max_y = max(max_y, y + len_y)

    grid = [[0] * max_y for _ in range(max_x)]
    ans = 0
    for rectangle in rectangles:
        for i, j in itertools.product(
            range(rectangle[0][0], rectangle[1][0]), range(rectangle[0][1], rectangle[1][1])
        ):
            grid[i][j] += 1
            ans += grid[i][j] == 2

    print(ans)


if __name__ == "__main__":
    main()
