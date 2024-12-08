"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=8 ; task=2)
"""

import sys


def main() -> None:
    # a -> len(2), len(3)
    # b -> (after f) -> len(4)
    # c -> len(6) each other -> len(2)
    # d -> (remaining after c) -> len(4)
    # e -> (remaining after d)
    # f -> (after e) -> len(3)
    # g -> remaining
    ans = 0
    for info in sys.stdin:
        segments_c = [None] * 7
        signal_patterns, output = info.strip().split(" | ")
        signal_patterns = sorted((set(s) for s in signal_patterns.split()), key=lambda s: len(s))

        # find top segment - difference between 1 and 7
        c = next(iter(signal_patterns[1] - signal_patterns[0]))
        segments_c[0] = c
        segments_n = {c: 0}
        # get differences of len 6 digits
        dif = set()
        for i in range(6, 9):
            for j in range(i + 1, 9):
                dif.update(signal_patterns[i].symmetric_difference(signal_patterns[j]))

        # find top-right segment - intersection of the difference between len 6 digits and 1
        c = next(iter(dif.intersection(signal_patterns[0])))
        segments_c[2] = c
        segments_n[c] = 2

        # find middle segment - intersection between remaining difference and 4
        dif.remove(c)
        c = next(iter(dif.intersection(signal_patterns[2])))
        segments_c[3] = c
        segments_n[c] = 3

        # find bottom-left segment - remaining difference
        dif.remove(c)
        c = next(iter(dif))
        segments_c[4] = c
        segments_n[c] = 4

        # find bottom-right segment - all segments of 7 where discovered already except 1
        c = next(iter(signal_patterns[1].difference(segments_n.keys())))
        segments_c[5] = c
        segments_n[c] = 5

        # find top-left segment - all segments of 4 where discovered already except 1
        c = next(iter(signal_patterns[2].difference(segments_n.keys())))
        segments_c[1] = c
        segments_n[c] = 1

        # find bottom segment - all segments where discovered already except 1
        c = next(iter(signal_patterns[-1].difference(segments_n.keys())))
        segments_c[6] = c
        segments_n[c] = 6

        nums = [
            "".join(sorted(segments_c[:3] + segments_c[4:])),  # 0
            "".join(sorted(segments_c[2] + segments_c[5])),  # 1
            "".join(sorted(segments_c[2:5] + [segments_c[0], segments_c[6]])),  # 2
            "".join(sorted(segments_c[2:4] + segments_c[5:] + [segments_c[0]])),  # 3
            "".join(sorted(segments_c[1:4] + [segments_c[5]])),  # 4
            "".join(sorted(segments_c[:2] + segments_c[5:] + [segments_c[3]])),  # 5
            "".join(sorted(segments_c[:2] + segments_c[3:])),  # 6
            "".join(sorted(segments_c[0] + segments_c[2] + segments_c[5])),  # 7
            "".join(sorted(segments_c)),  # 8
            "".join(sorted(segments_c[:4] + segments_c[5:])),  # 9
        ]

        val = 0
        for o in output.split():  # convert the output to a number
            val = val * 10 + nums.index("".join(sorted(o)))

        ans += val  # update the answer

    print(ans)


if __name__ == "__main__":
    main()
