"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=12 ; task=1)
"""

import sys


def get_number_of_arrangements(s: list[str], i: int, sizes: list[int], j: int, memo: dict) -> int:
    if i == len(s):
        return j == len(sizes)

    key = (s[i], i, j)
    if key not in memo:
        match s[i]:
            case ".":
                memo[key] = get_number_of_arrangements(s, i + 1, sizes, j, memo)

            case "#":
                if j == len(sizes) or i + sizes[j] > len(s) or "." in s[i : i + sizes[j]]:
                    memo[key] = 0

                else:
                    nxt = i + sizes[j]
                    if nxt < len(s) and s[nxt] == "#":
                        memo[key] = 0

                    else:
                        memo[key] = get_number_of_arrangements(
                            s,
                            nxt + (nxt < len(s) and s[nxt] == "?"),
                            sizes,
                            j + 1,
                            memo,
                        )

            case "?":
                s[i] = "."
                ans = get_number_of_arrangements(s, i, sizes, j, memo)
                s[i] = "#"
                ans += get_number_of_arrangements(s, i, sizes, j, memo)
                s[i] = "?"
                memo[key] = ans

    return memo[key]


def main() -> None:
    ans = 0
    for line in sys.stdin:
        s, sizes = line.strip().split()
        s = list(s)
        sizes = [int(x) for x in sizes.split(",")]
        ans += get_number_of_arrangements(s, 0, sizes, 0, {})

    print(ans)


if __name__ == "__main__":
    main()
