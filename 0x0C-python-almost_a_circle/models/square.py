#!/usr/bin/python3
"""~~~~~~~~~"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    -------------
    CLASS: SQUARE
    -------------
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes the needed variables for the class.
        Args:
            @size: height
            @x: horizontal length
            @y: vertical length
            @id: id generated from Class, Base.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        ---------------
        METHOD: __STR__
        ---------------
        Description:
            Overrides the usual str method with a
            custom definition. This function returns
            [Square] (<id>) <x>/<y> - <size> when
            called with print or str()
        Args:
            @self: refers back to the class
        """
        s = "[Square] ({}) {}/{} - {}"
        s = s.format(self.id, self.x, self.y, self.size)
        return s

    @property
    def size(self):
        """
        --------------------
        METHOD: X - (GETTER)
        --------------------
        Description:
            Getter method for atrribute x
        Args:
            @self: refers back to the class
        """
        return self.__size

    @size.setter
    def size(self, value=0):
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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

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
            for elements in range(4):
                if args[i]:
                    self.id = args[i]
                    i += 1
                if i == argc:
                    break
                if args[1]:
                    self.size = args[i]
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
                if 'size' in kwargs:
                    self.size = kwargs['size']
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
        attr_dict['size'] = self.size
        attr_dict['x'] = self.x
        attr_dict['y'] = self.y
        return attr_dict
