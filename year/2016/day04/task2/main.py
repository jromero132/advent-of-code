"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=4 ; task=2)
"""

import sys


def main() -> None:
    for line in sys.stdin:
        parts = line.split("-")
        p1 = 1
        while p1 < len(parts[-1]) and parts[-1][p1].isdigit():
            p1 += 1

        sector_id = int(parts[-1][:p1])
        parts = "-".join(parts[:-1])
        decrypted_name = "".join(
            " " if c == "-" else chr((ord(c) - 97 + sector_id) % 26 + 97) for c in parts
        )

        if decrypted_name == "northpole object storage":
            print(sector_id)


if __name__ == "__main__":
    main()
