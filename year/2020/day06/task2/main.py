"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=6 ; task=2)
"""

import sys


def main() -> None:
    groups = sys.stdin.read().split("\n\n")
    ans = 0
    for group in groups:
        questions = {chr(i) for i in range(ord("a"), ord("z") + 1)}  # universe: all questions
        for answer in (x for x in group.split("\n") if x != ""):
            questions.intersection_update(answer)
        ans += len(questions)
    print(ans)


if __name__ == "__main__":
    main()
