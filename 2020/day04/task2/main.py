import re

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
    return in_text.split("\n\n")  # get the passports


def write_output(out_file: Path, output: str):
    with open(out_file, "w") as f:
        return f.write(output)


def solve(in_parsed) -> str:
    required_keys = {  # required keys and validations
        "byr": lambda s: "1920" <= s <= "2002",
        "iyr": lambda s: "2010" <= s <= "2020",
        "eyr": lambda s: "2020" <= s <= "2030",
        "hgt": lambda s: (s[-2:] == "cm" and "150" <= s[:-2] <= "193") or (s[-2:] == "in" and "59" <= s[:-2] <= "76"),
        "hcl": lambda s: re.fullmatch(r"#[0-9a-f]{6}", s),
        "ecl": lambda s: s in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda s: len(s) == 9 and s.isdigit()
      }
    n = len(required_keys)
    valids = 0
    for passport in in_parsed:
        keys = set()
        for line in passport.split("\n"):
            for entry in line.split(" "):
                key, value = entry.split(":")
                if key in required_keys and required_keys[key](value):  # check if this is a valid key
                    keys.add(key)

        valids += len(keys) == n  # check if the passport is valid
    return str(valids)  # final answer


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