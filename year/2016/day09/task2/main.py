"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=9 ; task=2)
"""

import sys


def decompress(msg: str, start: int, end: int) -> int:
    """
    Recursively calculates the decompressed length of a compressed message.

    The function computes the total length of a message after decompression, supporting complex nested compression
    formats. It uses a recursive approach to handle multi-level compression markers.

    Args:
        msg (str): The compressed message string to decompress.
        start (int): The inclusive starting index for decompression.
        end (int): The exclusive ending index for decompression.

    Returns:
        int: The total length of the decompressed message segment.

    """
    ans, i = 0, start
    while i != end:
        if msg[i] == "(":
            p = i + 1
            while msg[p] != ")":
                p += 1
            l, t = (int(x) for x in msg[i + 1 : p].split("x"))
            ans += decompress(msg, p + 1, p + 1 + l) * t
            i = p + 1 + l

        else:
            ans += 1
            i += 1
    return ans


def main() -> None:
    line = sys.stdin.read().strip()
    print(decompress(line, 0, len(line)))


if __name__ == "__main__":
    main()
