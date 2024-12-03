"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=4 ; task=1)
"""

import hashlib
import sys


def main() -> None:
    secret_key = sys.stdin.readline().strip()
    n, hashing = 0, ""
    while not hashing.startswith("00000"):
        n += 1
        hashing = hashlib.md5(f"{secret_key}{n}".encode()).hexdigest()

    print(n)


if __name__ == "__main__":
    main()
