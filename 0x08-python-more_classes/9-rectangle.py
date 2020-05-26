#!/usr/bin/python3
"""DEFINING A RECTANGLE"""


class Rectangle:
    """
    ----------------
    CLASS: RECTANGLE
    ----------------
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        ----------------
        METHOD: __STR__
        ----------------
        Description:
            Handles the __str__ property in python, except
            this time, it returns a string of "#" which allows
            if to be called and returned without being printed
            out twice.
        Exceptions/Notes:
            No exceptions are raised since the setter function
            validates data input before __str__ has a chance to
            work on it.
        Args:
            @self: refers back to the class, allowing the function
            to pull in the data stored in the private width and height
            attributes.
        """
        buffer = ""
        if self.__height is 0 or self.__width is 0:
            return buffer
        for elements in range(self.__height):
            buffer += (str(self.print_symbol) * self.__width)
            if elements < self.__height - 1:
                buffer += "\n"
        return(buffer)

    def __repr__(self):
        """
        -----------------
        METHOD: __REPR__
        -----------------
        Description:
            Handles the __repr__ property in Python. __repr__
            returns a string with all of the objects required
            to build a variable or object
            This string should be able to be evaluated by the
            method, eval.
            The eval method would recall an instance of this
            class, creating a new rectangle with custom inputs
        Exceptions/Notes:
            Nil
        Args:
            @self: refers back to the class, allowing the function to
            pull in data from the private width and height attributes.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        ---------------
        METHOD: __DEL__
        ---------------
        Description:
            When the class is being deleted,
            print a custom message.
        Exception/Notes:
            Nil
        Args:
            @self: refers back to the class
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        -----------------------
        METHOD: BIGGER OR EQUAL
        -----------------------
        Description:
            Bigger or equal returns the larger rect
            amongst two rectangles after comparing
            their areas
        Exceptions/Notes:
            If input is not of type, class(rect),
            then raise TypeError.
        Args:
            @rect_1: rectangle 1
            @rect_2: rectangle 2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        --------------
        METHOD: SQUARE
        --------------
        Description:
            Creates a new square based off of
            the current class(Rectangle)
        Exceptions/Notes:
            Nil
        Args:
            @cls: Refers to the current class
            @size: takes size as input
        """
        return cls(size, size) # Rectangle(width, height)

    def area(self):
        """
        ------------
        METHOD: AREA
        ------------
        Description:
            Method that returns the area of the rectangle.
        Exceptions/Notes:
            Nil
        Args:
            @self: refers back to the class
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        -----------------
        METHOD: PERIMETER
        -----------------
        Description:
            Method that returns the perimeter of the
            rectangle.
        Exceptions/Notes:
            Nil
        Args:
            @self: refers back to the class
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
