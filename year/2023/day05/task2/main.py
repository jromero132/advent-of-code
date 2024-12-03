"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=5 ; task=2)
"""

import sys


def get_interception(seg1: list[int], seg2: list[int]) -> list[list[int]]:
    """
    Calculate the interception segments between two integer segments.

    This function determines the overlapping segments between two given segments based on their
    start and length values. It returns a list of segments that represent the areas of intersection.
    If there is an interception, then the first item in the return list will be the actual
    intersection, and if there are other items in the return list, they are the rest of the first
    segment after intercepting it with the second segment. Take into account that the return values
    are already mapped according to the provided map in the problem which is:
        seg2[1] -> seg2[0]
        seg2[1] + 1 -> seg2[0] + 1
        ...
        seg2[1] + seg2[2] - 1 -> seg2[0] + seg2[2] - 1

    Args:
        seg1 (list[int]): A list containing the start position and length of the first segment.
            E.g. [79, 14]
        seg2 (list[int]): A list containing the start position after mapping, the start position of
            the segment and length of the second segment. E.g. [50, 98, 2]

    Returns:
        list[list[int]]: A list of segments that represent the intersections between the two
            segments and the remaining parts of the first segment, if any of those exists.

    """
    if seg2[1] <= seg1[0] and seg1[0] + seg1[1] <= seg2[1] + seg2[2]:
        return [[seg2[0] + seg1[0] - seg2[1], seg1[1]]]

    if seg2[1] <= seg1[0] < seg2[1] + seg2[2]:
        return [
            [seg2[0] + seg1[0] - seg2[1], seg2[1] + seg2[2] - seg1[0]],
            [seg2[1] + seg2[2], seg1[0] + seg1[1] - seg2[1] - seg2[2]],
        ]

    if seg2[1] < seg1[0] + seg1[1] <= seg2[1] + seg2[2]:
        return [
            [seg2[0], seg1[0] + seg1[1] - seg2[1]],
            [seg1[0], seg2[1] - seg1[0]],
        ]

    if seg1[0] <= seg2[1] and seg2[1] + seg2[2] <= seg1[0] + seg1[1]:
        return [
            [seg2[0], seg2[2]],
            [seg1[0], seg2[1] - seg1[0]],
            [seg2[1] + seg2[2], seg1[0] + seg1[1] - seg2[1] - seg2[2]],
        ]

    return []


def main() -> None:
    assert get_interception([10, 15], [100, 5, 5]) == []
    assert get_interception([10, 15], [100, 25, 5]) == []
    assert get_interception([10, 15], [100, 9, 20]) == [[101, 15]]
    assert get_interception([10, 15], [100, 10, 15]) == [[100, 15]]
    assert get_interception([10, 15], [100, 8, 5]) == [[102, 3], [13, 12]]
    assert get_interception([10, 15], [100, 12, 25]) == [[100, 13], [10, 2]]
    assert get_interception([10, 15], [100, 12, 5]) == [[100, 5], [10, 2], [17, 8]]

    input_parts = sys.stdin.read().strip().split("\n\n")
    seeds = [int(n) for n in input_parts[0].split()[1:]]
    seeds = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    maps = [
        [[int(num) for num in section.split()] for section in map_.split("\n")[1:]]
        for map_ in input_parts[1:]
    ]

    for map_ in maps:
        checked = [False] * len(seeds)
        for sector in map_:
            i = 0
            while i < len(seeds):
                if not checked[i] and (intersection := get_interception(seeds[i], sector)):
                    checked[i] = True
                    seeds[i] = intersection[0]
                    seeds.extend(intersection[1:])
                    checked.extend([False] * len(intersection[1:]))

                i += 1

    print(min(seeds)[0])


if __name__ == "__main__":
    main()
