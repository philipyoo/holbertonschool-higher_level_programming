class Node:
    """A class that creates a single Node in a Linked List.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next must be a Node object")
        self.__next = value


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
            temp = temp.next
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
                curr = curr.next
            if curr is None:
                prev.next = Node(value)
            elif curr is self.__head and prev is None:
                self.__head = Node(value, curr)
            else:
                newNode = Node(value, curr)
                prev.next = newNode

#
