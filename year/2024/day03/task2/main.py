"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=3 ; task=2)
"""

import re
import sys


def main() -> None:
    ans = 0
    enabled = True
    for line in sys.stdin:
        for m in re.finditer(r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)|do\(\)|don't\(\)", line):
            match m.group(0):
                case "do()":
                    enabled = True

                case "don't()":
                    enabled = False

                case _:
                    if enabled:
                        ans += int(m.group("num1")) * int(m.group("num2"))

    print(ans)


if __name__ == "__main__":
    main()
