"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=4 ; task=1)
"""

import sys


def check_win(board: list[list[str]], i: int, j: int) -> bool:
    """Determine if after marking a number at (i, j) results in a winning condition.

    This function checks if all numbers in the specified row or column of the board have been
    marked. It returns a boolean indicating whether the current marking leads to a win.

    Args:
        board (list[list[str]]): The bingo game board represented as a list of lists.
        i (int): The row index of the marked number.
        j (int): The column index of the marked number.

    Returns:
        bool: True if the marking results in a win, False otherwise.
    """
    return all(board[i][k].startswith("-") for k in range(len(board[i]))) or all(
        board[k][j].startswith("-") for k in range(len(board))
    )


def is_winning_number(board: list[list[str]], num: str) -> bool:
    """Mark a number on the bingo board and check for a winning condition.

    This function searches for a specified number on the board, marks it if found, and checks if
    this marking results in a winning condition. It returns a boolean indicating whether the marking
    led to a win.

    Args:
        board (list[list[str]]): The bingo game board represented as a list of lists.
        num (str): The number to be marked on the board.

    Returns:
        bool: True if marking the number results in a win, False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == num:
                board[i][j] = f"-{num}"
                return check_win(board, i, j)
    return False


def get_board_sum(board: list[list[str]]):
    """Calculate the sum of unmarked cells in the bingo board.

    This function iterates through the board and sums the values of all cells that have not been
    marked. It returns the total sum of these unmarked cells.

    Args:
        board (list[list[str]]): The game board represented as a list of lists.

    Returns:
        int: The sum of all unchecked cells in the board.
    """
    return sum(int(x) for row in board for x in row if not x.startswith("-"))


def main():
    nums_to_call = sys.stdin.readline().split(",")  # get bingo numbers to call
    boards = [line.strip() for line in sys.stdin.readlines() if line != "\n"]
    boards = [  # bingo boards
        [line.split() for line in boards[i : i + 5]] for i in range(0, len(boards), 5)
    ]

    for num in nums_to_call:  # call numbers
        for board in boards:  # mark them in every board
            if is_winning_number(board, num):
                print(get_board_sum(board) * int(num))
                return


if __name__ == "__main__":
    main()
