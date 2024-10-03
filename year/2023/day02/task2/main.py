"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=2 ; task=2)
"""

import sys


def solve(game: str) -> int:
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
