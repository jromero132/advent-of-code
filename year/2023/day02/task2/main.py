"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=2 ; task=2)
"""

import sys


def solve(game: str) -> int:
    """Calculate the product of the maximum counts of revealed balls by color.

    This function processes a game string to determine the maximum number of balls revealed for each
    color (red, green, blue) and returns the product of these maximum counts. The game string is
    formatted as "count color; ..." for each reveal.

    Args:
        game (str): A string representing the game reveals, formatted as "count color; ...".

    Returns:
        int: The product of the maximum counts of red, green, and blue balls revealed.
    """
    color_id = {"red": 0, "green": 1, "blue": 2}
    balls = [0, 0, 0]
    for reveal in game.split(";"):
        for ball_reveal in reveal.split(","):
            cnt, color = ball_reveal.strip().split()
            balls[color_id[color]] = max(balls[color_id[color]], int(cnt))

    return balls[0] * balls[1] * balls[2]


def main():
    ans = 0
    for line in sys.stdin:
        game_id, game = line.split(":")
        ans += solve(game)

    print(ans)


if __name__ == "__main__":
    main()
