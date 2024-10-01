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
    return in_text.split("\n")  # get instructions


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    def dist(p1, p2):  # get the distance between two points
        return max(abs(x - y) for x, y in zip(p1, p2))

    def add(p1, p2):  # add two points
        return tuple(x + y for x, y in zip(p1, p2))

    def sign(x):  # get the sign of a number
        return 1 if x > 0 else (0 if x == 0 else -1)

    dir_move = {  # directions to move
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }

    knots = [(0, 0) for _ in range(2)]  # knots to be tracked

    pos = set(knots[:1])
    for instruction in in_parsed:
        d, c = instruction.split()
        d = dir_move[d]  # direction to move
        c = int(c)       # amount of steps to move

        for _ in range(1, c + 1):
            knots[0] = add(knots[0], d)  # update head

            for i, j in zip(range(0, len(knots) - 1), range(1, len(knots))):  # update tail
                ht_dist = dist(knots[i], knots[j])
                if ht_dist == 2:
                    knots[j] = add(knots[j], (sign(knots[i][0] - knots[j][0]), sign(knots[i][1] - knots[j][1])))

            pos.add(knots[-1])  # update position of tail

    return str(len(pos))  # final answer


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
