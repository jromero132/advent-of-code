"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=10 ; task=2)
"""

import sys

from scipy.optimize import linprog


def main() -> None:
    ans = 0
    for line in sys.stdin:
        config = line.strip().split()

        # Parse target joltage values (last item in {curly braces})
        target = [int(i) for i in config[-1][1:-1].split(",")]

        # Build constraint matrix: each button contributes +1 to specified counters
        # btns[i][j] = 1 if button i affects counter j, else 0
        btns = []
        for btn in config[1:-1]:
            btns.append([0] * len(target))
            for i in map(int, btn[1:-1].split(",")):
                btns[-1][i] = 1

        # Solve: minimize sum(x_i) where each x_i = number of times to press button i
        # Subject to: A*x = b, where A is the transposed button matrix
        # integrality=True forces integer solutions (can't press button 0.5 times)
        result = linprog(
            [1] * len(btns),  # Objective: minimize total presses
            A_eq=list(zip(*btns)),  # Equality constraints matrix (transposed)
            b_eq=target,  # Target result: joltage values
            integrality=True,  # Integer programming (not just linear)
        )
        ans += int(result.fun)  # Add minimal presses for this machine

    print(ans)


if __name__ == "__main__":
    main()
