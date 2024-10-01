from pathlib import Path


TESTS_FOLDER = "tests"
EXAMPLE_TEST_CASES = 5
RUN_EXAMPLES = False
MAIN_TEST_CASES = 1
RUN_MAIN = True
LOG = True


def log(msg):
    print(msg, end="")


def read_input(in_file: Path) -> str:
    with open(in_file, "r") as f:
        return f.read()


def parse_input(in_text: str) -> list:
    return [int(x) for x in in_text.split(",")]  # get the input


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(memory) -> str:
    memory[1], memory[2] = 12, 2
    i = 0
    while i < len(memory):
        match memory[i]:
            case 1:
                memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]

            case 2:
                memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]

            case 99:
                break

        i += 4
    return str(memory[0])


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
    if RUN_EXAMPLES:
        run_cases(tests_folder, tests_id[:EXAMPLE_TEST_CASES])

    # Run main test cases
    if RUN_MAIN:
        run_cases(tests_folder, tests_id[EXAMPLE_TEST_CASES:])


if __name__ == "__main__":
    main()
