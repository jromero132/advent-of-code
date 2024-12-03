"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=1 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for n in sys.stdin:
        module_fuel = int(n)
        while module_fuel > 6:
            module_fuel = module_fuel // 3 - 2
            ans += module_fuel
    print(ans)


if __name__ == "__main__":
    main()
