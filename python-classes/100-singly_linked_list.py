#!/usr/bin/python3
"""Module for singly linked list classes."""


class Node:
    """Defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data, ensuring it is an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, ensuring it's a Node or None."""
        if value is not None and not isinstance(value, Node):

