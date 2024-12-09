"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=7 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin.read().splitlines():
        brackets, outside, inside = 0, False, False
        for i in range(len(line) - 3):
            if line[i] == "[":
                brackets += 1

            elif line[i] == "]":
                brackets -= 1

            elif line[i] != line[i + 1] and line[i : i + 2] == line[i + 3 : i + 1 : -1]:
                outside |= brackets == 0
                inside |= brackets > 0

        ans += outside and not inside
    print(ans)


if __name__ == "__main__":
    main()
