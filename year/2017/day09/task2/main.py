"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=9 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        garbage, i = False, 0
        while i < len(line.strip()):
            match line[i]:
                case "<":
                    ans += garbage
                    garbage = True

                case ">":
                    garbage = False

                case "!":
                    i += 1

                case _:
                    ans += garbage

            i += 1
    print(ans)


if __name__ == "__main__":
    main()
