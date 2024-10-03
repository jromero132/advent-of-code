"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=3 ; task=2)
"""

import sys


def main():
    triangles = []
    for i, line in enumerate(sys.stdin):
        if i % 3 == 0:
            triangles.extend(([], [], []))

        for j, side in enumerate(int(x) for x in line.split()):
            triangles[-3 + j].append(side)

    print(sum(sum(triangle) > 2 * max(triangle) for triangle in triangles))


if __name__ == "__main__":
    main()
