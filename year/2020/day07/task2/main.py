"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=7 ; task=2)
"""

import sys


def main() -> None:
    graph = {}
    for bag in sys.stdin:  # parse
        bag_color, content = bag.strip().split("contain")
        bag_color = " ".join(bag_color.split(" ")[:2])

        content = content.strip(" .")
        inner_bags_description = content.split(", ")
        inner_bags = []
        for inner_bag_description in inner_bags_description:
            cnt, inner_bag = inner_bag_description.rsplit(" ", 1)[0].split(" ", 1)
            if inner_bag != "other":
                inner_bags.append((inner_bag, int(cnt)))

        graph[bag_color] = inner_bags

    memo = {}

    def get_sum_of_bags(bag: str) -> int:
        # Get the total amount of bags inside a bag.
        if bag not in memo:
            memo[bag] = sum((get_sum_of_bags(inner_bag) + 1) * cnt for inner_bag, cnt in graph[bag])
        return memo[bag]

    print(get_sum_of_bags("shiny gold"))


if __name__ == "__main__":
    main()
