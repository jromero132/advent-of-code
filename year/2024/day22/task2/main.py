"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=22 ; task=1)
"""

import sys
from collections import defaultdict


def main() -> None:
    universe = (1 << 24) - 1  # used for pruning; to calculate modulo 16777216
    sequences = []
    for line in sys.stdin:
        secret_number = int(line.strip())
        sequences.append([secret_number % 10])
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
            sequences[-1].append(secret_number % 10)

    sold = defaultdict(int)
    for seq in sequences:
        checked = set()
        for i in range(4, len(seq)):
            delta = tuple(seq[j] - seq[j - 1] for j in range(i - 3, i + 1))
            if delta not in checked:
                checked.add(delta)
                sold[delta] += seq[i]

    print(max(sold.values()))


if __name__ == "__main__":
    main()
