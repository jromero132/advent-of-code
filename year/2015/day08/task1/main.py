"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=8 ; task=1)
"""

import sys
from string import hexdigits


def is_hex_string(s: str) -> bool:
    """
        Determine if a string represents a valid hexadecimal escape sequence.

    Args:
        s (str): The string to be evaluated for a hex escape sequence.

    Returns:
        bool: True if the string is a valid hex escape sequence, False otherwise.

    """
    return len(s) == 4 and s[:2] == "\\x" and all(c in hexdigits for c in s[2:])


def main() -> None:
    chars_of_code, chars_in_memory = 0, 0
    for line in (line.strip() for line in sys.stdin):
        chars_of_code += len(line)

        i = 1
        while i < len(line) - 1:  # from 1...-1 since the string starts and ends with a double quote
            if line[i : i + 2] in ('\\"', "\\\\"):
                i += 1

            elif is_hex_string(line[i : i + 4]):
                i += 3

            chars_in_memory += 1
            i += 1

    print(chars_of_code - chars_in_memory)


if __name__ == "__main__":
    main()
