from pathlib import Path


TESTS_FOLDER = "tests"
EXAMPLE_TEST_CASES = 2
MAIN_TEST_CASES = 1
LOG = True


def log(msg):
    print(msg, end="")


def read_input(in_file: Path) -> str:
    with open(in_file, "r") as f:
        return f.read()


def parse_input(in_text: str) -> list:
    return [line.split() for line in in_text.split("\n")]  # get instructions


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    cycles = {  # amount of cycles for each command
        "noop": 1,
        "addx": 2
    }

    n, m = 6, 40  # crt dimensions (rows and columns)
    crt = [""] * n
    i, j = 0, 0

    x = 1
    for cmd in in_parsed:
        for _ in range(cycles[cmd[0]]):
            crt[i] += '#' if x - 1 <= j <= x + 1 else ' '
            j += 1
            if j == m:
                j = 0
                i += 1

        if cmd[0] == "addx":
            x += int(cmd[1])

    return "\n".join(crt)  # final answer - PLULKBZH


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
