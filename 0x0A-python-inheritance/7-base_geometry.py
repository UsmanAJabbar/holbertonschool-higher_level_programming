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
