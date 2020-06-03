#!/usr/bin/python3
"""BASE GEOMETRY CLASS"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
