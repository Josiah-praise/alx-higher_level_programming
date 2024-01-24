#!/usr/bin/python3
"""
Singly Linked List
"""


class Node:
    """A node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """creates a Node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """self.__data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """self.__data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """self.__next_node getter method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """self.__next_node setter method"""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        """Creates a singly linked list instance"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a node in sorted order"""
        if self.__head is None:
            self.__head = Node(value)
        else:
            newNode = Node(value)
            currentNode = self.__head
            if self.__head.data > value:
                newNode.next_node = self.__head
                self.__head = newNode
            else:
                while (
                    currentNode.next_node is not None
                    and currentNode.next_node.data < value
                ):
                    currentNode = currentNode.next_node
                newNode.next_node = currentNode.next_node
                currentNode.next_node = newNode

    def __display(self):
        """string representation of a singly linked list"""
        current = self.__head
        while current:
            if current.next_node is not None:
                print(current.data)
            else:
                print(current.data, end="")
            current = current.next_node

    def __str__(self):
        """calls the display function"""
        self.__display()
        return ""
