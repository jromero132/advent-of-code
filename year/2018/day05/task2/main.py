"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=5 ; task=2)
"""

import sys


def get_measure_of_reaction(polymer: str) -> int:
    """Calculate the measure of a polymer reaction by removing the reactive units.

    This function processes the polymer string and returns the length of the remaining units after
    all possible reactions.

    Args:
        polymer (str): The input string representing the polymer.

    Returns:
        int: The length of the polymer after all reactions have been completed.
    """
    stack, idx = [], 0
    while idx < len(polymer):
        # Check if there are units to react at the left and they can react, since A...Z => 65...90
        # and a...z => 97...122 so 'A' - 'a' = -32 and 'a' - 'A' = 32 and so on.
        # The units are stored in a stack so I can easily access them from the latest to the newest
        # stored, i.e. from right to left.
        if stack and abs(ord(stack[-1]) - ord(polymer[idx])) == 32:
            stack.pop()

        else:
            stack.append(polymer[idx])

        idx += 1
    return len(stack)


def main():
    line = sys.stdin.readline().strip()
    checked = [False] * len(line)
    ans = len(line)
    for i in range(len(checked)):
        if not checked[i]:  # If this letter has not been removed, remove it and check the size
            polymer = line[:i]  # Since this letter has not been removed, it's its first appearance
            for j in range(i, len(checked)):
                if abs(ord(line[i]) - ord(line[j])) in (0, 32):  # 'A' - 'A' = 0 and 'A' - 'a' = -32
                    checked[j] = True

                else:
                    polymer += line[j]

            ans = min(ans, get_measure_of_reaction(polymer))
    print(ans)


if __name__ == "__main__":
    main()
