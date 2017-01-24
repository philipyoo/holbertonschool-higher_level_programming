#!/usr/bin/python3
"""
This is the "Single Linked List" module.

Class Node takes in integer values as data within each node,
and a next attribute which points to the next node or to None.

Class SinglyLinkedList initializes a default head of None.
Method sorted_insert handles all nodes created and adds them to
the linked list sorted by the int value stored within.
"""


class Node:
    """A class that creates a single Node in a Linked List.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that creates a Singly Linked List.
    """
    def __init__(self):
        self.__head = None

    def __repr__(self):
        temp = self.__head
        total = ""
        while temp:
            total += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                total += "\n"
        return total

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            curr = self.__head
            prev = None
            while curr and value > curr.data:
                prev = curr
                curr = curr.next_node
            if curr is None:
                prev.next_node = Node(value)
            elif curr is self.__head and prev is None:
                self.__head = Node(value, curr)
            else:
                newNode = Node(value, curr)
                prev.next_node = newNode
