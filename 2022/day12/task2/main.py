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
    return in_text.split("\n")  # get grid


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    rs, cs = -1, -1
    re, ce = -1, -1
    n, m = len(in_parsed), len(in_parsed[0])
    q = []
    for i in range(n):
        for j in range(m):
            match in_parsed[i][j]:
                case 'S':  # one of the possible starting points
                    rs, cs = i, j
                    q.append((i, j))

                case 'E':  # ending point
                    re, ce = i, j

                case 'a':  # other possible starting points
                    q.append((i, j))

    in_parsed[rs] = in_parsed[rs].replace('S', 'a')
    in_parsed[re] = in_parsed[re].replace('E', 'z')

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    steps = [[-1] * m for _ in range(n)]
    for i, j in q:
        steps[i][j] = 0  # it costs 0 to start at any of these points

    i = 0
    while i < len(q) and q[i] != (re, ce):  # BFS
        rs, cs = q[i]
        for mr, mc in moves:
            nr, nc = rs + mr, cs + mc
            if 0 <= nr < n and 0 <= nc < m \
            and steps[nr][nc] == -1 and ord(in_parsed[rs][cs]) + 1 >= ord(in_parsed[nr][nc]):
                steps[nr][nc] = steps[rs][cs] + 1
                q.append((nr, nc))
        i += 1

    return str(steps[re][ce])  # final answer


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
