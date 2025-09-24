"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=20 ; task=2)
"""

import sys
from enum import Enum
from math import lcm


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
    target_module = None
    for m in modules.values():
        if "rx" in m.out:
            target_module = m.name

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
    cycles = {m: 0 for m in modules[target_module].inp}
    n_cycles = 0

    while not all(cycles.values()):
        n_cycles += 1
        queue = [(modules["broadcaster"], Pulse.LOW)]

        while queue:
            module, pulse = queue.pop(0)

            if module.typ == "%" and pulse == Pulse.HIGH:
                continue

            elif module.typ == "%":
                pulse = Pulse.LOW if module.state == ModuleState.ON else Pulse.HIGH
                module.state = ModuleState.ON if module.state == ModuleState.OFF else ModuleState.OFF

            elif module.typ == "&":
                pulse = Pulse.LOW if all(v == Pulse.HIGH for v in module.memory.values()) else Pulse.HIGH

                if module.name == target_module and any(v == Pulse.HIGH for v in module.memory.values()):
                    for m in module.memory:
                        if module.memory[m] == Pulse.HIGH and cycles[m] == 0:
                            cycles[m] = n_cycles

            for m in module.out:
                queue.append((m, pulse))

                if m.typ == "&":
                    m.memory[module.name] = pulse

    print(lcm(*cycles.values()))


if __name__ == "__main__":
    main()

# 4013 {'nx': 3851, 'sp': 4013, 'cc': 4001, 'jq': 3911}
# task 2: 241823802412393
