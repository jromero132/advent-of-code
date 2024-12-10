"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=7 ; task=2)
"""

import sys
from itertools import permutations
from typing import Union


class IntCodeAmplifier:
    """
    IntCodeAmplifier class for executing Intcode programs.

    This class encapsulates the functionality to run an Intcode program using a specified memory and input values. It
    provides methods to execute various instructions, including arithmetic operations, input/output handling, and
    control flow jumps.

    Attributes:
        _memory (list[int]): The list representing the Intcode program's memory.
        _inp (list[int | IntCodeAmplifier]): The list of input values or other IntCodeAmplifier instances.
        _inp_index (int): The current index for input retrieval.
        _index (int): The current instruction pointer index.
        buffer (int | None): The output buffer for storing the last output value.
        finished (bool): A flag indicating whether the program has finished execution.

    """

    def __init__(self, memory: list[int], inp: list[Union[int, "IntCodeAmplifier"]]):
        """
        Initialize an IntCodeAmplifier instance.

        This constructor initializes the IntCodeAmplifier with the provided memory and input values. It sets up the
        necessary attributes for executing the Intcode program, including the current instruction pointer and input
        index.

        Args:
            memory (list[int]): The list representing the Intcode program's memory.
            inp (list[int | IntCodeAmplifier]): The list of input values or other IntCodeAmplifier instances.

        """
        self._memory = memory
        self._inp = inp
        self._inp_index = 0
        self._index = 0
        self.buffer = None
        self.finished = False

    def _get_param(self, param: int) -> int:
        """
        Retrieve a parameter value from memory based on the given index and parameter mode.

        This function checks the mode of the parameter to determine whether to return the value directly
        from memory or to dereference it. It supports both immediate and positional parameter modes.

        Args:
            param (int): The parameter index to retrieve.

        Returns:
            int: The value of the parameter based on its mode.

        """
        return (
            self._memory[self._index + param]
            if (self._memory[self._index] // (10 ** (1 + param))) % 10 == 1
            else self._memory[self._memory[self._index + param]]
        )

    def _execute_arithmetic(self) -> None:  # opcode = 1, 2, 7, 8
        """
        Execute arithmetic operations based on the provided opcode.

        This function performs arithmetic operations on two parameters retrieved from memory based on the provided
        opcode. The supported operations are addition (1), multiplication (2), less than comparison (7) and equality
        comparison (8).

        """
        opcode = self._memory[self._index] % 10
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        if opcode == 1:
            ans = param1 + param2

        elif opcode == 2:
            ans = param1 * param2

        elif opcode == 7:
            ans = int(param1 < param2)

        else:  # opcode == 8
            ans = int(param1 == param2)

        self._memory[self._memory[self._index + 3]] = ans
        self._index += 4

    def _execute_input(self) -> None:  # opcode = 3
        """
        Execute input operations by storing a predefined value in memory.

        This function takes the current instruction pointer index and stores a specified input value in memory at the
        location indicated by the parameter. It then returns the updated instruction pointer index.

        """
        if isinstance(self._inp[self._inp_index], int):
            inp = self._inp[self._inp_index]
            self._inp_index += 1

        else:  # IntCodeAmplifier
            inp = self._inp[self._inp_index].buffer

        self._memory[self._memory[self._index + 1]] = inp
        self._index += 2

    def _execute_output(self) -> None:  # opcode = 4
        """
        Execute output operations by retrieving a parameter value from memory.

        This function retrieves a value from memory based on the current instruction pointer index and the specified
        parameter. It returns the updated instruction pointer index along with the retrieved value.

        """
        self.buffer = self._get_param(1)
        self._index += 2

    def _execute_jump(self) -> None:  # opcode = 5, 6
        """
        Execute jump operations based on the provided opcode.

        This function evaluates the parameters to determine whether to jump to a new instruction pointer index based on
        the opcode. It supports conditional jumps for both non-zero and zero values.

        """
        opcode = self._memory[self._index] % 10
        param1 = self._get_param(1)
        param2 = self._get_param(2)
        self._index = (
            param2
            if (opcode == 5 and param1 != 0) or (opcode == 6 and param1 == 0)
            else self._index + 3
        )

    def _execute_instruction(self) -> None:
        """
        Execute a specific instruction based on the provided opcode.

        This function determines the type of operation to perform based on the opcode and calls the corresponding
        function to execute the instruction. It handles arithmetic operations, input/output operations, and jumps,
        returning the updated instruction pointer index and the output value.

        """
        opcode = self._memory[self._index] % 10
        match opcode:
            case 1 | 2 | 7 | 8:
                self._execute_arithmetic()

            case 3:
                self._execute_input()

            case 4:
                self._execute_output()

            case 5 | 6:
                self._execute_jump()

            case _:  # Error
                pass

    def add_input(self, inp: Union[int, "IntCodeAmplifier"]) -> None:
        """
        Add an input value to the amplifier's input queue.

        This function appends a new input value, which can be either an integer or another IntCodeAmplifier instance,
        to the input list. This allows the amplifier to process additional input values during execution.

        Args:
            inp (int | IntCodeAmplifier): The input value to be added to the input queue.

        """
        self._inp.append(inp)

    def run(self) -> None:
        """
        Run the Intcode program with the provided memory and inputs.

        This function processes the Intcode instructions stored in memory, using the provided inputs to execute the
        program. It continues executing until it encounters the halt instruction (99) and returns the final output
        value.

        """
        previous_buffer = self.buffer
        self.buffer = None
        while (
            self._index < len(self._memory)
            and self._memory[self._index] != 99
            and self.buffer is None
        ):
            self._execute_instruction()

        if self._memory[self._index] == 99:
            self.finished = True
            self.buffer = self.buffer or previous_buffer


def main() -> None:
    amplifiers_cnt = 5
    initial_memory = [int(n) for n in sys.stdin.readline().split(",")]
    ans = 0
    for permutation in permutations(range(amplifiers_cnt, 2 * amplifiers_cnt)):
        amplifiers = [IntCodeAmplifier(initial_memory.copy(), [permutation[0], 0])]
        amplifiers.extend(
            IntCodeAmplifier(initial_memory.copy(), [permutation[i], amplifiers[i - 1]])
            for i in range(1, len(permutation))
        )
        amplifiers[0].add_input(amplifiers[-1])

        while not amplifiers[-1].finished:
            for amplifier in amplifiers:
                amplifier.run()

        ans = max(ans, amplifiers[-1].buffer)
    print(ans)


if __name__ == "__main__":
    main()
