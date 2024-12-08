"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=7 ; task=1)
"""

import sys


def main() -> None:
    graph = {}
    for bag in sys.stdin:  # parse
        bag_color, content = bag.strip().split("contain")
        bag_color = " ".join(bag_color.split(" ")[:2])

        content = content.strip(" .")
        inner_bags = content.split(", ")
        inner_bags: list[str] = [
            inner_bag_color
            for inner_bag in inner_bags
            if (inner_bag_color := " ".join(inner_bag.split(" ")[1:3])) != "other bags"
        ]

        graph[bag_color] = inner_bags

    memo = {}

    def is_bag_valid(bag: str) -> int:
        # Check if any of the inner bags is either a 'shiny gold' or can carry a 'shiny gold' bag.
        if bag not in memo:
            memo[bag] = any(
                inner_bag == "shiny gold" or is_bag_valid(inner_bag) for inner_bag in graph[bag]
            )
        return memo[bag]

    print(sum(is_bag_valid(bag) for bag in graph))


if __name__ == "__main__":
    main()
