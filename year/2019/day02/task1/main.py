"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=2 ; task=1)
"""

import sys


def main():
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    if len(memory) > 12:  # In order to run the actual puzzle input
        memory[1], memory[2] = 12, 2

    for i in range(0, len(memory), 4):
        match memory[i]:
            case 1:
                memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]

            case 2:
                memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]

            case 99:
                break

            case _:  # Error
                pass

    print(memory[0])


if __name__ == "__main__":
    main()
