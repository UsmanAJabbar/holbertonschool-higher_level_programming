#!/usr/bin/python3
"""SQUARE"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    -------------
    CLASS: SQUARE
    -------------
    """

    def __init__(self, size):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes a square with the given arguments
        Args:
            @self: refers back to the class
            @size: size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        ------------
        METHOD: AREA
        ------------
        Description:
            Returns the area of a given square
        Args:
            @self: refers back to the class
        """
        return self.__size ** 2
