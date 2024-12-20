"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=4 ; task=1)
"""

import sys


def main() -> None:
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    keys = set()
    for line in sys.stdin:
        line_parts = line.strip()

        if line_parts == "":
            valid += len(keys) == len(required_keys)
            keys = set()

        else:
            for entry in line_parts.split(" "):
                key = entry.split(":")[0]
                if key in required_keys:  # check if this is a valid key
                    keys.add(key)

    if len(keys) > 0:  # Special case when there is not final blank line
        valid += len(keys) == len(required_keys)

    print(valid)


if __name__ == "__main__":
    main()
