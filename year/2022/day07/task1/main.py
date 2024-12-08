"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=7 ; task=1)
"""

import sys
from typing import Union


class Dir:
    """
    Represent a directory in a file system.

    This class serves as a helper to model a directory, including its name, parent directory, subdirectories, and files.
    It also holds a placeholder for the directory's size, which can be calculated based on its contents.

    Attributes:
        subdirs (dict): A dictionary mapping subdirectory names to their corresponding Dir objects.
        files (list): A list of files contained in the directory.
        size (int | None): The size of the directory, which will be calculated based on its contents.

    """

    def __init__(self, name: str, parent: Union["Dir", None] = None) -> None:
        """
        Initialize a new directory instance.

        This constructor sets up a directory with a specified name and an optional parent directory. It also initializes
        empty collections for subdirectories and files, and sets the size attribute to None until it is calculated.

        Args:
            name (str): The name of the directory.
            parent (Dir | None, optional): The parent directory of this directory. Defaults to None.

        """
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = []
        self.size = None


# update directory size and get the sum of sizes of those with size at most threshold
def get_size_sum(cwd: Dir, threshold: int = 100000) -> int:
    """
    Calculate the total size of files and directories that are below a specified size threshold.

    This function recursively computes the sizes of a directory and its subdirectories, summing the sizes of those that
    do not exceed the given threshold. It updates the size of the current directory and returns the total size of all
    directories that meet the size criteria.

    Args:
        cwd (Dir): The current directory object containing files and subdirectories.
        threshold (int, optional): The size threshold for including directories in the sum. Defaults to 100000.

    Returns:
        int: The total size of directories and files that are below the specified threshold.

    """
    cwd.size = 0
    ans = 0
    for d in cwd.subdirs.values():
        ans += get_size_sum(d, threshold)  # recursively work on subdirectories
        cwd.size += d.size

    for _, fs in cwd.files:  # work on files
        cwd.size += fs

    return ans + (cwd.size if cwd.size <= threshold else 0)


def main() -> None:
    dir_tree = Dir("/")  # root dir
    cwd = dir_tree
    for cmd_line in sys.stdin:
        cmd = cmd_line.strip().split()
        match cmd[0]:
            case "$":
                if cmd[1] == "cd":
                    match cmd[2]:
                        case "/":  # go to root directory
                            cwd = dir_tree

                        case "..":  # go to parent directory
                            cwd = cwd.parent

                        case _:  # go to subdirectory
                            cwd = cwd.subdirs[cmd[2]]

            case "dir":  # current directory has a 'cmd[2]' subdirectory
                cwd.subdirs[cmd[1]] = Dir(cmd[1], parent=cwd)

            case _:  # current directory has a 'cmd[1]' file with 'cmd[0]' size
                cwd.files.append((cmd[1], int(cmd[0])))

    print(get_size_sum(dir_tree))


if __name__ == "__main__":
    main()
