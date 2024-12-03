"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=1 ; task=2)
"""

import sys


def main() -> None:
    str_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    ans = 0
    for line in sys.stdin:
        first, last = None, None
        for i, c in enumerate(line):
            cur_char = c
            for k, v in str_to_digit.items():
                if line[i : i + len(k)] == k:
                    cur_char = v

            if cur_char.isdigit():
                first = cur_char if first is None else first
                last = cur_char

        ans += int(first + last)

    print(ans)


if __name__ == "__main__":
    main()
