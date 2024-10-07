"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=3 ; task=2)
"""

import string
import sys


def main():
    ans = 0
    repeated_elements = set(string.ascii_letters)
    for i, rucksack in enumerate(sys.stdin, start=1):
        repeated_elements = repeated_elements.intersection(rucksack)

        if i % 3 == 0:
            char = list(repeated_elements)[0]  # get the only repeated character
            # get 1...26 if character is in a...z otherwise get 27...52 (since A...Z is in 65..90)
            ans += ord(char) - 96 if char >= "a" else ord(char) - 64 + 26
            repeated_elements = set(string.ascii_letters)
    print(ans)


if __name__ == "__main__":
    main()
