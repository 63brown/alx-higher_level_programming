#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """Module of a node of a singly linked list
    Attributes:
        __data (int): data contained in node
        __next_node (Node): the following node in linked list
    """
    def __init__(self, data, next_node=None):
        """Initializes the node attributes
        Args:
            data (int): data contained in node
            next_node (Node): the following node in linked list
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        """Represents the Node objects as a string
        Returns:
            the representing string
        """
        return str(self.__data)

    @property
    def data(self):
        """getting the data
        Returns:
            data contained in node
        """
        return (self.__data)

    @property
    def next_node(self):
        """getting the next_node
        Returns:
            the following node in linked list
        """
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """setting the data
        Args:
            value (int): data contained in node
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setting the next_node
        Args:
            value (Node): the following node in linked list
        Returns:
            None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Module of a singly linked list
    Attributes:
        __head (Node): head of linked list
    """
    def __init__(self):
        """Initializes the singly linked list attributes
        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list
        Args:
            value (int): data contained in new node
        Returns:
            None
        """
        new = Node(value)
        temp = self.__head
        if temp is None or temp.data >= value:
            if temp:
                new.next_node = temp
            self.__head = new
            return
        while temp.next_node is not None:
            if temp.next_node.data >= value:
                break
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        """Represents the SinglyLinkedList objects as a string
        Returns:
            the representing string
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp)
            if temp.next_node is not None:
                string += "\n"
            temp = temp.next_node
        return (string)
