#!/usr/bin/python3
"""BASE GEOMETRY CLASS"""


class BaseGeometry:
    """
    --------------------
    CLASS: BASE GEOMETRY
    --------------------
    """
    pass

    def area(self):
        """
        ------------
        METHOD: AREA
        ------------
        Description:
            A function that raises a TypeError
        Args:
            @self: refers back to the class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        -------------------------
        METHOD: INTEGER VALIDATOR
        -------------------------
        Description:
            Validates whether any of the inputs
            are actual integers.
        Notes/Exceptions:
            If input value is not an integer raise
            TypeError accordingly
        Args:
            @name: name
            @value: value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
"""RECTANGLE"""


class Rectangle(BaseGeometry):
    """
    ----------------
    CLASS: RECTANGLE
    ----------------
    """

    def __init__(self, width, height):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            A rectangle that inherits from class BaseGeometry
        Notes/Exceptions:
            Inherits from BaseGeometry
        Args:
            @BaseGeometry: Imports class from BaseGeometry.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        ---------------
        METHOD: __STR__
        ---------------
        Description:
            Returns a string representation of the class
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        ------------
        METHOD: AREA
        ------------
        Description:
            Returns the area of the rectangle.
        Args:
            @self: refers back to the class/instance.
        """
        return (self.__height * self.__width)
"""SQUARE"""


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
