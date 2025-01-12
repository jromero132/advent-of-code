"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=10 ; task=2)
"""

import sys
from functools import reduce
from operator import xor


def main() -> None:
    lengths = [ord(x) for x in sys.stdin.read().strip()] + [17, 31, 73, 47, 23]
    cur_pos = 0
    array_len = 5 if len(lengths) < 5 else 256
    array = list(range(array_len))
    for k in range(64):
        for skip, l in enumerate(lengths, start=k * len(lengths)):
            new_array = array.copy()
            for i in range(l):
                new_array[(cur_pos + i) % array_len] = array[(cur_pos + l - 1 - i) % array_len]

            array = new_array
            cur_pos = (cur_pos + l + skip) % array_len

    print("".join(hex(reduce(xor, array[i : i + 16]))[2:].zfill(2) for i in range(0, 256, 16)))


if __name__ == "__main__":
    main()
