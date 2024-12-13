"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=8 ; task=1)
"""

import sys


def main() -> None:
    operations = [line.strip().split() for line in sys.stdin]
    checked = [False] * len(operations)
    accumulator, i = 0, 0
    while i < len(operations) and not checked[i]:
        checked[i] = True
        op, arg = operations[i]
        match op:
            case "nop":
                i += 1

            case "acc":
                accumulator += int(arg)
                i += 1

            case "jmp":
                i += int(arg)

    print(accumulator)


if __name__ == "__main__":
    main()
