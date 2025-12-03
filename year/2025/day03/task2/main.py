"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=2)
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
    N_TURNS = 12
    ans = 0
    for line in sys.stdin:
        array = [int(x) for x in line.strip()]

        sol_array = [-1]
        for i in range(N_TURNS - 1, -1, -1):
            sol_array.append(get_index_of_max(array, sol_array[-1] + 1, len(array) - i))

        cur_ans = 0
        for i in range(1, len(sol_array)):
            cur_ans *= 10
            cur_ans += array[sol_array[i]]

        ans += cur_ans

    print(ans)


if __name__ == "__main__":
    main()
