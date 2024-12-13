"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=8 ; task=1)
"""

import sys


def main() -> None:
    picture = sys.stdin.read().strip()
    wide, tall = (3, 2) if len(picture) <= 20 else (25, 6)
    layer_size = wide * tall
    layers = len(picture) // layer_size

    ans, min_zeros = 0, layer_size
    for l in range(layers):
        zeros, ones, twos = 0, 0, 0
        for c in picture[l * layer_size : (l + 1) * layer_size]:
            zeros += c == "0"
            ones += c == "1"
            twos += c == "2"

        if zeros < min_zeros:
            min_zeros = zeros
            ans = ones * twos

    print(ans)


if __name__ == "__main__":
    main()
