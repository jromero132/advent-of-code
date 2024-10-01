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
    return [
        [
            [
                int(x) for x in vent.split(',')
            ] for vent in line.split(" -> ")  # get the values as int
        ] for line in in_text.split("\n")  # get vents
    ]  # get lines of vents


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    def compress():  # move the field to be from [0, N] x [0, M]
        mins = [x for x in in_parsed[0][0]]
        maxs = [x for x in in_parsed[0][0]]

        for line in in_parsed:  # get minimum and maximum values
            for vent in line:
                for i in range(len(vent)):
                    mins[i] = min(mins[i], vent[i])
                    maxs[i] = max(maxs[i], vent[i])

        for i in range(len(in_parsed)):  # update cells based on the minimum values
            for j in range(len(in_parsed[i])):
                for k in range(len(mins)):
                    in_parsed[i][j][k] -= mins[k]

        return [ma - mi + 1 for ma, mi in zip(maxs, mins)]

    def generate(v1, v2):  # generate points between two vents
        sign = [1 if v1[i] <= v2[i] else -1 for i in range(len(v1))]
        yield v1
        while v1 != v2:
            for i in range(len(v1)):
                if v1[i] != v2[i]:
                    v1[i] += sign[i]
            yield v1

    n, m = compress()
    field = [[0] * m for _ in range(n)]

    for v1, v2 in in_parsed:
        for i, j in generate(v1, v2):
            field[i][j] += 1

    return str(sum(cell >= 2 for row in field for cell in row))  # get final result


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
