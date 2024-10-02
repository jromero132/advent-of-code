"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=1 ; task=1)
"""

import sys


def main():
    data = [0]
    for line in sys.stdin:
        if line == "\n":
            data.append(0)

        else:
            data[-1] += int(line)

    print(max(data))


if __name__ == "__main__":
    main()
