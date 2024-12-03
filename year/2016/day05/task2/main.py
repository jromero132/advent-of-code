"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=5 ; task=2)
"""

import hashlib
import sys


def main() -> None:
    door_id = sys.stdin.readline().strip()
    password, password_length, index = [""] * 8, 0, 0
    while len(password) != password_length:
        hash_hex = hashlib.md5(f"{door_id}{index}".encode()).hexdigest()
        if (
            hash_hex.startswith("00000")
            and "0" <= hash_hex[5] <= "7"
            and password[pos := int(hash_hex[5])] == ""
        ):
            password[pos] = hash_hex[6]
            password_length += 1

        index += 1

    print("".join(password))


if __name__ == "__main__":
    main()
