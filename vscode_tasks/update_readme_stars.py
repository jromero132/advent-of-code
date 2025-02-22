"""
Module for updating the readme file with Advent of Code stars.

This module contains functions to retrieve the number of stars for each year of the Advent of Code
and to update a readme file with badges and a summary table reflecting the stars data. It serves as
a utility for maintaining an up-to-date representation of achievements in the Advent of Code
challenges.
"""

from pathlib import Path

YEAR_DIR = "year"
README_FILE_PATH = Path("readme.md")


def get_stars_data(year_dir: Path) -> list[tuple[str, int]]:
    """
    Retrieve the number of stars for each year in the Advent of Code.

    This function scans the specified directory for subdirectories representing years of the Advent
    of Code and counts the number of directories for each year. Each of these directories represents
    a day challenge for Advent of Code and inside each of these days, the number of directories
    represents the number of tasks, and each task represents a star. So this basically returns the
    number of tasks directories for each year.

    Args:
        year_dir (Path): The path to the directory containing year subdirectories.

    Returns:
        list[tuple[str, int]]: A list of tuples where each tuple contains the year as a string and
            the corresponding count of stars (directories) as an integer.

    """
    print(f"Retrieving stars data for each year using the directory `{year_dir}`...")
    stars_data = [
        (
            year.name,
            sum(sum(path.is_dir() for path in day.iterdir()) for day in sorted(year.iterdir())),
        )
        for year in sorted(year_dir.iterdir())
    ]
    print(f"stars_data = {stars_data}")
    return stars_data


def update_readme_file(path: Path, stars_data: list[tuple[str, int]]) -> None:
    """
    Update the readme file with badges for each year and a table of stars.

    This function generates badge links and a summary table for the Advent of Code stars based on
    the provided stars data, and updates the specified readme file accordingly.

    Args:
        path (Path): The path to the readme file to be updated.
        stars_data (list[tuple[str, int]]): A list of tuples containing the year as a string and the
            corresponding number of stars as an integer.

    Raises:
        FileNotFoundError: If the specified readme file does not exist.

    """
    print(f"Updating `{path}` file with stars_data = {stars_data}\n")

    badges_text = "".join(
        f"[![AoC {year}]("
        f"https://img.shields.io/badge/{year}-⭐%20{stars}-gray?logo=adventofcode&labelColor=8a2be2"
        f")](https://adventofcode.com/{year}){'  ' if i % 5 == 0 else ''}\n"
        for i, (year, stars) in enumerate(stars_data, start=1)
    )
    print(f"Badges:\n{badges_text}\n")

    table_text = "| Year | Stars | Advent of Code Link |\n| :--: | :---: | :--: |\n" + "".join(
        f"| [{year}]({YEAR_DIR}/{year}) | ⭐️{stars}  | https://adventofcode.com/{year} |\n"
        for year, stars in stars_data
    )
    print(f"Table:\n{table_text}\n")

    with path.open(encoding="utf-8") as f:
        readme_text = f.read()

    print(f"Replacing `{path}` file with the badges and the table...")

    # Place badges
    badges_begin_mark = r"<!-- Badges of stars: begin -->"
    badges_end_mark = r"<!-- Badges of stars: end -->"
    badges_begin_pos = readme_text.index(badges_begin_mark) + len(badges_begin_mark) + 1
    badges_end_pos = readme_text.index(badges_end_mark)
    readme_text = readme_text[:badges_begin_pos] + badges_text + readme_text[badges_end_pos:]

    # Place sum of stars
    sum_of_stars = sum(stars for _, stars in stars_data)
    print(f"Replacing `{path}` file with sum of stars: {sum_of_stars}")
    sum_of_stars_marks = (
        (r"<!-- sum of stars 1: begin -->", r"<!-- sum of stars 1: end -->"),
        (r"<!-- sum of stars 2: begin -->", r"<!-- sum of stars 2: end -->"),
    )
    for begin_mark, end_mark in sum_of_stars_marks:
        begin_pos = readme_text.find(begin_mark) + len(begin_mark)
        end_pos = readme_text.find(end_mark)
        readme_text = f"{readme_text[:begin_pos]}(⭐ {sum_of_stars}){readme_text[end_pos:]}"

    # Place table
    table_begin_mark = r"<!-- Table summary of years: begin -->"
    table_end_mark = r"<!-- Table summary of years: end -->"
    table_begin_pos = readme_text.index(table_begin_mark) + len(table_begin_mark) + 1
    table_end_pos = readme_text.index(table_end_mark)
    readme_text = readme_text[:table_begin_pos] + table_text + readme_text[table_end_pos:]

    print(f"Saving `{path}` file...")
    with path.open("w", encoding="utf-8") as f:
        f.write(readme_text)

    print(f"File `{path}` updated successfully with the number of AoC stars!")


def main() -> None:
    """
    Update the readme file with Advent of Code stars.

    This function retrieves the stars data for each year and updates the readme file with the latest
    information, ensuring that the displayed badges and table contains the correct number of stars
    for each year.

    """
    stars_data = get_stars_data(Path(YEAR_DIR))
    update_readme_file(README_FILE_PATH, stars_data)


if __name__ == "__main__":
    main()
