from pathlib import Path


TESTS_FOLDER = "tests"
EXAMPLE_TEST_CASES = 1
MAIN_TEST_CASES = 1
LOG = True


def log(msg):
    print(msg, end="")


def read_input(in_file: Path) -> str:
    with open(in_file, "r") as f:
        return f.read()


def parse_input(in_text: str) -> list:
    return in_text.split("\n")  # get bags


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed) -> str:
    graph = {}
    for bag in in_parsed:  # parse
        bag_color, content = bag.split("contain")
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
    def get_sum_of_bags(bag):  # get the total amount of bags inside a bag
        if bag not in memo:
            memo[bag] = sum((get_sum_of_bags(inner_bag) + 1) * cnt for inner_bag, cnt in graph[bag])
        return memo[bag]

    return str(get_sum_of_bags("shiny gold"))  # final answer


def run_case(in_file: Path, out_file: Path):
    in_text = read_input(in_file)
    in_parsed = parse_input(in_text)
    output = solve(in_parsed)
    write_output(out_file, output)
    return output


def run_cases(tests_folder: Path, tests_id: list):
    for test_id in tests_id:
        in_file = tests_folder / f"{test_id}.in"
        out_file = tests_folder / f"{test_id}.out"

        if LOG:
            log(f"Test case {test_id}... ")

        output = run_case(in_file, out_file)

        if LOG:
            log(f"{output}\n")


def main():
    tests_folder = Path(__file__).parent / TESTS_FOLDER
    tests_id = [f"{i:02}" for i in range(1, EXAMPLE_TEST_CASES + MAIN_TEST_CASES + 1)]

    # Run examples test cases
    run_cases(tests_folder, tests_id[:EXAMPLE_TEST_CASES])

    # Run main test cases
    run_cases(tests_folder, tests_id[EXAMPLE_TEST_CASES:])


if __name__ == "__main__":
    main()
