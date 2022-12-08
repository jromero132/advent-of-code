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
    return in_text.split("\n")  # get the grid


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    n, m = len(in_parsed) - 1, len(in_parsed[0]) - 1
    dp1 = [[0] * len(in_parsed[0]) for _ in range(len(in_parsed))]  # how many trees to the left can tree [i][j] see
    dp2 = [[0] * len(in_parsed[0]) for _ in range(len(in_parsed))]  # how many trees to the right can tree [i][j] see
    dp3 = [[0] * len(in_parsed[0]) for _ in range(len(in_parsed))]  # how many trees to the bottom can tree [i][j] see
    dp4 = [[0] * len(in_parsed[0]) for _ in range(len(in_parsed))]  # how many trees to the top can tree [i][j] see

    for i in range(1, n):  # run for rows
        stack1, stack2 = [0], [n]
        for j, k in zip(range(1, m), range(m - 1, 0, -1)):
            while len(stack1) > 0 and in_parsed[i][stack1[-1]] < in_parsed[i][j]:  # run from left to right
                stack1.pop()

            while len(stack2) > 0 and in_parsed[i][stack2[-1]] < in_parsed[i][k]:  # run from right to left
                stack2.pop()

            dp1[i][j] = j if len(stack1) == 0 else j - stack1[-1]
            dp2[i][k] = m - k if len(stack2) == 0 else stack2[-1] - k

            stack1.append(j)
            stack2.append(k)

    for i in range(1, m):  # run for columns
        stack1, stack2 = [0], [m]
        for j, k in zip(range(1, n), range(n - 1, 0, -1)):
            while len(stack1) > 0 and in_parsed[stack1[-1]][i] < in_parsed[j][i]:  # run from top to bottom
                stack1.pop()

            while len(stack2) > 0 and in_parsed[stack2[-1]][i] < in_parsed[k][i]:  # run from bottom to top
                stack2.pop()

            dp3[j][i] = j if len(stack1) == 0 else j - stack1[-1]
            dp4[k][i] = n - k if len(stack2) == 0 else stack2[-1] - k

            stack1.append(j)
            stack2.append(k)

    ans = max(dp1[i][j] * dp2[i][j] * dp3[i][j] * dp4[i][j] for i in range(len(dp1)) for j in range(len(dp1[0])))
    return str(ans)


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
