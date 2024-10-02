"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=1 ; task=2)
"""


def main():
    line = input()
    step = len(line) // 2
    print(sum(int(line[i]) for i in range(len(line)) if line[i] == line[(i + step) % len(line)]))


if __name__ == "__main__":
    main()
