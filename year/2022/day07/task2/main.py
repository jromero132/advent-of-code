"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=7 ; task=2)
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


def update_size(cwd: Dir) -> None:  # update directory size
    """
    Update the size of a directory by calculating the total size of its contents.

    This function recursively computes the size of a directory, including the sizes of all its subdirectories and files.
    It sets the size attribute of the directory to the sum of its own files and the sizes of its subdirectories.

    Args:
        cwd (Dir): The directory object whose size is to be updated.

    """
    cwd.size = 0
    for d in cwd.subdirs.values():
        update_size(d)  # recursively work on subdirectories
        cwd.size += d.size

    for _, fs in cwd.files:  # work on files
        cwd.size += fs


# get the directory with the smallest size such that after delete it,
# 0the amount of free space is greater than the required space
def get_directory_to_delete(cwd: Dir, free_space: int, required_space: int) -> Dir:
    """
    Find the smallest directory that can be deleted to free up enough space.

    This function recursively searches through a directory and its subdirectories to identify the smallest directory
    that, when deleted, will provide sufficient free space. It compares the sizes of directories to determine which one
    meets the required space criteria while minimizing the size of the deleted directory.

    Args:
        cwd (Dir): The current directory object to search within.
        free_space (int): The amount of free space currently available.
        required_space (int): The amount of space that needs to be freed.

    Returns:
        Dir: The directory object that should be deleted to meet the space requirements.

    """
    ans = cwd
    for d in ans.subdirs.values():
        if free_space + d.size >= required_space:
            sub_ans = get_directory_to_delete(d, free_space, required_space)
            if ans.size > sub_ans.size:
                ans = sub_ans
    return ans


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
                cwd.subdirs[cmd[1]] = Dir(cmd[1], cwd)

            case _:  # current directory has a 'cmd[1]' file with 'cmd[0]' size
                cwd.files.append((cmd[1], int(cmd[0])))

    update_size(dir_tree)
    folder = get_directory_to_delete(
        dir_tree,
        free_space=70000000 - dir_tree.size,
        required_space=30000000,
    )
    print(folder.size)


if __name__ == "__main__":
    main()
