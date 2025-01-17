"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=15 ; task=2)
"""

import sys


def get_hash(sequence: str) -> int:
    h = 0
    for c in sequence:
        h = (h + ord(c)) * 17 % 256
    return h


def main() -> None:
    sequences = sys.stdin.read().strip().replace("\n", "").split(",")
    boxes = [[] for _ in range(256)]
    focal_lengths = {}
    for sequence in sequences:
        if sequence[-1] == "-":
            label = sequence[:-1]
            box = get_hash(label)
            if label in boxes[box]:
                boxes[box].remove(label)

        else:  # This is for =
            label, focal_length = sequence.split("=")
            box = get_hash(label)
            focal_lengths[label] = int(focal_length)
            if label not in boxes[box]:
                boxes[box].append(label)

    print(
        sum(
            i * j * focal_lengths[label]
            for i, box in enumerate(boxes, start=1)
            for j, label in enumerate(box, start=1)
        ),
    )


if __name__ == "__main__":
    main()
