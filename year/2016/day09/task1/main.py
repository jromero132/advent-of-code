"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=9 ; task=1)
"""

import sys


def decompress(msg: str) -> int:
    """
    Calculate the decompressed length of a compressed message.

    The function handles a custom compression format where certain sections are marked for repetition. It computes the
    total length of the message after decompression without actually expanding the entire string.

    Args:
        msg (str): The compressed message string to decompress.

    Returns:
        int: The total length of the decompressed message.

    """
    ans, i = 0, 0
    while i < len(msg):
        if msg[i] == "(":
            p = i + 1
            while msg[p] != ")":
                p += 1
            l, t = (int(x) for x in msg[i + 1 : p].split("x"))
            ans += l * t
            i = p + 1 + l

        else:
            ans += 1
            i += 1
    return ans


def main() -> None:
    line = sys.stdin.read().strip()
    print(decompress(line))


if __name__ == "__main__":
    main()
