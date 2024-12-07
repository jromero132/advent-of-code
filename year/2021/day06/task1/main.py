"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=6 ; task=1)
"""

import sys


def main() -> None:
    nums = sys.stdin.read().strip().split(",")
    state = [0] * 9
    for s in nums:
        state[int(s)] += 1

    for _ in range(80):
        state = state[1:] + [state[0]]
        state[6] += state[-1]

    print(sum(state))


if __name__ == "__main__":
    main()
