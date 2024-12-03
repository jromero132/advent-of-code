"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=4 ; task=2)
"""

import sys
from collections import deque


def main() -> None:
    ans, accumulate = 0, deque([1])
    for line in sorted(sys.stdin):
        _, card = line.split(":")
        winning_nums, nums = (set(part.strip().split()) for part in card.split("|"))
        n = len(nums.intersection(winning_nums))

        if len(accumulate) < n + 1:
            accumulate.extend([1] * (n + 1 - len(accumulate)))

        cnt = accumulate.popleft()
        ans += cnt
        for i in range(n):
            accumulate[i] += cnt

    print(ans)


if __name__ == "__main__":
    main()
