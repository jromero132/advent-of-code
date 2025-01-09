"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=9 ; task=2)
"""

from __future__ import annotations

import sys


class Node:
    """
    Represents a node in a doubly linked list.

    Nodes store data and pointers to their left and right neighbors.
    """

    def __init__(self, data: int, left: Node | None = None, right: Node | None = None) -> None:
        """
        Initialize a new Node.

        Args:
            data: The data to store in the node.
            left: The left neighbor of the node.
            right: The right neighbor of the node.

        """
        self.data = data
        self.left = left
        self.right = right


class LinkedList:
    """
    Represents a circular doubly linked list.

    It allows insertion, moving the current node, and popping elements.
    """

    def __init__(self, array: list[int] | None = None) -> None:
        """
        Initialize a new LinkedList.

        Args:
            array: An optional list of initial values to populate the list.

        """
        self.size = 0
        self.node = None

        if array:
            for x in array:
                self.insert(x)

    def move(self, steps: int) -> None:
        """
        Move the current node by a given number of steps.

        Args:
            steps: The number of steps to move (positive for right, negative for left).

        """
        steps %= self.size  # move at max the size
        steps = (
            steps if steps <= abs(steps - self.size) else steps - self.size
        )  # move at max half of the size

        if steps > 0:  # move right
            for _ in range(steps):
                self.node = self.node.right

        else:  # move left
            for _ in range(-steps):
                self.node = self.node.left

    def insert(self, data: int) -> None:
        """
        Insert a new node with the given data after the current node.

        Args:
            data: The data to insert into the list.

        """
        node = Node(data)
        if self.size == 0:
            node.right = node.left = node

        else:
            node.left = self.node
            node.right = self.node.right
            self.node.right.left = node
            self.node.right = node

        self.node = node
        self.size += 1

    def pop(self) -> int:
        """
        Remove and returns the data of the current node.

        Returns:
            The data of the removed node.

        """
        data = self.node.data
        self.size -= 1

        if self.size == 0:
            self.node = None

        else:
            self.node.left.right = self.node.right
            self.node.right.left = self.node.left
            self.node = self.node.right

        return data


def main() -> None:
    line = sys.stdin.read().strip().split()
    players, marbles = int(line[0]), int(line[-2]) * 100
    scores, board = [0] * players, LinkedList([0])
    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            board.move(-7)
            scores[marble % players] += marble + board.pop()

        else:
            board.move(1)
            board.insert(marble)

    print(max(scores))


if __name__ == "__main__":
    main()
