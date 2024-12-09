"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=9 ; task=1)
"""

import sys


def main() -> None:
    line = sys.stdin.read().strip()
    memory = []
    for i in range(len(line)):
        _id = i // 2 if i % 2 == 0 else -1
        memory.extend([_id] * int(line[i]))

    i, j = 0, len(memory) - 1
    while i < j:
        if memory[i] != -1:
            i += 1

        elif memory[j] == -1:
            j -= 1

        else:
            memory[i] = memory[j]
            memory[j] = -1
            i += 1
            j -= 1

    print(sum(i * memory[i] for i in range(len(memory)) if memory[i] != -1))


if __name__ == "__main__":
    main()
