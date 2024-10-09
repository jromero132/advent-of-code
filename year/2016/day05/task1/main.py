"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=5 ; task=1)
"""

import hashlib
import sys


def main():
    door_id = sys.stdin.readline().strip()
    password, password_length, index = "", 8, 0
    while len(password) != password_length:
        hash_hex = hashlib.md5(f"{door_id}{index}".encode()).hexdigest()
        if hash_hex.startswith("00000"):
            password += hash_hex[5]

        index += 1

    print(password)


if __name__ == "__main__":
    main()
