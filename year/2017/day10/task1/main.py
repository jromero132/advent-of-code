"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=10 ; task=1)
"""

import sys


def main() -> None:
    lengths = [int(x) for x in sys.stdin.read().strip().split(",")]
    cur_pos, skip = 0, 0
    array_len = 5 if len(lengths) < 5 else 256
    array = list(range(array_len))
    for skip, l in enumerate(lengths):
        new_array = array.copy()
        for i in range(l):
            new_array[(cur_pos + i) % array_len] = array[(cur_pos + l - 1 - i) % array_len]

        array = new_array
        cur_pos = (cur_pos + l + skip) % array_len

    print(array[0] * array[1])


if __name__ == "__main__":
    main()
