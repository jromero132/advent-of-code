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
        inner_bags = content.split(", ")
        inner_bags = [
            inner_bag_color
            for inner_bag in inner_bags
            if (inner_bag_color := " ".join(inner_bag.split(" ")[1:3])) != "other bags"
        ]

        graph[bag_color] = inner_bags

    memo = {}
    def is_bag_valid(bag):  # check if any of the inner bags is either a 'shiny gold' or can carry a 'shiny gold' bag
        if bag not in memo:
            memo[bag] = any(inner_bag == "shiny gold" or is_bag_valid(inner_bag) for inner_bag in graph[bag])
        return memo[bag]

    ans = 0
    for bag in graph:
        ans += is_bag_valid(bag)

    return str(ans)  # final answer


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
