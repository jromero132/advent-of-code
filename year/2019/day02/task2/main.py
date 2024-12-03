"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=2 ; task=2)
"""

import itertools
import sys


def get_output(memory: list[int]) -> int:
    """
    Process a list of integers as a simple instruction set.

    This function interprets a list of integers as a series of instructions, performing addition or
    multiplication based on the opcode at each step. It modifies the list in place and returns the
    value at the first position after processing all instructions.

    Args:
        memory (list[int]): A list of integers representing the instruction set.

    Returns:
        int: The value at the first position of the modified list after executing the instructions.

    """
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

    return memory[0]


def main() -> None:
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    for noun, verb in itertools.product(range(100), range(100)):
        mem = memory[:]
        mem[1], mem[2] = noun, verb
        if get_output(mem) == 19690720:  # Expected output
            print(100 * noun + verb)
            return


if __name__ == "__main__":
    main()
