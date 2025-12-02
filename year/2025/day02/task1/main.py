"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=2 ; task=1)
"""

import sys
from itertools import accumulate
from bisect import bisect_left

def main() -> None:
    invalid_ids = [int(str(i) * 2) for i in range(1, 10**6)]
    pref_sum = [0, *accumulate(invalid_ids)]

    pairs = sys.stdin.read().strip().split(",")
    ans = 0
    for pair in pairs:
        l, r = map(int, pair.split("-"))
        pos_l = bisect_left(invalid_ids, l)
        pos_r = bisect_left(invalid_ids, r + 1)
        ans += pref_sum[pos_r] - pref_sum[pos_l]
    print(ans)


if __name__ == "__main__":
    main()
