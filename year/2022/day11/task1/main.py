"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=11 ; task=1)
"""

import re
import sys
from dataclasses import dataclass


@dataclass
class Monkey:
    """
    Represents a monkey in a simulation with specific attributes and behaviors.

    This class models a monkey that holds a list of items and performs operations based on defined rules. It includes
    attributes for the monkey's index, operation, division criteria, and the results of its actions, as well as a
    counter for the number of items inspected.

    Args:
        idx (int): The unique identifier for the monkey.
        items (list): A list of items held by the monkey.
        op (str): The operation that the monkey performs on its items.
        div (int): The divisor used for determining the outcome of the operation.
        result_true (int): The index of the monkey to which the result is sent if the condition is true.
        result_false (int): The index of the monkey to which the result is sent if the condition is false.
        items_inspected (int, optional): The count of items inspected by the monkey. Defaults to 0.

    """

    idx: int
    items: list
    op: str
    div: int
    result_true: int
    result_false: int
    items_inspected: int = 0


def main() -> None:
    pattern = (
        r"Monkey (\d+):\n  Starting items: (.*)\n  Operation: new = (.*)\n  Test: divisible by (\d+)\n"
        r"    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"
    )

    monkeys_data = sys.stdin.read().split("\n\n")
    monkeys = []
    for monkey_data in monkeys_data:
        d = re.match(pattern, monkey_data).groups()
        monkeys.append(
            Monkey(
                int(d[0]),
                [int(x) for x in d[1].split(", ")],
                d[2],
                int(d[3]),
                int(d[4]),
                int(d[5]),
            ),
        )

    for _ in range(20):
        for monkey in monkeys:
            monkey.items_inspected += len(monkey.items)  # update items processed
            items, monkey.items = [eval(monkey.op) // 3 for old in monkey.items], []
            for item in items:
                monkeys[
                    monkey.result_true if item % monkey.div == 0 else monkey.result_false
                ].items.append(item)

    most_active = sorted((monkey.items_inspected for monkey in monkeys), reverse=True)
    print(most_active[0] * most_active[1])  # final answer


if __name__ == "__main__":
    main()
