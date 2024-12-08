"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=7 ; task=1)
"""

import sys
from collections.abc import Callable


def ternary_search(
    nums: list[int],
    f: Callable[[int, list[int]], int],
    left: int,
    right: int,
) -> int:
    """
    Perform a ternary search on a list to find the optimal index based on a given function.

    This function iteratively narrows down the search space to locate the index that maximizes or minimizes the value
    returned by the provided function. It continues until the search space is reduced to a single index.

    Args:
        nums (list[int]): The list of integers to search through.
        f (Callable[[int, list[int]], int]): The function that the ternary search will be based on. This is a function
            that takes an integer and the list of numbers and returns an integer value.
        left (int): The starting index of the search range.
        right (int): The ending index of the search range.

    Returns:
        int: The index that corresponds to the optimal value as determined by the function f.

    """
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid, nums) > f(mid + 1, nums):
            left = mid + 1
        else:
            right = mid
    return left


def f(p: int, nums: list[int]) -> int:
    """
    Calculate the sum of absolute differences between a given point and elements in a list.

    This function takes an integer point and a list of integers, returning the total of the absolute differences between
    each element in the list and the specified point. It is typically used in optimization problems to evaluate the cost
    associated with a particular point.

    Args:
        p (int): The point to compare against the elements in the list.
        nums (list[int]): The list of integers to calculate differences from.

    Returns:
        int: The sum of absolute differences between the point and each element in the list.

    """
    return sum(abs(x - p) for x in nums)


def main() -> None:
    nums = [int(x) for x in sys.stdin.read().strip().split(",")]
    print(f(ternary_search(nums, f, min(nums), max(nums)), nums))


if __name__ == "__main__":
    main()
