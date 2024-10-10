"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=5 ; task=2)
"""

import sys


def get_param(memory: list[int], idx: int, param: int) -> int:
    return (
        memory[idx + param]
        if (memory[idx] // (10 ** (1 + param))) % 10 == 1
        else memory[memory[idx + param]]
    )


def main():
    memory = [int(n) for n in sys.stdin.readline().split(",")]
    i, output = 0, 0
    while i < len(memory):
        match memory[i] % 100:
            case 1 | 2 | 7 | 8:
                param1 = get_param(memory, i, 1)
                param2 = get_param(memory, i, 2)

                match memory[i] % 10:
                    case 1:
                        ans = param1 + param2

                    case 2:
                        ans = param1 * param2

                    case 7:
                        ans = int(param1 < param2)

                    case 8:
                        ans = int(param1 == param2)

                memory[memory[i + 3]] = ans
                i += 4

            case 3:
                memory[memory[i + 1]] = 5  # Initial input
                i += 2

            case 4:
                assert output == 0
                output = get_param(memory, i, 1)
                i += 2

            case 5 | 6:
                param1 = get_param(memory, i, 1)
                param2 = get_param(memory, i, 2)
                if (memory[i] % 10 == 5 and param1 != 0) or (memory[i] % 10 == 6 and param1 == 0):
                    i = param2

                else:
                    i += 3

            case 99:
                break

            case _:  # Error
                pass

    print(output)


if __name__ == "__main__":
    main()
