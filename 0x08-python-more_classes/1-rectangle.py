#!/usr/bin/python3
"""DEFINING A RECTANGLE"""


class Rectangle:
    """
    ----------------
    CLASS: RECTANGLE
    ----------------
    """

    def __init___(self, width=0, height=0)
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes needed variable for the class, Rectangle.
        Exceptions/Notes:
        Args:
            @width: width
            @height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        -------------
        METHOD: WIDTH
        -------------
        Description:
            Getter method retrives the value stored in width.
        Exceptions/Notes:
            Nil
        Args:
            @self: refers back to the class.
        -------------
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        -------------
        METHOD: WIDTH
        -------------
        Description:
            Setter method that inserts the value
            into the attributes initialized by __init__
            and retrieved by getter, width
        Exceptions/Notes:
            Verifies whether the inputs defined by
            @value is an integers/floats.
            Otherwise, TypeError's raised accordingly.
        Args:
            @self: refers back to the class
            @value: value to be assigned in width
        """
        if type(value) not in [float, int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        --------------
        METHOD: HEIGHT
        --------------
        Description:
            Getter method retrives the value stored in height.
        Exceptions/Notes:
            Nil
        Args:
            @self: refers back to the class.
        -------------
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        --------------
        METHOD: HEIGHT
        --------------
        Description:
            Setter method that inserts the value
            into the attributes initialized by __init__
            and retrieved by getter, height
        Exceptions/Notes:
            Verifies whether the inputs defined by
            @value is an integers/floats.
            Otherwise, TypeError's raised accordingly.
        Args:
            @self: refers back to the class
            @value: value to be assigned in height
        """
        if type(value) not in [float, int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
