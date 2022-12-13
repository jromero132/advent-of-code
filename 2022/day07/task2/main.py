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
    return in_text.split("\n")  # get commands


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed: list) -> str:
    class Dir:  # dir class helper
        def __init__(self, name: str, parent = None) -> None:
            self.name = name
            self.parent = parent
            self.subdirs = {}
            self.files = []
            self.size = None

    dir_tree = Dir("/")  # root dir
    cwd = dir_tree
    for cmd in in_parsed:
        cmd = cmd.split()
        match cmd[0]:
            case "$":
                if cmd[1] == "cd":
                    match cmd[2]:
                        case "/":  # go to root directory
                            cwd = dir_tree

                        case "..":  # go to parent directory
                            cwd = cwd.parent

                        case _:  # go to subdirectory
                            cwd = cwd.subdirs[cmd[2]]

            case "dir":  # current directory has a 'cmd[2]' subdirectory
                cwd.subdirs[cmd[1]] = Dir(cmd[1], cwd)

            case _:  # current directory has a 'cmd[1]' file with 'cmd[0]' size
                cwd.files.append((cmd[1], int(cmd[0])))

    def update_size(cwd):  # update directory size
        cwd.size = 0
        for d in cwd.subdirs.values():
            update_size(d)  # recursively work on subdirectories
            cwd.size += d.size

        for _, fs in cwd.files:  # work on files
            cwd.size += fs

    # get the directory with the smallest size such that after delete it,
    # 0the amount of free space is greater than the required space
    def get_directory_to_delete(cwd, free_space, required_space):
        ans = cwd
        for d in cwd.subdirs.values():
            if free_space + d.size >= required_space:
                sub_ans = get_directory_to_delete(d, free_space, required_space)
                if ans.size > sub_ans.size:
                    ans = sub_ans
        return ans

    update_size(dir_tree)  # update directory sizes
    folder = get_directory_to_delete(dir_tree, 70000000 - dir_tree.size, 30000000)  # get the folder to be deleted
    return str(folder.size)  # get the size of the folder to be deleted


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
