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
    return in_text.split("\n\n")  # get pair of packets


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    def compare(p1, p2):  # -1 if p1 is less than p2, 1 if it is greater and 0 if they are equals
        i, j = 0, 0
        while i < len(p1) and j < len(p2):
            if isinstance(p1[i], int) and isinstance(p2[j], int):
                if p1[i] != p2[j]:
                    return -1 if p1[i] < p2[j] else 1

            elif isinstance(p1[i], list) and isinstance(p2[j], list):
                if (result := compare(p1[i], p2[j])) != 0:
                    return result

            else:
                l1 = p1[i] if isinstance(p1[i], list) else [p1[i]]
                l2 = p2[j] if isinstance(p2[j], list) else [p2[j]]
                if (result := compare(l1, l2)) != 0:
                    return result

            i += 1
            j += 1

        return 0 if i == len(p1) and j == len(p2) else (-1 if i == len(p1) else 1)

    packages = [[eval(x) for x in pair.split("\n")] for pair in in_parsed]
    return str(sum(i for i, pair in enumerate(packages, 1) if compare(pair[0], pair[1]) == -1))  # final answer


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
