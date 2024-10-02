"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=1 ; task=1)
"""


def main():
    line = input()
    print(sum(1 if c == "(" else -1 for c in line))


if __name__ == "__main__":
    main()
