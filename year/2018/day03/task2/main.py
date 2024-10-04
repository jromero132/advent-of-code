"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=3 ; task=2)
"""

import sys


def no_overlaps(grid, rectangle):
    for i in range(rectangle[0][0], rectangle[1][0]):
        for j in range(rectangle[0][1], rectangle[1][1]):
            if grid[i][j] != 1:
                return False
    return True


def main():
    max_x, max_y = 0, 0
    rectangles = []
    for line in sys.stdin:
        desc = line.split()
        rid = desc[0][1:]
        x, y = (int(n) for n in desc[2].strip(":").split(","))
        len_x, len_y = (int(n) for n in desc[3].split("x"))
        rectangles.append(((x, y), (x + len_x, y + len_y), rid))
        max_x = max(max_x, x + len_x)
        max_y = max(max_y, y + len_y)

    grid = [[0] * max_y for _ in range(max_x)]
    for rectangle in rectangles:
        for i in range(rectangle[0][0], rectangle[1][0]):
            for j in range(rectangle[0][1], rectangle[1][1]):
                grid[i][j] += 1

    for rectangle in rectangles:
        if no_overlaps(grid, rectangle):
            print(rectangle[2])
            break


if __name__ == "__main__":
    main()
