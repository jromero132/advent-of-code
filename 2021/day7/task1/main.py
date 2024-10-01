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
    return [int(x) for x in in_text.split(",")]  # get initial positions


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)

def solve(in_parsed: list) -> str:
    def ternary_search(pos, f, l, r):  # ternary search on integers
        while r - l > 1:
            mid = (l + r) // 2
            if f(mid) > f(mid + 1):
                l = mid + 1
            else:
                r = mid
        return l

    def f(p):  # ternary search function
        return sum(abs(x - p) for x in in_parsed)

    return str(f(ternary_search(in_parsed, f, min(in_parsed), max(in_parsed))))  # get final value


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
