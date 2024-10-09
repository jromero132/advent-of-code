"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=5 ; task=1)
"""

import sys


def main():
    line = sys.stdin.readline().strip()
    stack, idx = [], 0
    while idx < len(line):
        # Check if there are units to react at the left and they can react, since A...Z => 65...90
        # and a...z => 97...122 so 'A' - 'a' = -32 and 'a' - 'A' = 32 and so on.
        # The units are stored in a stack so I can easily access them from the latest to the newest
        # stored, i.e. from right to left.
        if stack and abs(ord(stack[-1]) - ord(line[idx])) == 32:
            stack.pop()

        else:
            stack.append(line[idx])

        idx += 1

    print(len(stack))


if __name__ == "__main__":
    main()
