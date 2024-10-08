"""Module for executing and validating Advent of Code solutions.

This module facilitates the testing of Python solutions for Advent of Code challenges by running
them against predefined input files. It captures the output, compares it with expected results, and
presents the outcomes in a formatted manner for easy review.
"""

import subprocess
import sys
from pathlib import Path

LINE_SIZE = 25


def print_box(msg: str, size: int):
    """Print a message inside a decorative box.

    This function takes a message and a specified size, then formats and prints the message within a
    box made of special characters. It ensures that the message is centered and visually appealing,
    making it suitable for console output.

    Args:
        msg (str): The message to be printed inside the box.
        size (int): The width of the box, which determines how the message is centered.
    """
    print(f"╔{'═' * size}╗")
    for line in msg.split("\n"):
        print(f"║{line.center(size)}║")
    print(f"╚{'═' * size}╝")


def get_code_output(sol_file: Path, inp: Path) -> bytes:
    """Execute a Python solution file with input from a specified file.

    This function runs a Python script located at `sol_file`, using the contents of `inp` as its
    standard input. It captures and returns the output of the script as bytes, allowing for further
    processing or analysis.

    Args:
        sol_file (Path): The path to the Python solution file to be executed.
        inp (Path): The path to the input file that provides standard input to the solution.

    Returns:
        bytes: The output produced by the executed script.
    """
    with open(inp, encoding="utf-8") as in_file:
        return subprocess.check_output(["python", str(sol_file)], stdin=in_file).strip()


def main():
    """Run the Advent of Code solution tests and display results.

    This function retrieves the specified Python solution file and iterates through its
    corresponding input test files. It executes the solution for each input, compares the output
    with the expected result, and prints the outcome in a formatted manner.
    """
    aoc_py_file = Path(sys.argv[1])
    for inp in sorted(f for f in (aoc_py_file.parent / "tests").iterdir() if f.suffix == ".in"):
        print_box(f"> {inp.name} <", LINE_SIZE)

        ans = get_code_output(aoc_py_file, inp).decode("utf-8")
        print(ans)
        with open(inp.with_suffix(".out")) as out_file:
            sol = out_file.readline().strip()
        result = "OK" if ans.split("\n")[-1] == sol else f"FAIL\nExpected: {sol}"

        print_box(f"{inp.name} => {result}", LINE_SIZE)


if __name__ == "__main__":
    main()
