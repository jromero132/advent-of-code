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
    return in_text.split("\n\n")  # get the initial state and moves


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    starting_stacks = in_parsed[0].split('\n')
    size = len([x for x in starting_stacks[-1].split() if x != ''])  # get how many crates are there
    crates = [[] for _ in range(size)]  # stacks

    for line in reversed(starting_stacks[:-1]):  # parsing the initial state
        for i in range(0, len(line) // 4 + 1):
            char = line[i * 4 + 1]
            if char != ' ':
                crates[i].append(char)

    for line in in_parsed[1].split('\n'):  # making moves
        line_splitted = line.split()
        cnt = int(line_splitted[1])
        from_ = int(line_splitted[3]) - 1
        to = int(line_splitted[5]) - 1

        for _ in range(cnt):  # move 'cnt' crates from stack 'from_' to stack 'to'
            crates[to].append(crates[from_].pop())

    return "".join('' if len(crates[i]) == 0 else crates[i].pop() for i in range(len(crates)))  # get final state


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
