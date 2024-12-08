"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=7 ; task=2)
"""

import sys


def dfs(lines: dict[str, tuple[str]], origin: str, data: dict[str, int]) -> int:
    if origin.isdigit():
        return int(origin)

    if origin in data:
        return data[origin]

    op = lines[origin]
    match len(op):
        case 1:  # assignment
            res = dfs(lines, op[0], data)
            data[origin] = res
            return res

        case 2:  # not operator
            res = ~dfs(lines, op[1], data)
            data[origin] = res
            return res

        case 3:
            left, right = dfs(lines, op[0], data), dfs(lines, op[2], data)
            match op[1]:
                case "AND":
                    res = left & right

                case "OR":
                    res = left | right

                case "LSHIFT":
                    res = left << right

                case "RSHIFT":
                    res = left >> right

            data[origin] = res
            return res


def main() -> None:
    lines = [line.strip().split(" -> ") for line in sys.stdin]
    lines = {line[1]: tuple(line[0].split()) for line in lines}
    target = "f" if len(lines) <= 10 else "a"  # I set 'f' just for testing. f = 1968
    var_to_change = "x" if len(lines) <= 10 else "b"  # I set 'x' just for testing.
    res = dfs(lines, target, {})
    lines[var_to_change] = (str(res),)
    print(dfs(lines, target, {}))


if __name__ == "__main__":
    main()
