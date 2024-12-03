"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=1 ; task=2)
"""


def main() -> None:
    line = input()
    floor = 0
    for i, c in enumerate(line, start=1):
        floor += 1 if c == "(" else -1
        if floor == -1:
            print(i)
            break


if __name__ == "__main__":
    main()
