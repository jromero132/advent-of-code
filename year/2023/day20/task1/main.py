"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=20 ; task=1)
"""

import sys
from enum import Enum


class ModuleState(Enum):
    OFF = 0
    ON = 1

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Module:
    def __init__(self, line: str):
        self.name, dest = line.strip("\n").split(" -> ")
        self.inp = {}  # input modules (name: Module)
        self.out = dest.split(", ") if dest else []

        self.typ = ""
        self.state = None

        # For conjunction modules, memory of last pulse from each input
        self.memory = None

        if self.name[0] in "%&":
            self.typ, self.name = self.name[0], self.name[1:]

            if self.typ == "%":
                self.state = ModuleState.OFF

            else:
                self.memory = {}  # input_name: Pulse


def main() -> None:
    modules = {}
    for line in sys.stdin:
        m = Module(line.strip())
        modules[m.name] = m

    end_modules = {}
    for m in modules.values():
        for i in range(len(m.out)):
            if m.out[i] in modules:
                m_out = modules[m.out[i]]
                m.out[i] = m_out
                m_out.inp[m.name] = m

            else:
                end_modules[m.out[i]] = m.out[i] = Module(f"{m.out[i]} -> ")

    # Initialize conjunction module memories to LOW for each input
    for m in modules.values():
        if m.typ == "&":
            for inp_name in m.inp:
                m.memory[inp_name] = Pulse.LOW

    modules = {**modules, **end_modules}

    steps = 1000
    lows, highs = 0, 0
    for _ in range(steps):
        queue = [(modules["broadcaster"], Pulse.LOW)]

        while queue:
            module, pulse = queue.pop(0)

            if pulse == Pulse.LOW:
                lows += 1

            else:
                highs += 1

            if module.typ == "%" and pulse == Pulse.HIGH:
                continue

            elif module.typ == "%":
                pulse = Pulse.LOW if module.state == ModuleState.ON else Pulse.HIGH
                module.state = ModuleState.ON if module.state == ModuleState.OFF else ModuleState.OFF

            elif module.typ == "&":
                pulse = Pulse.LOW if all(v == Pulse.HIGH for v in module.memory.values()) else Pulse.HIGH

            for m in module.out:
                queue.append((m, pulse))

                if m.typ == "&":
                    m.memory[module.name] = pulse

    print(lows * highs)


if __name__ == "__main__":
    main()
