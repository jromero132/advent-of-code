"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=8 ; task=2)
"""

import sys


def main() -> None:
    picture = sys.stdin.read().strip()
    wide, tall = (2, 2) if len(picture) <= 20 else (25, 6)
    layer_size = wide * tall
    layers = len(picture) // layer_size
    image = []
    for i in range(tall):
        image.append([])
        for j in range(wide):
            image[-1].append(
                next(
                    pixel
                    for pixel in (picture[l * layer_size + i * wide + j] for l in range(layers))
                    if pixel != "2"
                ),
            )
    for row in image:
        for pixel in row:
            print("█" if pixel == "0" else "░", end="")
        print()
    # Output: GZKJY


if __name__ == "__main__":
    main()
