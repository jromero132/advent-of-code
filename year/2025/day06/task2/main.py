"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=6 ; task=2)
"""

import sys
from math import prod


def main() -> None:
    array = [line + " " for line in sys.stdin.read().splitlines()]
    ans = 0
    op, nums = None, []
    for i in range(len(array[0])):
        if all(txt[i] == " " for txt in array):
            ans += sum(nums) if op == "+" else prod(nums)
            op, nums = None, []
            continue

        if op is None and array[-1][i] != " ":
            op = array[-1][i]

        nums.append(int("".join(txt[i] for txt in array[:-1])))

    print(ans)


if __name__ == "__main__":
    main()
