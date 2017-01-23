class Square:
    """A class that defines a square by size and can compute area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __lt__(self, other):
        return self.__size < other.size

    def __le__(self, other):
        return self.__size <= other.size

    def __eq__(self, other):
        return self.__size == other.size

    def __ne__(self, other):
        return self.__size != other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __ge__(self, other):
        return self.__size >= other.size
