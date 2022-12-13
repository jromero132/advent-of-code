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
    return in_text.split("\n\n")  # get numbers and boards


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    nums_to_call = in_parsed[0].split(',')  # get bingo numbers to call
    boards = [[line.split() for line in board.split('\n')] for board in in_parsed[1:]]  # get bingo boards

    def check_win(board):  # check if any (row, column) has all its cells marked
        return any(
            all(board[i][j].startswith('-') for j in range(len(board)))
            or all(board[j][i].startswith('-') for j in range(len(board)))
            for i in range(len(board))
        )

    def get_sum(board):  # get the sum of unchecked cells in a board
        return sum(int(x) for row in board for x in row if not x.startswith('-'))

    def mark(board, num):  # mark a cell in a board if exists
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == num:
                    board[i][j] = f"-{num}"
                    if check_win(board):
                        return get_sum(board) * int(num)  # get the actual final value
        return -1

    for num in nums_to_call:  # call every number
        idx = 0
        while idx < len(boards):  # mark it in every board
            if (ans := mark(boards[idx], num)) != -1:
                if len(boards) == 1:
                    return str(ans)  # get final value

                else:
                    del boards[idx]  # remove this board of the game because it already won
                    idx -= 1
            idx += 1


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
