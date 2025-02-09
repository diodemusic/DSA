"""Node module"""

from typing import Any, Self


class Node:
    """Node data structure"""

    def __init__(
        self, value: Any, next_node: Self | None = None, prev_node: Self | None = None
    ) -> None:
        self.value: Any = value
        self.next_node: Self | None = next_node
        self.prev_node: Self | None = prev_node

    def get_value(self) -> Any:
        """
        Get the value from the Node object.

        Returns:
            Any: Nodes value.
        """

        return self.value

    def get_next_node(self) -> Self | None:
        """
        Get the next Node object from the current object next pointer.

        Returns:
            Self | None: Node object.
        """

        return self.next_node

    def get_prev_node(self) -> Self | None:
        """
        Get the previous Node object from the current object prev pointer.

        Returns:
            Self | None: Node object.
        """

        return self.prev_node
