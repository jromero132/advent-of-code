"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=1 ; task=2)
"""


def main():
    line = input()
    x, y = 0, 0
    dx, dy = 0, 1
    visited = {(0, 0)}
    for cmd in line.split(", "):
        if not cmd:
            continue

        steps = int(cmd[1:])
        dx, dy = (dy, -dx) if cmd[0] == "R" else (-dy, dx)

        for _ in range(steps):
            x += dx
            y += dy

            if (x, y) in visited:
                print(abs(x) + abs(y))
                return

            visited.add((x, y))


if __name__ == "__main__":
    main()
