"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=2 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        dims = [int(n) for n in line.split("x")]
        ribbon, bow, m = 0, 1, 0
        for d in dims:
            m = max(m, d)
            ribbon += d
            bow *= d

        ans += 2 * (ribbon - m) + bow
    print(ans)


if __name__ == "__main__":
    main()
