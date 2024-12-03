"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=4 ; task=1)
"""

import sys
from collections import defaultdict


def parse(line: str) -> tuple[tuple[int, int, int, int, int], str]:
    """
    Parse a log line into a structured format.

    This function extracts date and time components from a log line and returns them as a tuple,
    along with the remaining text. It is designed to facilitate the processing of log entries by
    breaking them down into manageable parts.

    Args:
        line (str): The log line to be parsed.

    Returns:
        tuple[tuple[int, int, int, int, int], str]: A tuple containing a tuple of integers
            representing the year, month, day, hour, and minute, and a string with the remaining
            text from the log line.

    """
    return (
        (int(line[1:5]), int(line[6:8]), int(line[9:11]), int(line[12:14]), int(line[15:17])),
        line[19:].strip(),
    )


def main() -> None:
    records = sorted((parse(line) for line in sys.stdin), key=lambda v: v[0])
    guard_id, asleep = None, None
    data = defaultdict(lambda: [0] * 61)
    for timestamp, message in records:
        if message.startswith("Guard"):
            guard_id = int(message.split()[1][1:])

        elif message.startswith("falls"):
            asleep = timestamp[4]

        elif guard_id is not None and asleep is not None:
            registry = data[guard_id]
            registry[-1] += timestamp[4] - asleep
            for i in range(asleep, timestamp[4]):
                registry[i] += 1

            asleep = None

    sleeping_time, minute = 0, 0
    for _id, registry in data.items():
        if registry[-1] > sleeping_time:
            guard_id = _id
            sleeping_time = registry[-1]
            for i in range(1, 60):
                if registry[i] > registry[minute]:
                    minute = i

    print(guard_id * minute)


if __name__ == "__main__":
    main()
