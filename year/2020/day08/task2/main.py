"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=8 ; task=2)
"""

import sys


def run_successfully(operations: list[tuple[str, str]]) -> tuple[int, bool]:
    """
    Simulate running a sequence of operations, tracking the accumulator and detecting infinite loops.

    It attempts to run through all operations, stopping if an instruction is revisited.

    Args:
        operations (list[tuple[str, str]]): A list of tuples containing operation type and argument.

    Returns:
        tuple[int, bool]: A tuple containing the final accumulator value and a boolean indicating whether all operations
            were executed.

    """
    checked = [False] * len(operations)
    accumulator, i = 0, 0
    while i < len(operations) and not checked[i]:
        checked[i] = True
        op, arg = operations[i]
        match op:
            case "nop":
                i += 1

            case "acc":
                accumulator += arg
                i += 1

            case "jmp":
                i += arg

    return accumulator, i == len(operations)


def main() -> None:
    operations = [line.strip().split() for line in sys.stdin]
    operations = [(op, int(arg)) for op, arg in operations]
    for i in range(len(operations)):
        if operations[i][0] != "acc":
            prev = operations[i][0]
            operations[i] = ("nop" if prev == "jmp" else "jmp", operations[i][1])
            accumulator, finished = run_successfully(operations)
            if finished:
                print(accumulator)
                break

            operations[i] = (prev, operations[i][1])


if __name__ == "__main__":
    main()
