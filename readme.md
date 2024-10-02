# Advent of Code Solutions and CLI

This project contains all my solutions for Advent of Code challenges.

In addition, this project contains a command-line application for managing, testing, and solving
Advent of Code challenges. This tool allows users to create challenge setups, run tests, generate
test files, and provides solutions for various tasks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Commands](#commands)
- [Solutions](#solutions)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Solutions**: Includes implementations for solving Advent of Code challenges.
- **Create Challenges**: Set up new Advent of Code challenges for a specified year and day.
- **Run Tests**: Execute tests for specific tasks with options to continue on failure and solve the
task in case all tests passed.
- **Generate Test Files**: Create multiple test files for a given task.

## Installation

This application is cross-platform, so it works on Linux, MacOS and Windows. To use it, ensure you
have `Python >= 3.10` installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/jromero132/advent-of-code
cd advent-of-code
pip install -r requirements.txt
```

## Usage

The application provides several commands. Use the `--help` option with the app or any command to
see its usage.

### Commands

- `create` - Create a new Advent of Code challenge.
- `maketests` - Create test files for one Advent of Code challenge.
- `test` - Run tests for one Advent of Code challenge.

## Solutions

This project includes all my solutions for Advent of Code challenges. Each solution is organized by
year, day and task, allowing easy access to the implementations. You can run the solutions directly
or use the CLI to test them against provided inputs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug
fixes.

## License

This project is licensed under the MIT License - see the [license](license) file for details.
