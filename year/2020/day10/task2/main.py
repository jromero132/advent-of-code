"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=10 ; task=1)
"""

import sys


def main() -> None:
    adapters = [0, *sorted(int(x) for x in sys.stdin.read().strip().split("\n"))]
    adapters.append(adapters[-1] + 3)
    dp = [0] * len(adapters)
    dp[0] = 1
    for i, a1 in enumerate(adapters):
        for j in range(i + 1, len(adapters)):
            a2 = adapters[j]
            if a1 + 3 < a2:
                break

            dp[j] += dp[i]
    print(dp[-1])


if __name__ == "__main__":
    main()
