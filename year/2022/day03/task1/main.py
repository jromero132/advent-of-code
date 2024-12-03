"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=3 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for rucksack in sys.stdin:
        mid = len(rucksack) // 2
        repeated_elements = set(rucksack[:mid]).intersection(
            rucksack[mid:]
        )  # get repeated elements in both halves
        char = next(iter(repeated_elements))  # get the only repeated character

        # get 1...26 if character is in a...z otherwise get 27...52 (since A...Z is in 65...90)
        ans += ord(char) - 96 if char >= "a" else ord(char) - 64 + 26
    print(ans)


if __name__ == "__main__":
    main()
