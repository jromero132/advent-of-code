"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=1 ; task=1)
"""

import sys


def main():
    print(sum(int(line.strip()) for line in sys.stdin))


if __name__ == "__main__":
    main()
