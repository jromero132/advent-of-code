"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=10 ; task=2)
"""

import sys


def main() -> None:
    cycles = {  # amount of cycles for each command.
        "noop": 1,
        "addx": 2,
    }

    n, m = 6, 40  # crt dimensions (rows and columns)
    crt = [""] * n
    i, j = 0, 0

    x = 1
    for cmd in (line.strip().split() for line in sys.stdin):
        for _ in range(cycles[cmd[0]]):
            crt[i] += "#" if x - 1 <= j <= x + 1 else " "
            j += 1
            if j == m:
                crt[i] = crt[i].strip()
                j = 0
                i += 1

        if cmd[0] == "addx":
            x += int(cmd[1])

    print("\n".join(crt))  # final answer: PLULKBZH


if __name__ == "__main__":
    main()
