#!/usr/bin/python3
""" Class Square """


class Square:
    """Initializing Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Method that initializes the class and checks
        for good input
        Args:
            self: refers back to the class
            size: default = 0, else defined input
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Method that retrieves the current size for
        the setter to work with
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method that sets the value
        Args:
            self: refers back to the class
            value: value defined
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Method that returns the area
        """
        return self.__size ** 2

    def my_print(self):
        """ Method that prints out a square size * size """
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))
        for height in range(self.__size):
            if self.__position[0] > 0:
                for spaces in range(self.__position[0]):
                    print(" ", end="")
            for width in range(self.__size):
                print("#", end="")
            print()
