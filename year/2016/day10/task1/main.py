"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=10 ; task=1)
"""

import sys
from collections import defaultdict


def main() -> None:
    bots, outputs, instructions, queue = defaultdict(list), {}, {}, []
    for line in sys.stdin:
        lp = line.split()  # lp: line_parts
        if lp[0] == "value":
            bot = int(lp[-1])
            bots[bot].append(int(lp[1]))
            if len(bots[bot]) == 2:
                bots[bot].sort()
                queue.append(bot)

        else:
            instructions[int(lp[1])] = ((lp[5], int(lp[6])), (lp[10], int(lp[11])))

    target = [2, 3] if len(bots) == 2 else [17, 61]
    i = 0
    while i < len(queue):
        bot = queue[i]
        if bots[bot] == target:
            print(bot)
            break

        for val, (dest, num) in zip(bots[bot], instructions[bot]):
            if dest == "bot":
                bots[num].append(val)
                if len(bots[num]) == 2:
                    bots[num].sort()
                    queue.append(num)

            else:
                outputs[num] = val

        bots[bot] = []
        i += 1


if __name__ == "__main__":
    main()
