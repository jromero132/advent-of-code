"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=9 ; task=2)
"""

import sys
from collections import defaultdict
from collections.abc import Iterable


class IntCode:
    def __init__(self, memory: list[int], initial_input: int) -> None:
        self.memory = defaultdict(int, enumerate(memory))
        self.initial_input = initial_input
        self.idx = 0
        self.base = 0

    def get_param(self, param: int) -> int:
        mode = (self.memory[self.idx] // (10 ** (1 + param))) % 10
        if mode == 0:
            return self.memory[self.idx + param]

        if mode == 1:
            return self.idx + param

        return self.base + self.memory[self.idx + param]

    def execute_arithmetic(self) -> None:  # opcode = 1, 2, 7, 8
        param1 = self.memory[self.get_param(1)]
        param2 = self.memory[self.get_param(2)]
        output = self.get_param(3)

        match self.memory[self.idx] % 10:
            case 1:
                ans = param1 + param2

            case 2:
                ans = param1 * param2

            case 7:
                ans = int(param1 < param2)

            case 8:
                ans = int(param1 == param2)

        self.memory[output] = ans
        self.idx += 4

    def execute_input(self) -> None:  # opcode = 3
        param = self.get_param(1)
        self.memory[param] = self.initial_input
        self.idx += 2

    def execute_output(self) -> int:  # opcode = 4
        out = self.memory[self.get_param(1)]
        self.idx += 2
        return out

    def execute_jump(self) -> None:  # opcode = 5, 6
        param1 = self.memory[self.get_param(1)]
        param2 = self.memory[self.get_param(2)]
        opcode = self.memory[self.idx] % 10
        self.idx = (
            param2
            if (opcode == 5 and param1 != 0) or (opcode == 6 and param1 == 0)
            else self.idx + 3
        )

    def execute_adjustment(self) -> None:  # opcode = 9
        param1 = self.memory[self.get_param(1)]
        self.base += param1
        self.idx += 2

    def run(self) -> Iterable[int]:
        while self.idx < len(self.memory) and self.memory[self.idx] != 99:
            match self.memory[self.idx] % 10:
                case 1 | 2 | 7 | 8:
                    self.execute_arithmetic()

                case 3:
                    self.execute_input()

                case 4:
                    yield self.execute_output()

                case 5 | 6:
                    self.execute_jump()

                case 9:
                    self.execute_adjustment()


def main() -> None:
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    intcode = IntCode(memory, 2)
    print(next(intcode.run()))


if __name__ == "__main__":
    main()
