"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=9 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        brackets, garbage, i = 0, False, 0
        while i < len(line.strip()):
            match line[i]:
                case "<":
                    garbage = True

                case ">":
                    garbage = False

                case "!":
                    i += 1

                case "{":
                    brackets += not garbage

                case "}":
                    if not garbage:
                        ans += brackets
                        brackets -= 1

            i += 1
    print(ans)


if __name__ == "__main__":
    main()
