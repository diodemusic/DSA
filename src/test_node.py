"""Linked list test module."""

from node import Node

node_one = Node("a")
node_two = Node(["b", "c", "d"])
node_three = Node(True)


def test_init() -> None:
    """Test __init__() constructor."""

    assert node_one.value == "a"
    assert node_one.next_node is None
    assert node_one.prev_node is None


def test_get_value() -> None:
    """Test add to head method."""

    value: list[str] = ["b", "c", "d"]

    assert node_two.get_value() == value


def test_get_next_node() -> None:
    """Test get next node method."""

    node_one.set_next_node(node_two)

    assert node_one.get_next_node() == node_two


def test_get_prev_node() -> None:
    """Test get prev node method."""

    node_two.set_prev_node(node_one)

    assert node_two.get_prev_node() == node_one
