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
    return [[int(x) for x in line] for line in in_text.split("\n")]  # get the information


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)

def solve(in_parsed: list) -> str:
    dir_move = [  # directions to move
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    n, m = len(in_parsed), len(in_parsed[0])
    checked = [[False] * m for _ in range(n)]

    def is_low_point(r, c):
        ans = True
        for dr, dc in dir_move:
            nr, nc = r + dr, c + dc
            ans &= nr < 0 or nr >= n or nc < 0 or nc >= m or in_parsed[r][c] < in_parsed[nr][nc]
        return ans

    def get_basins_size(r, c):
        checked[r][c] = True
        queue = [(r, c)]
        i = 0
        while i < len(queue):
            r, c = queue[i]
            for dr, dc in dir_move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not checked[nr][nc] and in_parsed[nr][nc] != 9:
                    checked[nr][nc] = True
                    queue.append((nr, nc))
            i += 1
        return len(queue)

    basins = []
    for i in range(len(in_parsed)):
        for j in range(len(in_parsed[0])):
            if not checked[i][j] and is_low_point(i, j):
                basins.append(get_basins_size(i, j))

    basins = sorted(basins, reverse=True)
    return str(basins[0] * basins[1] * basins[2])


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
