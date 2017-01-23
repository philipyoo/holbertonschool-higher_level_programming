class Square:
    """A class that defines a square by size, which defaults 0.
    Also defines position using a tuple, which defaults (0, 0).
    Square can also get area, and print square using '#'.
    When printing, using position, offset on top and left.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        return (self.get_str())

    def area(self):
        return self.__size * self.__size

    def get_str(self):
        total = ""
        if self.__size is 0:
            total += "\n"
            return total
        for i in range(self.__position[1]):
            total += "\n"
        for i in range(self.__size):
            total += (" " * self.__position[0])
            total += ("#" * self.__size)
            if i is not (self.__size - 1):
                total += "\n"
        return total

    def my_print(self):
        print(self.get_str())
