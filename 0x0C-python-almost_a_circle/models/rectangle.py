#!/usr/bin/python3
""" Useless Docstring += 1"""
from models.base import Base


class Rectangle(Base):
    """
    ----------------
    CLASS: RECTANGLE
    ----------------
    """

    # ------------------------------ #
    #          MAGIC METHODS         #
    # ------------------------------ #

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes the needed variables for the class.
        Args:
            @x: horizontal length
            @y: vertical length
            @width: width
            @height: height
            @id: id generated from Class, Base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        ---------------
        METHOD: __STR__
        ---------------
        Description:
            Overrides the usual str method with a
            custom definition. This function returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
            when called with print or str()
        Args:
            @self: refers back to the class
        """
        r = "[Rectangle] ({}) {}/{} - {}/{}"
        r = r.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return r

    # ------------------------------ #
    #          GETTERS/SETTERS       #
    # ------------------------------ #

    @property
    def x(self):
        """
        --------------------
        METHOD: X - (GETTER)
        --------------------
        Description:
            Getter method for atrribute x
        Args:
            @self: refers back to the class
        """
        return self.__x

    @x.setter
    def x(self, value=0):
        """
        --------------------
        METHOD: X - (SETTER)
        --------------------
        Description:
            Setter method for attribute x
        Args:
            @self: refers back to the class
            @value: value to set onto attribute x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        --------------------
        METHOD: y - (GETTER)
        --------------------
        Description:
            Getter method for atrribute y
        Args:
            @self: refers back to the class
        """
        return self.__y

    @y.setter
    def y(self, value=0):
        """
        --------------------
        METHOD: y - (SETTER)
        --------------------
        Description:
            Setter method for attribute y
        Args:
            @self: refers back to the class
            @value: value to set onto attribute y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """
        ------------------------
        METHOD: width - (GETTER)
        ------------------------
        Description:
            Getter method for atrribute width
        Args:
            @self: refers back to the class
        """
        return self.__width

    @width.setter
    def width(self, value=0):
        """
        --------------------
        METHOD: width - (SETTER)
        --------------------
        Description:
            Setter method for attribute width
        Args:
            @self: refers back to the class
            @value: value to set onto attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        -------------------------
        METHOD: height - (GETTER)
        -------------------------
        Description:
            Getter method for atrribute height
        Args:
            @self: refers back to the class
        """
        return self.__height

    @height.setter
    def height(self, value=0):
        """
        --------------------
        METHOD: height - (SETTER)
        --------------------
        Description:
            Setter method for attribute height
        Args:
            @self: refers back to the class
            @value: value to set onto attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # -------------------------- #
    #       PUBLIC METHODS       #
    # -------------------------- #
    def area(self):
        """
        ------------
        METHOD: AREA
        ------------
        Description:
            Retrieves the width and height of a rectangle
            and returns the area as output
        Args:
            @self: refers back to the class
        """
        return self.__height * self.__width

    def display(self):
        """
        ---------------
        METHOD: DISPLAY
        ---------------
        Description:
            Prints out a representation of a given
            rectangle based off the current values
            present in the instance.
        Args:
            @self: refers back to the class
        """
        # EDGE CASES, Size 1 and 1 (h / w)
        print("\n" * self.__y, end="")
        for height in range(self.__height):
            print(" " *  self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        --------------
        METHOD: UPDATE
        --------------
        Description:
            Updates the values in the instance.
        Args:
            @self: refers back to the class
            @args/kwargs: multiple arguments where
            args contains a number of values to be
            updated and kwargs contains a dictionary
            of values to be updated.
                - If args has been defined, then
                it would be assigned in the following
                order: (id, width, height, x, y)
                - Values cannot be skipped over.
                However, if a specific attribute needs
                to be updated, the dictionary argument
                would handle it accordingly.
        """
        if args and len(args) > 0:
            i,argc = 0, len(args)
            for elements in range(5):
                if args[i]:
                    self.id = args[i]
                    i += 1
                if i == argc:
                    break
                if args[1]:
                    self.width = args[i]
                    i += 1
                if i == argc:
                    break
                if args[i]:
                    self.height = args[i]
                    i += 1
                if i == argc:
                    break
                if args[i]:
                    self.x = args[i]
                    i += 1
                if i == argc:
                    break
                if args[i]:
                    self.y = args[i]
                    break
        else:
            if kwargs and len(kwargs) > 0:
                keycount = len(kwargs)
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'width' in kwargs:
                    self.width = kwargs['width']
                if 'height' in kwargs:
                    self.height = kwargs['height']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        """
        ---------------------
        METHOD: TO DICTIONARY
        ---------------------
        Description:
            Returns a dictionary of the current
            instance
        Args:
            @self: refers back to the class
        """
        attr_dict = {}
        attr_dict['id'] = self.id
        attr_dict['width'] = self.__width
        attr_dict['height'] = self.__height
        attr_dict['x'] = self.__x
        attr_dict['y'] = self.__y
        return attr_dict
