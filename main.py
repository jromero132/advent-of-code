import inspect
import os
import subprocess
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace, _SubParsersAction
from datetime import date
from http import HTTPStatus
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

DAY_PATH = "year/{year}/day{day:02}"
TASK_PATH = DAY_PATH + "/task{task}"
TESTS_PATH = f"{TASK_PATH}/tests"

load_dotenv()


def font_color(txt: str, color: str) -> str:
    return f"{color}{txt}\033[0m"


def font_color_green(txt: str) -> str:
    return font_color(txt, "\033[92m")


def font_color_red(txt: str) -> str:
    return font_color(txt, "\033[91m")


def font_color_orange(txt: str) -> str:
    return font_color(txt, "\033[93m")


def font_color_blue(txt: str) -> str:
    return font_color(txt, "\033[94m")


def get_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}"


def get_response(url: str) -> requests.Response:
    response = requests.get(url, cookies={"session": os.getenv("AOC_COOKIE")})

    if response.status_code != HTTPStatus.OK:
        raise ValueError(
            f"Querying the url {url} resulted in status code {response.status_code} with the "
            f"following text: {response.text}"
        )

    return response


def get_html(year: int, day: int) -> str:
    return get_response(get_url(year, day)).text


def get_input(year: int, day: int) -> str:
    return get_response(f"{get_url(year, day)}/input").text


# Simplification of https://github.com/dlon/html2markdown/blob/master/html2markdown.py
def convert_html_to_markdown(tag):
    root_tag = tag
    footnotes = []

    def html_tags_to_markdown(tag):
        for child in tag.find_all(recursive=False):
            html_tags_to_markdown(child)

        match tag.name:
            case "h2":
                tag.insert_before("# ")
                tag.insert_after("\n")
                tag.unwrap()

            case "p":
                tag.insert_before("\n")
                tag.unwrap()

            case "em":
                # style = "**" if tag.has_attr("class") and "star" in tag["class"] else "*"
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
                tag.insert_after(f']({tag["href"]})')
                tag.unwrap()

            case "span":
                # tag.insert_before("*")
                # tag.insert_after("*")
                nonlocal footnotes
                footnotes.append(f"[^{len(footnotes) + 1}]: [{tag.text}] {tag['title']}")
                tag.insert_after(f"[^{len(footnotes)}]")
                tag.unwrap()

            case "ul":
                tag.contents = tag.contents[1:-1]
                tag.unwrap()

            case "li":
                tag.insert_before("  - ")
                # tag.insert_after("\n")
                tag.unwrap()

            case "code":
                # if "\n" in tag.text:
                #     tag.insert_before("```\n")
                #     tag.insert_after("\n```")
                # else:
                #     tag.insert_before("`")
                #     tag.insert_after("`")
                tag.insert_before("`")
                tag.insert_after("`")
                tag.unwrap()

            case "pre":
                tag.insert_before("")
                # tag.insert_after("\n")
                tag.unwrap()

            case "article":
                pass

            case _:
                raise ValueError(f"Missing condition for tag: {tag.name}")

    html_tags_to_markdown(root_tag)
    return f"{root_tag.text}\n{'\n\n'.join(footnotes)}\n" if footnotes else root_tag.text


def get_markdown(year: int, day: int) -> list[str]:
    soup = BeautifulSoup(get_html(year, day), features="html.parser")
    articles = soup.body.main.findAll("article", recursive=False)
    return [convert_html_to_markdown(article) for article in articles]


def create(args: Namespace):
    template_content = ""
    if args.template and (template := Path(args.template)).exists():
        with open(template, "r", encoding="utf-8") as f:
            template_content = f.read().replace("`year`", str(args.year))
            template_content = template_content.replace("`day`", str(args.day))

    mds = get_markdown(args.year, args.day)

    for i, md in enumerate(mds, start=1):
        task_dir = Path(TASK_PATH.format(year=args.year, day=args.day, task=i))

        task_dir.mkdir(parents=True, exist_ok=True)

        with open(task_dir / "description.md", "w", encoding="utf-8") as f:
            f.write(md)

        code_content = template_content.replace("`task`", str(i))
        if not (py_file := task_dir / "main.py").exists():
            with open(py_file, "w", encoding="utf-8") as f:
                f.write(code_content)

    with open(
        f"{DAY_PATH.format(year=args.year, day=args.day)}/task.in", "w", encoding="utf-8"
    ) as f:
        f.write(get_input(args.year, args.day))


def create_cli(subparsers: _SubParsersAction):
    parser: ArgumentParser = subparsers.add_parser(
        "create", help="Settings for deploying the project"
    )
    parser.add_argument("-y", "--year", type=int, default=date.today().year, help="")
    parser.add_argument("-d", "--day", type=int, required=True, help="")
    parser.add_argument("-t", "--template", default=None, help="")


def maketests(args: Namespace):
    tests_dir = Path(TESTS_PATH.format(year=args.year, day=args.day, task=args.task))
    tests_dir.mkdir(exist_ok=True, parents=True)

    for i in range(1, args.number + 1):
        if not (test_in := tests_dir / f"{i:02}.in").exists():
            test_in.touch()

        if not (test_out := tests_dir / f"{i:02}.out").exists():
            test_out.touch()


def maketests_cli(subparsers: _SubParsersAction):
    parser: ArgumentParser = subparsers.add_parser(
        "maketests", help="Settings for deploying the project"
    )
    parser.add_argument("-y", "--year", type=int, default=date.today().year, help="")
    parser.add_argument("-d", "--day", type=int, required=True, help="")
    parser.add_argument("-t", "--task", type=int, required=True, help="")
    parser.add_argument("-n", "--number", type=int, required=True, help="")


def test(args: Namespace):
    def get_code_output(sol_file: Path, inp: Path) -> bytes:
        with open(inp, "r", encoding="utf-8") as in_file:
            return subprocess.check_output(["py", str(sol_file)], stdin=in_file).strip()

    day_dir = Path(DAY_PATH.format(year=args.year, day=args.day)).absolute()
    task_dir = Path(TASK_PATH.format(year=args.year, day=args.day, task=args.task)).absolute()
    tests_dir = Path(TESTS_PATH.format(year=args.year, day=args.day, task=args.task)).absolute()
    sol_file = task_dir / "main.py"
    failed_testcases = 0
    print(f"Start testing AOC y{args.year}/d{args.day}/t{args.task}...")
    for inp in sorted(f for f in tests_dir.iterdir() if f.suffix == ".in"):
        print(f"  - {inp.name}    ", end="")
        ans = get_code_output(sol_file, inp)
        with open(inp.with_suffix(".out"), "rb") as out_file:
            sol = out_file.readline().strip()

        if ans == sol:
            print(font_color_green("OK"))

        else:
            print(
                font_color_red("FAIL")
                + " ["
                + font_color_orange(f"found={ans.decode('utf-8')}")
                + " ; "
                + font_color_blue(f"expected={sol.decode('utf8')}")
                + "]"
            )
            failed_testcases += 1
            if not args.continue_on_failure:
                break

    if failed_testcases == 0:
        print(font_color_green("All tests passed!"))
        if args.solve:
            ans = get_code_output(sol_file, day_dir / "task.in").decode("utf-8")
            with open(day_dir / f"task{args.task}.out", "w", encoding="utf-8") as f:
                f.write(ans)
                f.write("\n")

            print(f"Answer={font_color_blue(ans)}")

            if os.name == "nt":  # Windows
                subprocess.run("clip", text=True, input=ans)

            # TODO: Continue working on copying the solution to clipboard for other OSs.

    else:
        print(
            font_color_red(
                f"{failed_testcases} {'testcase' if failed_testcases == 1 else 'testcases'} failed!"
            )
        )


def test_cli(subparsers: _SubParsersAction):
    parser: ArgumentParser = subparsers.add_parser(
        "test", help="Settings for deploying the project"
    )
    parser.add_argument("-y", "--year", type=int, default=date.today().year, help="")
    parser.add_argument("-d", "--day", type=int, required=True, help="")
    parser.add_argument("-t", "--task", type=int, required=True, help="")
    parser.add_argument("-c", "--continue-on-failure", action="store_true", help="")
    parser.add_argument("-s", "--solve", action="store_true", help="")


def parse_args() -> Namespace:
    parser = ArgumentParser("qwerty", formatter_class=ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(dest="command")
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isfunction(obj) and name.endswith("_cli"):
            obj(subparsers)

    return parser.parse_args()


def main():
    args = parse_args()
    getattr(sys.modules[__name__], args.command)(args)


if __name__ == "__main__":
    main()
