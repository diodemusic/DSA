"""Linked list test module."""

from linkedlist import LinkedList
from node import Node

linked_list = LinkedList()


def test_init() -> None:
    """Test __init__() constructor."""

    assert linked_list.head is None


def test_add_to_head() -> None:
    """Test add to head method."""

    value: dict[str, int | bool] = {"some_value": 12, "some_other_value": True}

    linked_list.add_to_head(Node(value))

    assert linked_list.head is not None
    assert linked_list.head.get_value() == value
    assert type(isinstance(linked_list.head, dict))
