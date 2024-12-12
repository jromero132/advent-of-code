"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=11 ; task=1)
"""

import sys


def main() -> None:
    total_blinks = 25
    stones = sys.stdin.read().strip().split()
    for _ in range(total_blinks):
        next_step = []
        for s in stones:
            if s == "0":
                next_step.append("1")

            elif len(s) % 2 == 0:
                mid = len(s) // 2
                next_step.extend((s[:mid], str(int(s[mid:]))))

            else:
                next_step.append(str(int(s) * 2024))

        stones = next_step

    print(len(stones))


if __name__ == "__main__":
    main()
