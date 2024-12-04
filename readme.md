# Advent of Code Solutions and CLI

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black)](<https://buymeacoffee.com/jromero132> "Buy Me a Coffee - jromero132")
[![Advent of Code](https://img.shields.io/badge/Advent%20of%20Code-ffff66?logo=adventofcode&logoColor=000)](<https://adventofcode.com/> "Advent of Code homepage")
[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](<https://python.org> "Go to Python homepage")
![Last commit](https://img.shields.io/github/last-commit/jromero132/advent-of-code "Last commit")

---

<!-- Badges of stars: begin -->
[![AoC 2015](https://img.shields.io/badge/2015-⭐%2012-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2015)
[![AoC 2016](https://img.shields.io/badge/2016-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2016)
[![AoC 2017](https://img.shields.io/badge/2017-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2017)
[![AoC 2018](https://img.shields.io/badge/2018-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2018)
[![AoC 2019](https://img.shields.io/badge/2019-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2019)  
[![AoC 2020](https://img.shields.io/badge/2020-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2020)
[![AoC 2021](https://img.shields.io/badge/2021-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2021)
[![AoC 2022](https://img.shields.io/badge/2022-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2022)
[![AoC 2023](https://img.shields.io/badge/2023-⭐%2010-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2023)
[![AoC 2024](https://img.shields.io/badge/2024-⭐%208-gray?logo=adventofcode&labelColor=8a2be2)](https://adventofcode.com/2024)  
<!-- Badges of stars: end -->
---
This project contains all my solutions for [Advent of Code](https://adventofcode.com/) challenges.

> [!WARNING]
> Note that ***this project can automatically download tasks and inputs and submit your solutions*** to the Advent of
> Code server. Please use it moderately.

A brief introduction taken from the website:
> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that
> can be solved in any programming language you like. People use them as interview prep, company training, university
> coursework, practice problems, a speed contest, or to challenge each other.

In addition, this project contains a command-line application for managing, testing, solving and submitting
Advent of Code challenges. This tool allows users to create challenge setups, run tests, generate
test files, and provides solutions for various tasks.

> [!IMPORTANT]
> Take into account that if all tests passed and you select the option `-a` or `--answer` then
> the puzzle will be solved, and the output will be copied to the clipboard, so it can be
> easily pasted in the Advent of Code website. Also note that if you select the option
> `-s` or `--submit` then this answer will be automatically submitted to the Advent of Code
> server and you will get a console message to let you know whether you answered the task
> correctly or not 😄

## Table of Contents

- [Advent of Code Solutions and CLI](#advent-of-code-solutions-and-cli)
    - [Table of Contents](#table-of-contents)
    - [Stats](#stats)
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
        - [Commands](#commands)
    - [Solutions](#solutions)
        - [Directory Structure](#directory-structure)
    - [Contributing](#contributing)
    - [License](#license)
        - [Happy Coding! 🚀](#happy-coding-)

## Stats

For every year, the Advent of Code calendar has `25` challenges with `2` tasks per challenge. Every task gives you a
star ⭐️ so the maximum amount of stars for a year is `50`.

<!-- Table summary of years: begin -->
| Year | Stars | Advent of Code Link |
| :--: | :---: | :--: |
| [2015](year/2015) | ⭐️12  | https://adventofcode.com/2015 |
| [2016](year/2016) | ⭐️10  | https://adventofcode.com/2016 |
| [2017](year/2017) | ⭐️10  | https://adventofcode.com/2017 |
| [2018](year/2018) | ⭐️10  | https://adventofcode.com/2018 |
| [2019](year/2019) | ⭐️10  | https://adventofcode.com/2019 |
| [2020](year/2020) | ⭐️10  | https://adventofcode.com/2020 |
| [2021](year/2021) | ⭐️10  | https://adventofcode.com/2021 |
| [2022](year/2022) | ⭐️10  | https://adventofcode.com/2022 |
| [2023](year/2023) | ⭐️10  | https://adventofcode.com/2023 |
| [2024](year/2024) | ⭐️8  | https://adventofcode.com/2024 |
<!-- Table summary of years: end -->

## Features

- **Solutions**: Includes implementations for solving Advent of Code challenges.
- **Create Challenges**: Set up new Advent of Code challenges for a specified year and day.
- **Generate Test Files**: Create multiple test files for a given task.
- **Run Tests**: Execute tests for specific tasks with options to continue on failure and solve the
task in case all tests passed. Take into account that if the puzzle is solved, then the output will
be copied to the clipboard 😄
- **Submit Answer**: Allows you to automatically submit your answer for a specific task in the
Advent of Code challenges. This feature is essential if you who want to validate your solutions
against the official Advent of Code server without having to do it manually.

The `vscode_tasks` directory along with the `.vscode` directory enhances the development experience
for Advent of Code solutions by providing utility scripts and configurations specifically designed
for use within Visual Studio Code. This feature streamlines the process of executing and testing
solutions, making it easier to validate outputs and manage tasks. This will add a launch
configuration to run the current open file solution and 2 tasks, one for running the solution and
the other one for testing the solution.

## Installation

This application is cross-platform, so it works on Linux, MacOS and Windows. To use it, ensure you
have `Python >= 3.10` installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/jromero132/advent-of-code
cd advent-of-code
pip install -r requirements.txt
echo "AOC_COOKIE=<your-aoc-session-cookie>" > .env
```

> [!NOTE]
> The `AOC_COOKIE` is your Advent of Code session cookie. You can search for it pressing `F12`
and going into the `Network` tab in your browser.

## Usage

The application provides several commands. Use the `--help` option with the app or any command to
see its usage.

### Commands

- `create`: Create a new Advent of Code challenge.
- `maketests`: Create test files for one Advent of Code challenge.
- `test`: Run tests for one Advent of Code challenge.

## Solutions

This project includes all my solutions for Advent of Code challenges. You can run the solutions
directly or use the CLI to test them against provided inputs.

### Directory Structure

Each solution is organized by year, day and task, allowing easy access to the implementations.

```tree
advent-of-code
├── ...
├── year
│   ├── 2015
│   │   ├── day01
│   │   │   ├── task1
│   │   │   │   ├── tests
│   │   │   │   │   ├── 01.in
│   │   │   │   │   ├── 01.out
│   │   │   │   │   └── ...
│   │   │   │   ├── description.md
│   │   │   │   └── main.py
│   │   │   ├── task2
│   │   │   │   └── ...
│   │   │   ├── task.in
│   │   │   ├── task1.out
│   │   │   └── task2.out
│   │   ├── ...
│   │   └── day25
│   │       └── ...
│   ├── ...
│   └── 2023
│       └── ...
└── ...
```

`year/**`: Contains subdirectories for each year of challenges. For instance, from 2015 to 2023.

`day##/**`: Contains the solutions and additional files for each specified day of the Advent of Code
challenges. The days are numbered from `01` to `25`. Inside each day directory you will find:

- `task1/**`: This directory contains the solution for the first task of the Advent of Code
challenge for a specific year and day.
    - `tests/*`: This directory contains input and output files used for validating the solutions of
    the Advent of Code tasks. It is organized to facilitate testing and comparison of the
    implemented solutions against expected results.
        - `*.in`: This file contains sample input data that can be used to test the functionality of
        the solutions.
        - `*.out`: This file contains the expected output corresponding to the input data in `*.in`.
        It serves as a reference for validating the correctness of the solution by comparing the
        actual output generated by the program against this expected result.
    - `main.py`: This file contains the implementation of the solution for the respective task. It
    processes the input data from `task.in`, `tests/*.in` or custom input provided through the
    standard input, executes the necessary logic to solve the challenge, and generates the output.
- `task2/**`: This directory contains the solution for the second task of the Advent of Code
challenge for a specific year and day. It has the same structure as the `task1` directory.
- `task.in`: This file contains my personal input data required for both tasks solutions for the
specified year and day.
- `task1.out`: This file contains my output or solution for the first task. It serves as a record
of the result generated by my implementation based on the input provided in `task.in`.
- `task2.out`: This file contains my output or solution for the second task. It serves as a record
of the result generated by my implementation based on the input provided in `task.in`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug
fixes.

## License

This project is licensed under the MIT License - see the [license](license) file for details.

### Happy Coding! 🚀
