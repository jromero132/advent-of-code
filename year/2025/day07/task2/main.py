"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=7 ; task=2)
"""

import sys


def main() -> None:
    grid = [f".{line}." for line in sys.stdin.read().splitlines()]
    n, m = len(grid), len(grid[0])

    dp = [1 if c == "S" else 0 for c in grid[0]]
    for i in range(1, n):
        new_row_dp = [0] * m
        for j in range(1, m):
            if grid[i][j] == "^":
                new_row_dp[j - 1] += dp[j]
                new_row_dp[j + 1] += dp[j]

            else:
                new_row_dp[j] += dp[j]

        dp = new_row_dp

    print(sum(dp))


if __name__ == "__main__":
    main()
