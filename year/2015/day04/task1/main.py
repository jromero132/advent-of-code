"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=4 ; task=1)
"""

import hashlib
import sys


def main():
    secret_key = sys.stdin.readline().strip()
    n, hash = 0, ""
    while not hash.startswith("00000"):
        n += 1
        hash = hashlib.md5(f"{secret_key}{n}".encode()).hexdigest()

    print(n)


if __name__ == "__main__":
    main()
