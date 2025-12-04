"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=4 ; task=1)
"""

import sys


def main() -> None:
    grid = sys.stdin.read().splitlines()

    n, m = len(grid), len(grid[0])
    ans = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                cnt = 0
                for di in range(-1, 2, 1):
                    for dj in range(-1, 2, 1):
                        cnt += (0 <= i + di < n) and (0 <= j + dj < m) and grid[i + di][j + dj] == "@"

                ans += cnt < 5  # It should be less than 5 because when di = dj = 0 then it counts itself :)
    print(ans)


if __name__ == "__main__":
    main()
