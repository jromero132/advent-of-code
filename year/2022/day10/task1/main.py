"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=10 ; task=1)
"""

import sys


def main() -> None:
    cycles = {  # amount of cycles for each command
        "noop": 1,
        "addx": 2,
    }

    ans = 0
    cycle = 0
    x = 1
    for cmd in (line.strip().split() for line in sys.stdin):
        for _ in range(cycles[cmd[0]]):
            cycle += 1
            if cycle <= 220 and cycle % 40 == 20:
                ans += cycle * x

        if cmd[0] == "addx":
            x += int(cmd[1])

    print(ans)


if __name__ == "__main__":
    main()
