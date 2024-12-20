"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=4 ; task=2)
"""

import sys


def is_valid_password(password: str) -> bool:
    """
    Check if a password is valid based on specific criteria.

    This function determines the validity of a password by ensuring it is non-decreasing and
    contains at least one pair of adjacent matching digits. It returns a boolean indicating whether
    the password meets these requirements.

    Note that the other criteria (6-digit number and within the range given in input) are ensured
    before calling this method.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.

    """
    two_equals, equals = False, 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            equals += 1

        else:
            two_equals |= equals == 2
            equals = 1

        if password[i] < password[i - 1]:
            return False

    return two_equals or equals == 2


def main() -> None:
    lower_bound, upper_bound = (int(n) for n in sys.stdin.readline().split("-"))
    print(
        sum(
            is_valid_password(str(n))
            for n in range(max(10**5, lower_bound), min(upper_bound + 1, 10**6))  # 6-digit number
        ),
    )


if __name__ == "__main__":
    main()
