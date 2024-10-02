"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=2 ; task=2)
"""

import sys


def get_solution(line1: str, line2: str) -> str:
    if len(line1) < len(line2):
        line1, line2 = line2, line1

    if len(line1) != len(line2):
        return line2 if line1.startswith(line2) or line1.endswith(line2) else None

    p = -1
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            if p == -1:
                p = i

            else:
                return None

    return line1[:p] + line1[p + 1 :]


def main():
    prev_lines = []
    for line in sys.stdin:
        for prev_line in prev_lines:
            if sol := get_solution(prev_line, line):
                print(sol)
                return

        prev_lines.append(line)


if __name__ == "__main__":
    main()
