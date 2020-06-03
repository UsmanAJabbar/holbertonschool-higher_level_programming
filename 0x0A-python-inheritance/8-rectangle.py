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
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        -------------------------
        METHOD: INTEGER VALIDATOR
        -------------------------
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
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
