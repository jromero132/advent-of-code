"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=10 ; task=2)
"""

import sys


def main() -> None:
    char_value = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    char_reverse = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    ans = []
    for line in sys.stdin:
        stack, valid = [], True
        for c in line.strip():
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            elif not stack or c != char_reverse[stack.pop()]:
                valid = False
                break

        if valid and stack:
            ans.append(0)
            for c in stack[::-1]:
                ans[-1] *= 5
                ans[-1] += char_value[char_reverse[c]]

    print(sorted(ans)[len(ans) // 2])


if __name__ == "__main__":
    main()
