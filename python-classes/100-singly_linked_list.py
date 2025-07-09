#!/usr/bin/python3
class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data  # Validated via the setter
        self.next_node = next_node  # Validated via the setter

    @property
    def data(self):
        """Retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data, must be an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, must be None or a Node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None  # Private attribute

    def __str__(self):
        """String representation of the list"""
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node in the correct sorted position (increasing order)"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
