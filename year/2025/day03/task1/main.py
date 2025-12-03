"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=1)
"""

import sys


def get_index_of_max(array, start = 0, end = None) -> int:
    end = end or len(array)
    cur_max, idx = array[start], start
    for i in range(start + 1, end):
        if array[i] > cur_max:
            cur_max = array[i]
            idx = i

    return idx


def main() -> None:
    ans = 0
    for line in sys.stdin:
        array = [int(x) for x in line.strip()]
        p1 = get_index_of_max(array, 0, len(array) - 1)
        p2 = get_index_of_max(array, p1 + 1)
        ans += 10 * array[p1] + array[p2]

    print(ans)


if __name__ == "__main__":
    main()
