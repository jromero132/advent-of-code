"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=2 ; task=2)
"""

import sys


def main() -> None:
    code = ""
    grid = (
        (
            "",
            "",
            "1",
            "",
            "",
        ),
        (
            "",
            "2",
            "3",
            "4",
            "",
        ),
        (
            "5",
            "6",
            "7",
            "8",
            "9",
        ),
        (
            "",
            "A",
            "B",
            "C",
            "",
        ),
        (
            "",
            "",
            "D",
            "",
            "",
        ),
    )
    r, c = 2, 0
    for line in sys.stdin:
        for i in line:
            nr, nc = r, c
            match i:
                case "U":
                    nr -= 1

                case "R":
                    nc += 1

                case "D":
                    nr += 1

                case "L":
                    nc -= 1

                case _:  # Error
                    pass

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc]:
                r, c = nr, nc

        code += grid[r][c]

    print(code)


if __name__ == "__main__":
    main()
