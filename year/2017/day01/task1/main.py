"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=1 ; task=1)
"""


def main() -> None:
    line = input()
    step = 1
    print(sum(int(line[i]) for i in range(len(line)) if line[i] == line[(i + step) % len(line)]))


if __name__ == "__main__":
    main()
