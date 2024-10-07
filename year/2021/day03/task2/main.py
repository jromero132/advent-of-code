"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=3 ; task=2)
"""

import sys


def get_bit(op: callable, idx: int, data: list[str]) -> str:
    """Determine the least/most common bit at a specified index in a list of binary strings.

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


def get_value(op: callable, data: list[str]) -> str:
    """Filter a list of binary strings based on a specified operation (min/max) until one remains.

    This function iteratively applies a filtering process to a list of binary strings, using a
    provided operation (min/max) to determine which bit to keep at each index (least common/most
    common). The process continues until only one binary string remains, which is then returned.

    Args:
        op (callable): Either the min or max built-in function in order to get the least or the most
            common bit respectively.
        data (list[str]): A list of binary strings to filter.

    Returns:
        str: The remaining binary string after filtering.
    """
    i = 0
    while len(data) > 1:
        bit = get_bit(op, i, data)
        data = [num for num in data if num[i] == bit]
        i += 1
    return data[0]


def main():
    data = [line.strip() for line in sys.stdin]
    co2 = get_value(max, data)  # most common bit
    oxygen = get_value(min, data)  # least common bit
    print(int(co2, 2) * int(oxygen, 2))


if __name__ == "__main__":
    main()
