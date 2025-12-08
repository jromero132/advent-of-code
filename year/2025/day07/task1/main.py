"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=7 ; task=1)
"""

import sys


def main() -> None:
    grid = [f".{line}." for line in sys.stdin.read().splitlines()]
    n, m = len(grid), len(grid[0])

    ans = 0
    dp = [c == "S" for c in grid[0]]
    for i in range(1, n):
        new_row_dp = [False] * m
        for j in range(1, m):
            if grid[i][j] == "^" and dp[j]:
                new_row_dp[j - 1] = True
                new_row_dp[j + 1] = True
                ans += 1

            else:
                new_row_dp[j] |= dp[j]

        dp = new_row_dp

    print(ans)


if __name__ == "__main__":
    main()
