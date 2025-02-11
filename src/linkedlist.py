"""Linked list module"""

from node import Node


class LinkedList:
    """Linked list data structure"""

    def __init__(self) -> None:
        self.head: Node | None = None

    def add_to_head(self, new_head: Node) -> None:
        """
        Add a node to the head.

        Args:
            new_head (Node): Node to add to head.
        """

        if self.head is None:
            self.head = new_head
            return

        new_head.set_next_node(self.head)
        self.head = new_head
