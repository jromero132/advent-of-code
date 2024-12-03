"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=5 ; task=1)
"""

import sys


def main() -> None:
    input_parts = sys.stdin.read().split("\n\n")
    starting_stacks = input_parts[0].split("\n")
    size = len(starting_stacks[-1].split())  # get how many crates are there
    crates = [[] for _ in range(size)]  # stacks

    for line in reversed(starting_stacks[:-1]):  # parsing the initial state
        for i in range(len(line) // 4 + 1):
            char = line[i * 4 + 1]
            if char != " ":
                crates[i].append(char)

    for line in input_parts[1].strip().split("\n"):  # making moves
        line_splitted = line.split()
        cnt = int(line_splitted[1])
        from_ = int(line_splitted[3]) - 1
        to = int(line_splitted[5]) - 1

        # move 'cnt' crates one by one from stack 'from_' to stack 'to', so they go in reverse order
        crates[to].extend(crates[from_][-cnt:][::-1])
        crates[from_] = crates[from_][:-cnt]

    print(
        "".join("" if len(crates[i]) == 0 else crates[i].pop() for i in range(len(crates)))
    )  # get final state


if __name__ == "__main__":
    main()
