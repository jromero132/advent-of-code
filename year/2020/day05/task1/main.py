"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=5 ; task=1)
"""

import sys


def decode(s: str) -> int:
    """
    Convert a binary space partitioning string into a binary integer representation.

    This function interprets the characters in the string, where 'B' and 'R' are treated as binary
    '1' and all other characters as binary '0'. The resulting binary string is then converted to an
    integer.

    Args:
        s (str): The binary space partitioning string to decode.

    Returns:
        int: The integer representation of the decoded binary space partitioning.

    """
    return int("".join("1" if c in ("B", "R") else "0" for c in s), 2)


def main() -> None:
    ans = 0
    for bp in (line.strip() for line in sys.stdin):
        ans = max(ans, decode(bp[:7]) * 8 + decode(bp[7:]))

    print(ans)


if __name__ == "__main__":
    main()
