"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=5 ; task=2)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        pair_of_two_letters, letter_between = False, False
        pairs = set()
        for i in range(2, len(line)):
            letter_between |= line[i - 2] == line[i]

            if line[i - 2] == line[i - 1] == line[i]:
                pair_of_two_letters |= line[i - 1 : i + 1] in pairs
                pairs.add(line[i - 2 : i])

            else:
                pairs.add(line[i - 2 : i])
                pair_of_two_letters |= line[i - 1 : i + 1] in pairs

        ans += pair_of_two_letters and letter_between
    print(ans)


if __name__ == "__main__":
    main()
