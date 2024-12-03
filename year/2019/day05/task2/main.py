"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=5 ; task=2)
"""

import sys


def get_param(memory: list[int], idx: int, param: int) -> int:
    """
    Retrieve a parameter value from memory based on the given index and parameter mode.

    This function checks the mode of the parameter to determine whether to return the value directly
    from memory or to dereference it. It supports both immediate and positional parameter modes.

    Args:
        memory (list[int]): The list representing the memory.
        idx (int): The current instruction pointer index.
        param (int): The parameter index to retrieve.

    Returns:
        int: The value of the parameter based on its mode.

    """
    return (
        memory[idx + param]
        if (memory[idx] // (10 ** (1 + param))) % 10 == 1
        else memory[memory[idx + param]]
    )


def execute_arithmetic(memory: list[int], i: int, opcode: int) -> int:  # opcode = 1, 2, 7, 8
    """
    Execute arithmetic operations based on the provided opcode.

    This function performs arithmetic operations on two parameters retrieved from memory based on the provided opcode.
    The supported operations are addition (1), multiplication (2), less than comparison (7) and equality comparison (8).

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.
        opcode (int): The operation code indicating the arithmetic operation (1 for addition, 2 for multiplication,
            7 for less than comparison, 8 for equality comparison).

    Returns:
        int: The updated instruction pointer index after executing the operation.

    """
    param1 = get_param(memory, i, 1)
    param2 = get_param(memory, i, 2)

    if opcode == 1:
        ans = param1 + param2

    elif opcode == 2:
        ans = param1 * param2

    elif opcode == 7:
        ans = int(param1 < param2)

    else:  # opcode == 8
        ans = int(param1 == param2)

    memory[memory[i + 3]] = ans
    return i + 4


def execute_input(memory: list[int], i: int) -> int:  # opcode = 3
    """
    Execute input operations by storing a predefined value in memory.

    This function takes the current instruction pointer index and stores a specified input value in memory at the
    location indicated by the parameter. It then returns the updated instruction pointer index.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.

    Returns:
        int: The updated instruction pointer index after executing the input operation.

    """
    memory[memory[i + 1]] = 5  # Initial input
    return i + 2


def execute_output(memory: list[int], i: int) -> int:  # opcode = 4
    """
    Execute output operations by retrieving a parameter value from memory.

    This function retrieves a value from memory based on the current instruction pointer index and the specified
    parameter. It returns the updated instruction pointer index along with the retrieved value.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.

    Returns:
        int: The updated instruction pointer index after executing the output operation.

    """
    return i + 2, get_param(memory, i, 1)


def execute_jump(memory: list[int], i: int, opcode: int) -> int:  # opcode = 5, 6
    """
    Execute jump operations based on the provided opcode.

    This function evaluates the parameters to determine whether to jump to a new instruction pointer index based on the
    opcode. It supports conditional jumps for both non-zero and zero values.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.
        opcode (int): The operation code indicating the type of jump (5 for jump-if-true, 6 for jump-if-false).

    Returns:
        int: The updated instruction pointer index after evaluating the jump condition.

    """
    param1 = get_param(memory, i, 1)
    param2 = get_param(memory, i, 2)
    return param2 if (opcode == 5 and param1 != 0) or (opcode == 6 and param1 == 0) else i + 3


def execute_instruction(memory: list[int], i: int, opcode: int, output: int) -> int:
    """
    Execute a specific instruction based on the provided opcode.

    This function determines the type of operation to perform based on the opcode and calls the corresponding function
    to execute the instruction. It handles arithmetic operations, input/output operations, and jumps, returning the
    updated instruction pointer index and the output value.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.
        opcode (int): The operation code indicating the type of instruction to execute.
        output (int): The current output value.

    Returns:
        int: The updated instruction pointer index after executing the instruction.

    """
    if opcode in (1, 2, 7, 8):
        return execute_arithmetic(memory, i, opcode), output

    if opcode == 3:
        return execute_input(memory, i), output

    if opcode == 4:
        assert output == 0
        return execute_output(memory, i)

    if opcode in (5, 6):
        return execute_jump(memory, i, opcode), output

    return None  # Error case


def run_intcode(memory: list[int]) -> int:
    i, output = 0, 0
    while i < len(memory) and memory[i] != 99:
        i, output = execute_instruction(memory, i, memory[i] % 10, output)
    return output


def main() -> None:
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    output = run_intcode(memory)
    print(output)


if __name__ == "__main__":
    main()
