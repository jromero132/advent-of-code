"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=8 ; task=1)
"""

import sys


class Tree:
    """
    A Tree represents a hierarchical data structure with metadata and child nodes.

    Attributes:
        parent (Tree, optional): Parent node of the current tree node.
        children (list[Tree]): List of child nodes.
        metadata (list[int]): Metadata associated with the current node.

    """

    def __init__(self, parent: "Tree" = None, metadata: list[int] = None):
        """
        Initialize a Tree node.

        Args:
            parent (Tree, optional): Parent node of the current tree node. Defaults to None.
            metadata (list[int], optional): Metadata associated with the current node. Defaults to None.

        """
        self.parent = parent
        self.children: list["Tree"] = []
        self.metadata = metadata or []

    def get_sum(self) -> int:
        """
        Calculate the sum of metadata for the current node.

        Returns:
            int: Sum of metadata for the current node.

        """
        return sum(self.metadata)

    def get_whole_sum(self) -> int:
        """
        Recursively calculate the total sum of metadata for the current node and all its descendants.

        Returns:
            int: Total sum of metadata for the current node and all its children.

        """
        return self.get_sum() + sum(child.get_whole_sum() for child in self.children)


def build_tree(flat_tree: list[int], pos: int = 0, parent: Tree = None) -> tuple[Tree, int]:
    """
    Recursively builds a tree structure from a flattened list of integers.

    The function transforms a linear representation into a hierarchical tree with nested children and metadata. The
    structure of each node of the tree is:
        - A header, which is always exactly two numbers:
            - The quantity of child nodes.
            - The quantity of metadata entries.
        - Zero or more child nodes (as specified in the header).
        - One or more metadata entries (as specified in the header).

    Args:
        flat_tree (list[int]): A flattened list representing the tree structure.
        pos (int, optional): Starting position in the flat_tree list. Defaults to 0.
        parent (Tree, optional): Parent tree node for the current recursive call. Defaults to None.

    Returns:
        tuple[Tree, int]: A tuple containing the constructed tree and the last processed position.

    """
    tree = Tree(parent)
    last_pos = pos + 2
    for _ in range(flat_tree[pos]):
        child, last_pos = build_tree(flat_tree, last_pos, tree)
        tree.children.append(child)

    tree.metadata = flat_tree[last_pos : last_pos + flat_tree[pos + 1]]
    return tree, last_pos + flat_tree[pos + 1]


def main() -> None:
    flat_tree = [int(x) for x in sys.stdin.read().strip().split()]
    tree, pos = build_tree(flat_tree)
    assert pos == len(flat_tree)
    print(tree.get_whole_sum())


if __name__ == "__main__":
    main()
