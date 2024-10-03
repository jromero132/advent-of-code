"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=2 ; task=1)
"""

import sys


def is_valid_game(game: str) -> bool:
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


def main():
    ans = 0
    for line in sys.stdin:
        game_id, game = line.split(":")
        ans += is_valid_game(game) * int(game_id.split()[1])

    print(ans)


if __name__ == "__main__":
    main()
