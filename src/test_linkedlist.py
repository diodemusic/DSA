"""Linked list test module."""

from linkedlist import LinkedList
from node import Node

linked_list = LinkedList()

value_one: dict[str, int | bool] = {"some_value": 12, "some_other_value": True}
node_one: Node = Node(value_one)

value_two: list[bool] = [True, True, False]
node_two: Node = Node(value_two)


def test_add_to_empty_head() -> None:
    """Test add to head method where head is empty."""

    linked_list.add_to_head(node_one)

    assert linked_list.head is not None
    assert linked_list.head.get_value() == value_one
    assert type(isinstance(linked_list.head, dict))
    assert linked_list.head.get_next_node() is None
    assert node_one.get_next_node() is None


def add_to_non_empty_head() -> None:
    """Test add to head method where head is non-empty."""

    linked_list.add_to_head(node_one)

    assert linked_list.head is not None

    linked_list.add_to_head(node_two)

    assert linked_list.head is not None
    assert linked_list.head.get_value() == value_two
    assert type(isinstance(linked_list.head, list))
    assert linked_list.head == node_two
    assert linked_list.head.get_next_node() is node_one
    assert node_two.get_next_node() == node_one
