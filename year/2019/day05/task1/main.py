"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=5 ; task=1)
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


def execute_arithmetic(memory: list[int], i: int, opcode: int) -> int:  # opcode = 1, 2
    """
    Execute arithmetic operations based on the provided opcode.

    This function retrieves two parameters from memory and performs either addition (1) or multiplication (2) based on
    the opcode. The result is stored back in memory at the specified location.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.
        opcode (int): The operation code indicating the arithmetic operation (1 for addition, 2 for multiplication).

    Returns:
        int: The updated instruction pointer index after executing the operation.

    """
    param1 = get_param(memory, i, 1)
    param2 = get_param(memory, i, 2)
    memory[memory[i + 3]] = param1 + param2 if opcode == 1 else param1 * param2
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
    memory[memory[i + 1]] = 1  # Initial input
    return i + 2


def execute_output(memory: list[int], i: int) -> tuple[int, int]:  # opcode = 4
    """
    Execute output operations by retrieving a parameter value from memory.

    This function retrieves a value from memory based on the current instruction pointer index and the specified
    parameter. It returns the updated instruction pointer index along with the retrieved value.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.

    Returns:
        tuple[int, int]: A tuple containing the updated instruction pointer index and the retrieved value.

    """
    return i + 2, get_param(memory, i, 1)


def execute_instruction(memory: list[int], i: int, opcode: int, output: int) -> tuple[int, int]:
    """
    Execute a specific instruction based on the provided opcode.

    This function determines the type of operation to perform based on the opcode and calls the corresponding
    function to execute the instruction. It returns the updated instruction pointer index and the output value.

    Args:
        memory (list[int]): The list representing the memory.
        i (int): The current instruction pointer index.
        opcode (int): The operation code indicating the type of instruction to execute.
        output (int): The current output value.

    Returns:
        tuple[int, int]: A tuple containing the updated instruction pointer index and the output value.

    """
    if opcode in (1, 2):
        return execute_arithmetic(memory, i, opcode), output

    if opcode == 3:
        return execute_input(memory, i), output

    if opcode == 4:
        assert output == 0
        return execute_output(memory, i)

    return None  # Error case


def run_intcode(memory: list[int]) -> int:
    """
    Run the Intcode program using the provided memory.

    This function processes the instructions in the memory until it encounters the halt instruction (99). It executes
    each instruction in sequence and returns the final output value.

    Args:
        memory (list[int]): The list representing the memory containing the Intcode program.

    Returns:
        int: The final output value after executing the Intcode program.

    """
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
