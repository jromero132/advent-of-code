"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=10 ; task=1)
"""

import sys


def main() -> None:
    char_value = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    char_reverse = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    ans = 0
    for line in sys.stdin:
        stack = []
        for c in line.strip():
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            elif not stack or c != char_reverse[stack.pop()]:
                ans += char_value[c]
                break

    print(ans)


if __name__ == "__main__":
    main()
