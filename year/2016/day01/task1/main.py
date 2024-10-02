"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=1 ; task=1)
"""


def main():
    line = input()
    x, y = 0, 0
    dx, dy = 0, 1
    for cmd in line.split(", "):
        if not cmd:
            continue

        steps = int(cmd[1:])
        dx, dy = (dy, -dx) if cmd[0] == "R" else (-dy, dx)
        x += dx * steps
        y += dy * steps

    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
