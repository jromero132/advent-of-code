"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=2 ; task=1)
"""

import sys


def is_valid_game(game: str) -> bool:
    """
    Determine if the game reveals are valid based on ball counts.

    This function checks if the number of balls revealed in each round of the game does not exceed
    the maximum allowed for each color. It processes the game string and returns True if all rounds
    are valid, and False if any round exceeds the limits.

    Args:
        game (str): A string representing the game reveals, formatted as "count color; ...".

    Returns:
        bool: True if all game reveals are valid, False otherwise.

    """
    color_id = {"red": 0, "green": 1, "blue": 2}
    balls = [12, 13, 14]
    for reveal in game.split(";"):
        cur_reveal_balls = [0, 0, 0]
        for ball_reveal in reveal.split(","):
            cnt, color = ball_reveal.strip().split()
            cur_reveal_balls[color_id[color]] += int(cnt)

        if any(max_balls < cur_balls for max_balls, cur_balls in zip(balls, cur_reveal_balls)):
            return False

    return True


def main() -> None:
    ans = 0
    for line in sys.stdin:
        game_id, game = line.split(":")
        ans += is_valid_game(game) * int(game_id.split()[1])

    print(ans)


if __name__ == "__main__":
    main()
