"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=8 ; task=1)
"""

import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    n, m = len(lines) - 1, len(lines[0]) - 1
    visible = [  # [i][j] is True if the tree is visible, otherwise it is False
        [i in (0, n) or j in (0, m) for j in range(len(lines[0]))] for i in range(len(lines))
    ]

    for i in range(1, n):  # run for rows
        greater = lines[i][0]
        for j in range(1, m):  # run from left to right
            if lines[i][j] > greater:
                visible[i][j] = True
            greater = max(greater, lines[i][j])

        greater = lines[i][-1]
        for j in range(m - 1, 0, -1):  # run from right to left
            if lines[i][j] > greater:
                visible[i][j] = True
            greater = max(greater, lines[i][j])

    for j in range(1, m):  # run for columns
        greater = lines[0][j]
        for i in range(1, n):  # run from top to bottom
            if lines[i][j] > greater:
                visible[i][j] = True
            greater = max(greater, lines[i][j])

        greater = lines[-1][j]
        for i in range(n - 1, 0, -1):  # run from bottom to top
            if lines[i][j] > greater:
                visible[i][j] = True
            greater = max(greater, lines[i][j])

    print(sum(x for row in visible for x in row))


if __name__ == "__main__":
    main()
