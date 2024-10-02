"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=1 ; task=1)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        first, last = None, None
        for c in line:
            if c.isdigit():
                first = c if first is None else first
                last = c

        ans += int(first + last)

    print(ans)


if __name__ == "__main__":
    main()
