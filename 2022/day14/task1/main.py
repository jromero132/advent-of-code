from collections import defaultdict
from pathlib import Path
from sortedcontainers import SortedDict


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
    return in_text.split("\n")  # get paths


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    paths = [
        [
            [
                int(x) for x in point.split(',')
            ]
            for point in path.split(" -> ")
        ]
        for path in in_parsed
    ]

    sand_x, sand_y = 500, 0
    grid = defaultdict(SortedDict)

    def set_rocks(p1, p2):
        if p1[0] == p2[0]:
            for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                grid[p1[0]][i] = -1

        else:
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                grid[i][p1[1]] = -1

    for path in paths:
        for i in range(1, len(path)):
            set_rocks(path[i - 1], path[i])

    def fall(x, y):  # fall as much as possible from column x and row y
        d = grid[x]
        if y in d:
            return None

        idx = d.bisect_left(y)
        return None if len(d) == idx else (x, d.peekitem(idx)[0] - 1)

    while True:
        p = fall(sand_x, sand_y)
        while p is not None:  # continuously drop the sand
            if p[1] + 1 not in grid[p[0] - 1]:
                p = fall(p[0] - 1, p[1] + 1)

            elif p[1] + 1 not in grid[p[0] + 1]:
                p = fall(p[0] + 1, p[1] + 1)

            else:
                break

        if p is None:
            break

        grid[p[0]][p[1]] = 1
        if p == (sand_x, sand_y):
            break

    return str(sum(list(col.values()).count(1) for col in grid.values()))  # final answer


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
