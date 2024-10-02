"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=1 ; task=2)
"""

import sys


def main():
    ans = 0
    for module in (int(x) for x in sys.stdin):
        while module > 6:
            module = module // 3 - 2
            ans += module
    print(ans)


if __name__ == "__main__":
    main()
