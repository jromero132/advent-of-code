"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    code = ""
    r, c = 1, 1
    for line in sys.stdin:
        for i in line:
            match i:
                case "U":
                    r = max(0, r - 1)

                case "R":
                    c = min(2, c + 1)

                case "D":
                    r = min(2, r + 1)

                case "L":
                    c = max(0, c - 1)

                case _:  # Error
                    pass

        code += str(r * 3 + c + 1)

    print(code)


if __name__ == "__main__":
    main()
