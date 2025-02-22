"""
Main module for the Advent of Code project.

This module provides a command-line interface for managing and testing solutions to Advent of Code
challenges. It includes functionality for creating tasks, running tests, submit answers and parsing
command-line arguments to facilitate user interaction with the project.

The module defines various subcommands, each associated with specific actions, and utilizes argument
parsing to handle user inputs effectively.
"""

from __future__ import annotations

import argparse
import datetime
import inspect
import os
import subprocess
import sys
from http import HTTPStatus
from pathlib import Path

import bs4
import pyperclip
import requests
from dotenv import load_dotenv

DAY_PATH = "year/{year}/day{day:02}"
TASK_PATH = DAY_PATH + "/task{task}"
TESTS_PATH = f"{TASK_PATH}/tests"
REQUESTS_TIMEOUT = 5  # 5 seconds

LANG_EXTENSION = {
    "py": "py",
    "python": "py",
    "cpp": "cpp",
    "c++": "cpp",
}

load_dotenv()


def font_color(txt: str, color: str) -> str:
    """
    Format the given text with the specified color.

    This function takes a string and a color code, returning the text wrapped in the color code for
    terminal output. The formatting is reset after the text to ensure subsequent text is not
    affected.

    Args:
        txt (str): The text to be formatted.
        color (str): The color code to apply to the text.

    Returns:
        str: The formatted text with the specified color.

    """
    return f"{color}{txt}\033[0m"


def font_color_green(txt: str) -> str:
    """
    Format the given text in green color.

    This function wraps the provided text in a green color code for terminal output, allowing the
    text to be displayed in green. It utilizes the `font_color` function to apply the formatting.

    Args:
        txt (str): The text to be formatted in green.

    Returns:
        str: The formatted text in green color.

    """
    return font_color(txt, "\033[92m")


def font_color_red(txt: str) -> str:
    """
    Format the given text in red color.

    This function wraps the provided text in a red color code for terminal output, allowing the text
    to be displayed in red. It utilizes the `font_color` function to apply the formatting.

    Args:
        txt (str): The text to be formatted in red.

    Returns:
        str: The formatted text in red color.

    """
    return font_color(txt, "\033[91m")


def font_color_orange(txt: str) -> str:
    """
    Format the given text in orange color.

    This function wraps the provided text in an orange color code for terminal output, allowing the
    text to be displayed in orange. It utilizes the `font_color` function to apply the formatting.

    Args:
        txt (str): The text to be formatted in orange.

    Returns:
        str: The formatted text in orange color.

    """
    return font_color(txt, "\033[93m")


def font_color_blue(txt: str) -> str:
    """
    Format the given text in blue color.

    This function wraps the provided text in a blue color code for terminal output, allowing the
    text to be displayed in blue. It utilizes the `font_color` function to apply the formatting.

    Args:
        txt (str): The text to be formatted in blue.

    Returns:
        str: The formatted text in blue color.

    """
    return font_color(txt, "\033[94m")


def get_url(year: int, day: int) -> str:
    """
    Construct the URL for a specific Advent of Code challenge.

    This function generates a URL based on the provided year and day parameters, allowing users to
    easily access the corresponding challenge page. The URL is formatted to point to the specific
    challenge for the given year and day.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.

    Returns:
        str: The constructed URL for the specified challenge.

    """
    return f"https://adventofcode.com/{year}/day/{day}"


def get_response(url: str, data: dict | None = None) -> requests.Response:
    """
    Fetch the HTTP response from the specified URL.

    This function sends a GET request to the provided URL using a session cookie for authentication.
    If the response status code indicates an error, it raises a ValueError with details about the
    failure.

    Args:
        url (str): The URL to send the GET request to.
        data (dict, optional): The data to send with the POST request. Defaults to an empty
            dictionary.

    Returns:
        requests.Response: The HTTP response object from the request.

    Raises:
        ValueError: If the response status code is not 200 OK.

    """
    response = (
        requests.get(
            url,
            cookies={"session": os.getenv("AOC_COOKIE", "")},
            timeout=REQUESTS_TIMEOUT,
        )
        if data is None
        else requests.post(
            url,
            cookies={"session": os.getenv("AOC_COOKIE", "")},
            data=data,
            timeout=REQUESTS_TIMEOUT,
        )
    )

    if response.status_code != HTTPStatus.OK:
        error_msg = (
            f"Querying the url {url} resulted in status code {response.status_code} with the "
            f"following text: {response.text}"
        )
        raise ValueError(error_msg)

    return response


def get_html(year: int, day: int) -> str:
    """
    Retrieve the HTML content for a specific Advent of Code challenge.

    This function constructs the URL for the given year and day, then fetches the corresponding HTML
    content by making an HTTP request. It returns the text of the response, allowing users to access
    the challenge details.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.

    Returns:
        str: The HTML content of the specified challenge page.

    """
    return get_response(get_url(year, day)).text


def get_input(year: int, day: int) -> str:
    """
    Retrieve the input data for a specific Advent of Code challenge.

    This function constructs the URL for the given year and day, then fetches the input data by
    making an HTTP request to the appropriate endpoint. It returns the text of the response,
    providing access to the challenge input.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.

    Returns:
        str: The input data for the specified challenge.

    """
    return get_response(f"{get_url(year, day)}/input").text


def submit_answer(year: int, day: int, task: int, answer: str) -> int:
    """
    Submit an answer for a specific task of a given day in a specified year.

    This function sends the provided answer to the Advent of Code server for the specified  year,
    day, and task level, and checks if the response indicates that the answer is correct.

    Args:
        year (int): The year of the Advent of Code event.
        day (int): The day of the challenge within the specified year.
        task (int): The task level for which the answer is being submitted.
        answer (str): The answer to be submitted.

    Returns:
        int: 0 if the answer is wrong, 1 if the answer if correct and -1 if the problem was already
            solved.

    """
    response = get_response(
        f"{get_url(year, day)}/answer",
        data={"level": task, "answer": answer},
    ).text

    return (
        1
        if "That's the right answer!" in response
        else -1
        if "Both parts of this puzzle are complete!" in response
        or ("The first half of this puzzle is complete!" in response and task == 1)
        else 0
    )


# Simplification of https://github.com/dlon/html2markdown/blob/master/html2markdown.py
def convert_html_to_markdown(tag: bs4.element.Tag) -> str:
    """
    Convert an HTML tag and its children into Markdown format.

    This function processes an HTML structure, transforming specific HTML elements into their
    corresponding Markdown representations while handling footnotes. It returns the converted
    Markdown text, including any footnotes generated during the conversion.

    Args:
        tag (bs4.element.Tag): The root HTML tag to be converted to Markdown.

    Returns:
        str: The Markdown representation of the HTML content, including footnotes if present.

    Raises:
        ValueError: If an unsupported HTML tag is encountered during conversion.

    """
    root_tag = tag
    footnotes: list[str] = []

    def html_tags_to_markdown(tag: bs4.element.Tag) -> None:
        """
        Convert HTML tags to Markdown format recursively.

        This function processes an HTML tag and its children, transforming specific HTML elements
        into their Markdown equivalents. It modifies the tag in place, allowing for a structured
        representation of the content in Markdown format.

        Args:
            tag (bs4.element.Tag): The HTML tag to be converted to Markdown.

        Raises:
            ValueError: If an unsupported HTML tag is encountered.

        """
        for child in tag.find_all(recursive=False):
            html_tags_to_markdown(child)

        match tag.name:
            case "h2":
                tag.insert_before("# ")
                tag.insert_after("\n")
                tag.unwrap()

            case "p" | "br":
                tag.insert_before("\n")
                tag.unwrap()

            case "em":
                style = "**"
                tag.insert_before(style)
                tag.insert_after(style)
                tag.unwrap()

            case "s":
                tag.insert_before("~~")
                tag.insert_after("~~")
                tag.unwrap()

            case "a":
                tag.insert_before("[")
                tag.insert_after(f"]({tag['href']})")
                tag.unwrap()

            case "span":
                if tag.has_attr("title"):
                    nonlocal footnotes
                    footnotes.append(f"[^{len(footnotes) + 1}]: [{tag.text}] {tag['title']}")
                    tag.insert_after(f"[^{len(footnotes)}]")

                elif tag.has_attr("class") and "quiet" in tag["class"]:
                    tag.insert_before("*")
                    tag.insert_after("*")

                else:
                    error_msg = f"Missing condition for tag: {tag}"
                    raise ValueError(error_msg)

                tag.unwrap()

            case "ul":
                tag.contents = tag.contents[1:-1]
                tag.unwrap()

            case "li":
                tag.insert_before("    - ")
                tag.unwrap()

            case "code":
                if "\n" in tag.text:
                    tag.insert_before("```\n")
                    tag.insert_after("```")

                else:
                    tag.insert_before("`")
                    tag.insert_after("`")

                tag.unwrap()

            case "pre":
                tag.unwrap()

            case "article":
                pass

            case _:
                error_msg = f"Missing condition for tag: {tag}"
                raise ValueError(error_msg)

    html_tags_to_markdown(root_tag)
    content = root_tag.text
    if footnotes:
        content += "\n" + "\n\n".join(footnotes) + "\n"
    return content


def get_markdown(year: int, day: int) -> list[str]:
    """
    Retrieve and converts the articles of a specific Advent of Code challenge to Markdown.

    This function fetches the HTML content for the given year and day, parses it to extract the
    articles, and converts each article into Markdown format. It returns a list of Markdown strings
    representing the articles.

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.

    Returns:
        list[str]: A list of Markdown representations of the articles.

    """
    soup = bs4.BeautifulSoup(get_html(year, day), features="html.parser")
    if soup.body is None or soup.body.main is None:
        return []

    articles = soup.body.main.findAll("article", recursive=False)
    if articles is None:
        articles = []

    return [convert_html_to_markdown(article) for article in articles]


def create(args: argparse.Namespace) -> None:
    """
    Create task directories and files for a specific Advent of Code challenge.

    This function generates directories and files for each task of the specified challenge year and
    day. It reads a template file if provided, replaces placeholders with the year and day, and
    writes the Markdown descriptions and input data into the appropriate files.

    Args:
        args (argparse.Namespace): The command-line arguments containing the year, day, and optional
            template file path.

    Raises:
        FileNotFoundError: If the specified template file does not exist.

    """
    if not args.template:
        args.template = f"template.{LANG_EXTENSION[args.lang]}"

    template_content = ""
    if (template := Path(args.template)).exists():
        with template.open(encoding="utf-8") as f:
            template_content = f.read().replace("`year`", str(args.year))
            template_content = template_content.replace("`day`", str(args.day))

    mds = get_markdown(args.year, args.day)

    for i, md in enumerate(mds, start=1):
        task_dir = Path(TASK_PATH.format(year=args.year, day=args.day, task=i))
        task_dir.mkdir(parents=True, exist_ok=True)
        with Path(task_dir / "description.md").open("w", encoding="utf-8") as f:
            f.write(md)

        code_content = template_content.replace("`task`", str(i))
        if not (py_file := task_dir / f"main.{LANG_EXTENSION[args.lang]}").exists():
            with py_file.open("w", encoding="utf-8") as f:
                f.write(code_content)

        test_dir = Path(TESTS_PATH.format(year=args.year, day=args.day, task=i))
        test_dir.mkdir(parents=True, exist_ok=True)
        (test_dir / "01.in").touch()
        (test_dir / "01.out").touch()

    with Path(f"{DAY_PATH.format(year=args.year, day=args.day)}/task.in").open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write(get_input(args.year, args.day))


def create_cli(subparsers: argparse._SubParsersAction) -> None:
    """
    Set up the command-line interface for the 'create' command.

    This function configures the argument parser for the 'create' command, allowing users to
    specify the year, day, and an optional template file when deploying the project. It ensures
    that the necessary arguments are available for the command's execution.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers action object to which the 'create'
            command parser will be added.

    """
    parser: argparse.ArgumentParser = subparsers.add_parser(
        "create",
        help="Create a new Advent of Code challenge setup.",
    )
    parser.add_argument(
        "-l",
        "--lang",
        "--language",
        type=str,
        default="py",
        help="The language of the solution you want to test. Defaults to python.",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=datetime.datetime.now(tz=datetime.timezone.utc).year,
        help="The year of the Advent of Code challenge (e.g., 2024). Defaults to the current year.",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="The day of the Advent of Code challenge (e.g., 13). This option is required.",
    )
    parser.add_argument(
        "-t",
        "--template",
        default=None,
        help=(
            "Specify an optional template file to use as the starting solution to the challenge. "
            "If not provided, an empty template will be used."
        ),
    )


def maketests(args: argparse.Namespace) -> None:
    """
    Create input and output test files for a specific task.

    This function generates a directory for test files based on the specified year, day, and task,
    and creates input and output files for a given number of tests. It ensures that the necessary
    files are created if they do not already exist.

    Args:
        args (argparse.Namespace): The command-line arguments containing the year, day, task, and
            number of tests to create.

    """
    tests_dir = Path(TESTS_PATH.format(year=args.year, day=args.day, task=args.task))
    tests_dir.mkdir(exist_ok=True, parents=True)

    for i in range(1, args.number + 1):
        if not (test_in := tests_dir / f"{i:02}.in").exists():
            test_in.touch()

        if not (test_out := tests_dir / f"{i:02}.out").exists():
            test_out.touch()


def maketests_cli(subparsers: argparse._SubParsersAction) -> None:
    """
    Set up the command-line interface for the 'maketests' command.

    This function configures the argument parser for the 'maketests' command, allowing users to
    specify the year, day, task, and number of test files to create. It ensures that the necessary
    arguments are available for the command's execution.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers action object to which the
            'maketests' command parser will be added.

    """
    parser: argparse.ArgumentParser = subparsers.add_parser(
        "maketests",
        help="Create test files for one Advent of Code challenge.",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=datetime.datetime.now(tz=datetime.timezone.utc).year,
        help="The year of the Advent of Code challenge (e.g., 2024). Defaults to the current year.",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="The day of the Advent of Code challenge (e.g., 13). This option is required.",
    )
    parser.add_argument(
        "-t",
        "--task",
        type=int,
        required=True,
        help="The task number for which to create test files. This option is required.",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        required=True,
        help="The number of test files to create. This option is required.",
    )


def test(args: argparse.Namespace) -> None:
    """
    Run tests for a specific Advent of Code task and compares outputs.

    This function executes a series of input tests against a solution file, comparing the actual
    output to the expected output. It reports the results of each test, indicating whether they
    passed or failed, and can optionally solve the task and submit the answer if all tests pass.

    Args:
        args (argparse.Namespace): The command-line arguments containing the year, day, task, and
            options for continuing on failure or solving the task.

    Raises:
        FileNotFoundError: If the input or output test files do not exist.
        subprocess.CalledProcessError: If the solution script fails to execute.

    """

    def get_code_output(sol_file: Path, inp: Path, lang: str) -> bytes:
        """
        Execute a Python solution file with input from a specified file.

        This function runs a Python script located at `sol_file`, using the contents of `inp` as its
        standard input. It captures and returns the output of the script as bytes, allowing for
        further processing or analysis.

        Args:
            sol_file (Path): The path to the Python solution file to be executed.
            inp (Path): The path to the input file that provides standard input to the solution.

        Returns:
            bytes: The output produced by the executed script.

        """
        if lang in {"py", "python"}:
            with inp.open(encoding="utf-8") as in_file:
                return subprocess.check_output(["python", str(sol_file)], stdin=in_file).rstrip()

        if lang in {"cpp", "c++"}:
            executable = sol_file.with_suffix(".exe")
            subprocess.call(
                ["g++", "-Wl,-z,stack-size=268435456", "-O2", str(sol_file), "-o", str(executable)],
            )
            with inp.open(encoding="utf-8") as in_file:
                process = subprocess.check_output(
                    [str(executable), str(sol_file)],
                    stdin=in_file,
                ).rstrip()
            executable.unlink()
            return process

        return b""

    def is_correct_solution(sol_file: Path, input_file: Path, output_file: Path) -> bool:
        print(f"  - {input_file.name:<8}", end=" ")
        ans = get_code_output(sol_file, input_file, args.lang)
        with output_file.open("rb") as out_file:
            sol = out_file.read().strip()

        if ans == sol:
            print(font_color_green("OK"))
            return True

        print(
            font_color_red("FAIL")
            + " ["
            + font_color_orange(f"found={ans.decode('utf-8')}")
            + " ; "
            + font_color_blue(f"expected={sol.decode('utf8')}")
            + "]",
        )
        return False

    day_dir = Path(DAY_PATH.format(year=args.year, day=args.day)).absolute()
    task_dir = Path(TASK_PATH.format(year=args.year, day=args.day, task=args.task)).absolute()
    tests_dir = Path(TESTS_PATH.format(year=args.year, day=args.day, task=args.task)).absolute()

    sol_file = task_dir / f"main.{LANG_EXTENSION[args.lang]}"

    failed_testcases = 0
    no_tests = True
    print(f"Start testing AOC y{args.year}/d{args.day}/t{args.task}...")
    if tests_dir.exists():
        for inp in sorted(f for f in tests_dir.iterdir() if f.suffix == ".in"):
            no_tests = False
            if not is_correct_solution(sol_file, inp, inp.with_suffix(".out")):
                failed_testcases += 1
                if not args.continue_on_failure:
                    break

    if failed_testcases == 0:
        if no_tests:
            print(font_color_orange("No test files found!"))

        if args.answer or args.submit:
            ans_decoded = get_code_output(sol_file, day_dir / "task.in", args.lang).decode("utf-8")
            with Path(day_dir / f"task{args.task}.out").open("w", encoding="utf-8") as f:
                f.write(ans_decoded)
                f.write("\n")

            print(f"Answer:{'\n' if '\n' in ans_decoded else ' '}{font_color_blue(ans_decoded)}")
            pyperclip.copy(ans_decoded)

            if args.submit:
                match submit_answer(args.year, args.day, args.task, ans_decoded):
                    case 1:
                        print(font_color_green("Task solved!"))

                    case 0:
                        print(font_color_red("Wrong answer!"))

                    case -1:
                        print(font_color_orange("This task was already solved!"))

        elif (day_dir / f"task{args.task}.out").stat().st_size != 0:
            is_correct_solution(sol_file, day_dir / "task.in", day_dir / f"task{args.task}.out")

    else:
        print(
            font_color_red(
                f"{failed_testcases} {'testcase' if failed_testcases == 1 else 'testcases'} failed!",
            ),
        )
        sys.exit(1)


def test_cli(subparsers: argparse._SubParsersAction) -> None:
    """
    Set up the command-line interface for the 'test' command.

    This function configures the argument parser for the 'test' command, allowing users to specify
    the year, day, task, and options for continuing on failure or solving the task. It ensures that
    all necessary arguments are available for executing the testing process.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers action object to which the 'test'
            command parser will be added.

    """
    parser: argparse.ArgumentParser = subparsers.add_parser(
        "test",
        help="Run tests for one Advent of Code challenge.",
    )
    parser.add_argument(
        "-l",
        "--lang",
        "--language",
        type=str,
        default="py",
        help="The language of the solution you want to test. Defaults to python.",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=datetime.datetime.now(tz=datetime.timezone.utc).year,
        help="The year of the Advent of Code challenge (e.g., 2024). Defaults to the current year.",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="The day of the Advent of Code challenge (e.g., 13). This option is required.",
    )
    parser.add_argument(
        "-t",
        "--task",
        type=int,
        required=True,
        help="The task number to test. This option is required.",
    )
    parser.add_argument(
        "-c",
        "--continue-on-failure",
        action="store_true",
        help="Continue running tests even if some fail.",
    )
    parser.add_argument(
        "-a",
        "--answer",
        action="store_true",
        help="Solve the task after running the tests, in case all tests passed.",
    )
    parser.add_argument(
        "-s",
        "--submit",
        action="store_true",
        help="Submit the answer of the task after running the tests, in case all tests passed. "
        "Note that this option implies the --answer option.",
    )


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the application.

    This function sets up an argument parser with subcommands based on functions that end with
    '_cli'. It returns the parsed arguments as a Namespace object, allowing for easy access to the
    command-line inputs.

    Returns:
        argparse.Namespace: The parsed command-line arguments.

    """
    parser = argparse.ArgumentParser(
        "aoc",
        description=(
            "A command-line application for managing and testing Advent of Code challenges, "
            "featuring modular subcommands for various tasks and easy argument parsing."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command")
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isfunction(obj) and name.endswith("_cli"):
            obj(subparsers)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    getattr(sys.modules[__name__], args.command)(args)


if __name__ == "__main__":
    main()
