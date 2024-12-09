"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=7 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin.read().splitlines():
        brackets, aba, bab = 0, set(), set()
        for i in range(len(line) - 2):
            if line[i] == "[":
                brackets += 1

            elif line[i] == "]":
                brackets -= 1

            elif line[i] != line[i + 1] and line[i] == line[i + 2]:
                if brackets == 0:
                    aba.add(line[i : i + 3])

                else:
                    bab.add(
                        line[i + 1] + line[i] + line[i + 1],
                    )  # converting 'bab' into 'aba' in order to match

        ans += len(aba.intersection(bab)) > 0
    print(ans)


if __name__ == "__main__":
    main()
