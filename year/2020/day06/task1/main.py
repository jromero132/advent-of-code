"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=6 ; task=1)
"""

import sys


def main() -> None:
    groups = sys.stdin.read().split("\n\n")
    ans = 0
    for group in groups:
        questions = set()
        for answer in group.split("\n"):
            questions.update(answer)
        ans += len(questions)
    print(ans)


if __name__ == "__main__":
    main()
