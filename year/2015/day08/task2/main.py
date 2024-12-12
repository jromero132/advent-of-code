"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=8 ; task=2)
"""

import sys


def main() -> None:
    chars_of_code, chars_in_memory = 0, 0
    for line in (line.strip() for line in sys.stdin):
        chars_of_code += len(line)
        chars_in_memory += 2  # the surrounding double quotes
        for c in line:
            chars_in_memory += 1
            if c in ("\\", '"'):
                chars_in_memory += 1

    print(chars_in_memory - chars_of_code)


if __name__ == "__main__":
    main()
