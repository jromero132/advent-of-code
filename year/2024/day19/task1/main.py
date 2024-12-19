"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=19 ; task=1)
"""

import sys


def main() -> None:
    patterns, designs = sys.stdin.read().split("\n\n")
    patterns = {*patterns.strip().split(", ")}
    designs = designs.strip().split("\n")

    ans = 0
    for design in designs:
        dp = [False] * (len(design) + 1)
        dp[len(design)] = True
        for i in range(len(design) - 1, -1, -1):
            for pattern in patterns:
                dp[i] |= pattern == design[i : i + len(pattern)] and dp[i + len(pattern)]

        ans += dp[0]
    print(ans)


if __name__ == "__main__":
    main()
