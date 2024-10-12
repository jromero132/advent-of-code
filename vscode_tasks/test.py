"""Module for configuring and executing tests for Advent of Code tasks.

This module is responsible for setting up the necessary parameters to run tests on specific Advent
of Code solutions. It extracts relevant information from the file path and initiates the testing
process, ensuring that solutions are validated against expected outcomes.
"""

import sys
from collections import namedtuple
from pathlib import Path

# It seems that Path() is the root of the workspace directory. In this case `advent-of-code`.
sys.path.append(str(Path().absolute()))
from main import test


def main():
    """Initialize and run tests for a specific Advent of Code task.

    This function extracts the year, day, and task number from the provided file path and sets up a
    test configuration. It then invokes the testing process using the constructed configuration,
    allowing for the validation of the solution for the specified task.
    """
    aoc_py_file_parts = Path(sys.argv[1]).parts
    task = int(aoc_py_file_parts[-2][-1])
    day = int(aoc_py_file_parts[-3][3:])
    year = int(aoc_py_file_parts[-4])

    TestConfig = namedtuple(
        "TestConfig", ("year", "day", "task", "continue_on_failure", "answer", "submit")
    )
    test_config = TestConfig(
        year=year,
        day=day,
        task=task,
        continue_on_failure=False,
        answer=True,
        submit=True,
    )

    test(test_config)


if __name__ == "__main__":
    main()
