#!/usr/bin/python3
"""BASE GEOMETRY CLASS"""


class BaseGeometry:
    """
    --------------------
    CLASS: BASE GEOMETRY
    --------------------
    """

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
