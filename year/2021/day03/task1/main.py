"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=3 ; task=1)
"""

import sys


def get_bit(op: callable, idx: int, data: list[str]) -> str:
    """
    Determine the least/most common bit at a specified index in a list of binary strings.

    This function counts the occurrences of '0' and '1' at a given index across all binary strings
    in the provided data. It applies a specified operation (min/max) to decide which bit (either '0'
    or '1') should be returned based on the counts.

    Args:
        op (callable): Either the min or max built-in function in order to get the least or the most
            common bit respectively.
        idx (int): The index in the binary strings to evaluate.
        data (list[str]): A list of binary strings to analyze.

    Returns:
        str: The least/most common bit ('0' or '1') at the specified index.

    """
    cnt = sum(val[idx] == "0" for val in data)
    return op((cnt, "0"), (len(data) - cnt, "1"))[1]


def main() -> None:
    data = [line.strip() for line in sys.stdin]
    gamma = "".join(get_bit(max, i, data) for i in range(len(data[0])))  # most common bit
    epsilon = "".join(get_bit(min, i, data) for i in range(len(data[0])))  # least common bit
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    main()
