"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=5 ; task=1)
"""

import sys


def main() -> None:
    rules, updates = sys.stdin.read().split("\n\n")
    rules = {tuple(line.split("|")) for line in rules.split()}
    updates = [line.split(",") for line in updates.split()]

    ans = 0
    for update in updates:
        valid = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if (update[j], update[i]) in rules:
                    valid = False

        if valid:
            ans += int(update[len(update) // 2])

    print(ans)


if __name__ == "__main__":
    main()
