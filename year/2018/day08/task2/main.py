"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=8 ; task=2)
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
        self._value = None

    def get_value(self) -> int:
        """
        Calculate the value of a tree node based on specific rules for metadata interpretation.

        The method determines the node's value by either summing its metadata or recursively computing the values of its
        child nodes. The rules are as follows:
            - If a node has no child nodes, its value is the sum of its metadata entries.
            - If a node does have child nodes, the metadata entries become indexes which refer to those child nodes,
                starting the index from 1. The value of this node is the sum of the values of the child nodes referenced
                by the metadata entries. If a referenced child node does not exist, that reference is skipped.

        Returns:
            int: The computed value of the current tree node.

        """
        if self._value is None:
            if len(self.children) == 0:
                self._value = sum(self.metadata)

            else:
                self._value = 0
                for c in self.metadata:
                    self._value += (
                        self.children[c - 1].get_value() if c - 1 < len(self.children) else 0
                    )

        return self._value

    def get_whole_sum(self) -> int:
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
    print(tree.get_value())


if __name__ == "__main__":
    main()
