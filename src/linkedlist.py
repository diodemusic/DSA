"""Linked list module"""

from node import Node


class LinkedList:
    """Linked list data structure"""

    def __init__(self, head: Node | None = None) -> None:
        self.head: Node | None = head
