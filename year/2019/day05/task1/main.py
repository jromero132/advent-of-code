"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=5 ; task=1)
"""

import sys
from collections import defaultdict
from collections.abc import Iterable


class IntCode:
    def __init__(self, memory: list[int], initial_input: int) -> None:
        self.memory = defaultdict(int, enumerate(memory))
        self.initial_input = initial_input
        self.idx = 0

    def get_param(self, param: int) -> int:
        mode = (self.memory[self.idx] // (10 ** (1 + param))) % 10
        return self.memory[self.idx + param] if mode == 0 else self.idx + param

    def execute_arithmetic(self) -> None:  # opcode = 1, 2, 7, 8
        param1 = self.memory[self.get_param(1)]
        param2 = self.memory[self.get_param(2)]
        output = self.get_param(3)
        self.memory[output] = (
            param1 + param2 if self.memory[self.idx] % 10 == 1 else param1 * param2
        )
        self.idx += 4

    def execute_input(self) -> None:  # opcode = 3
        param = self.get_param(1)
        self.memory[param] = self.initial_input
        self.idx += 2

    def execute_output(self) -> int:  # opcode = 4
        out = self.memory[self.get_param(1)]
        self.idx += 2
        return out

    def run(self) -> Iterable[int]:
        while self.idx < len(self.memory) and self.memory[self.idx] != 99:
            match self.memory[self.idx] % 10:
                case 1 | 2:
                    self.execute_arithmetic()

                case 3:
                    self.execute_input()

                case 4:
                    yield self.execute_output()


def main() -> None:
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    intcode = IntCode(memory, 1)
    print(list(intcode.run())[-1])


if __name__ == "__main__":
    main()
