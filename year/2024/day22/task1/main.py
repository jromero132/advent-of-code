"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=22 ; task=1)
"""

import sys


def main() -> None:
    universe = (1 << 24) - 1  # used for pruning; to calculate modulo 16777216
    ans = 0
    for line in sys.stdin:
        secret_number = int(line.strip())
        for _ in range(2000):
            secret_number = (
                secret_number ^ (secret_number << 6)
            ) & universe  # multiply by 64 and prune
            secret_number = (
                secret_number ^ (secret_number >> 5)
            ) & universe  # divide by 32 and prune
            secret_number = (
                secret_number ^ (secret_number << 11)
            ) & universe  # multiply by 2048 and prune

        ans += secret_number
    print(ans)


if __name__ == "__main__":
    main()
