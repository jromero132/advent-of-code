"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=8 ; task=2)
"""

import sys
from collections import defaultdict


def main() -> None:
    register = defaultdict(int)
    ans = 0
    for instruction in sys.stdin:
        operation, condition = instruction.strip().split(" if ")
        op_parts = operation.split()
        cond_parts = condition.split()
        cond_parts[0] = f'register["{cond_parts[0]}"]'
        cond = " ".join(cond_parts)

        if eval(cond):
            register[op_parts[0]] += (1 if op_parts[1] == "inc" else -1) * int(op_parts[-1])
            ans = max(ans, register[op_parts[0]])

    print(ans)


if __name__ == "__main__":
    main()