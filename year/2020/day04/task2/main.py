"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=4 ; task=2)
"""

import re
import sys


def main():
    required_keys = {  # required keys and validations
        "byr": lambda s: "1920" <= s <= "2002",
        "iyr": lambda s: "2010" <= s <= "2020",
        "eyr": lambda s: "2020" <= s <= "2030",
        "hgt": lambda s: (
            (s[-2:] == "cm" and "150" <= s[:-2] <= "193")
            or (s[-2:] == "in" and "59" <= s[:-2] <= "76")
        ),
        "hcl": lambda s: re.fullmatch(r"#[0-9a-f]{6}", s),
        "ecl": lambda s: s in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda s: len(s) == 9 and s.isdigit(),
    }
    valids = 0
    keys = set()
    for line in sys.stdin:
        line = line.strip()

        if line == "":
            valids += len(keys) == len(required_keys)
            keys = set()

        else:
            for entry in line.split(" "):
                key, value = entry.split(":")
                if key in required_keys and required_keys[key](value):  # check if it's a valid key
                    keys.add(key)

    if len(keys) > 0:  # Special case when there is not final blank line
        valids += len(keys) == len(required_keys)

    print(valids)


if __name__ == "__main__":
    main()
