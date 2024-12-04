"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=3 ; task=1)
"""

import re
import sys


def main() -> None:
    print(
        sum(
            int(m.group("num1")) * int(m.group("num2"))
            for line in sys.stdin
            for m in re.finditer(r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)", line)
        ),
    )


if __name__ == "__main__":
    main()
