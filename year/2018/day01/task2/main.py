"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=1 ; task=2)
"""

import sys


def main() -> None:
    data = [int(line.strip()) for line in sys.stdin]
    i, cur, seen = 0, 0, set()
    while cur not in seen:
        seen.add(cur)
        cur += data[i]
        i = 0 if i + 1 == len(data) else i + 1

    print(cur)


if __name__ == "__main__":
    main()
