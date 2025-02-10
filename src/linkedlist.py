"""Linked list module"""

from node import Node


class LinkedList:
    """Linked list data structure"""

    def __init__(self) -> None:
        self.head: Node | None = None

    def add_to_head(self, node: Node) -> None:
        """
        Add a node to the head.

        Args:
            node (Node): Node to add to head.
        """

        self.head = node
