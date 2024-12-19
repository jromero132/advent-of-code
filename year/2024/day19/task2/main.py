"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=19 ; task=2)
"""

import sys


def main() -> None:
    patterns, designs = sys.stdin.read().split("\n\n")
    patterns = {*patterns.strip().split(", ")}
    designs = designs.strip().split("\n")

    ans = 0
    for design in designs:
        dp = [0] * (len(design) + 1)
        dp[len(design)] = 1
        for i in range(len(design) - 1, -1, -1):
            for pattern in patterns:
                dp[i] += dp[i + len(pattern)] if pattern == design[i : i + len(pattern)] else 0

        ans += dp[0]
    print(ans)


if __name__ == "__main__":
    main()
