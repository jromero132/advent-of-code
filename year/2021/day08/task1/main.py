"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=8 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for info in sys.stdin:
        _, output = info.strip().split(" | ")
        for signal in output.split():
            if len(signal) in (2, 3, 4, 7):  # check if the signal is a 1, 7, 4 or 8 respectively
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
