"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=3 ; task=2)
"""

import sys
from collections import defaultdict


def main():
    grid = [line.strip() for line in sys.stdin]
    gear = defaultdict(list)
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                p = j + 1
                while p < len(grid[i]) and grid[i][p].isdigit():
                    p += 1

                num = int(grid[i][j:p])
                for dj in range(j - 1, p + 1):
                    if i > 0 and 0 <= dj < len(grid[i]) and grid[i - 1][dj] == "*":
                        gear[(i - 1, dj)].append(num)

                    if i + 1 < len(grid) and 0 <= dj < len(grid[i]) and grid[i + 1][dj] == "*":
                        gear[(i + 1, dj)].append(num)

                if j > 0 and grid[i][j - 1] == "*":
                    gear[(i, j - 1)].append(num)

                if p < len(grid[i]) and grid[i][p] == "*":
                    gear[(i, p)].append(num)

                j = p

            else:
                j += 1

    ans = 0
    for values in gear.values():
        if len(values) == 2:
            ans += values[0] * values[1]

    print(ans)


if __name__ == "__main__":
    main()
