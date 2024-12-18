"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=17 ; task=1)
"""

import sys


def get_combo_value(operand: str, registers: list[int]) -> int:
    """
    Retrieve a value based on the operand and registers.

    The function converts the operand to an integer and returns either the direct value (if between 0 and 3, inclusive)
    or a value from the registers list (A -registers[0]- for 4, B -registers[1]- for 5 and C -registers[2]- for 6).

    Args:
        operand (str): A string representing a numeric value to be processed.
        registers (list[int]): A list of integer registers used for value retrieval.

    Returns:
        int: The computed value based on the operand and registers.

    """
    ans = int(operand)
    assert ans != 7  # Error
    return ans if ans <= 3 else registers[ans - 4]


def run(program: list[str], registers: list[int]) -> str:
    """
    Execute a custom program with specific operations on registers.

    The function iterates through the program instructions, performing various bitwise and arithmetic operations on
    registers. It generates an output sequence based on the program's execution and returns the result as a
    comma-separated string.

    Args:
        program (list[str]): A list of program instructions to be executed.
        registers (list[int]): A list of integer registers to be modified during program execution.

    Returns:
        str: A comma-separated string of output values generated during program execution.

    """
    # A <=> registers[0] ; B <=> registers[1] ; C <=> registers[2]
    ans, i = [], 0
    while i < len(program):
        op_code, operand = program[i], program[i + 1]
        i += 2
        match op_code:
            case "0" | "6" | "7":  # adv & bdc & cdv
                idx = 0 if op_code == "0" else 1 if op_code == "6" else 2  # Register A, B or C
                registers[idx] = registers[0] >> get_combo_value(
                    operand,
                    registers,
                )  # >> n == // 2 ** n

            case "1":  # bxl
                registers[1] ^= int(operand)

            case "2":  # bst
                registers[1] = get_combo_value(operand, registers) & 7  # & 7 is the same as % 8

            case "3":  # jnz
                if registers[0]:
                    i = int(operand)

            case "4":  # bxc
                registers[1] ^= registers[2]

            case "5":  # out
                ans.append(str(get_combo_value(operand, registers) & 7))  # & 7 is the same as % 8

    return ",".join(ans)


def main() -> None:
    registers_info, program = sys.stdin.read().split("\n\n")
    registers = [int(register.split()[-1]) for register in registers_info.split("\n")]
    program = program.split()[1].split(",")
    print(run(program, registers))


if __name__ == "__main__":
    main()
