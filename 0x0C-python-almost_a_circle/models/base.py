#!/usr/bin/python3
"""FOR UNNECESSARY DOCSTRINGS IN FILES, ADD DOCS"""


class Base:
    """
    -----------
    CLASS: BASE
    -----------
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes the needed attributes for the class
        Args:
            @self: refers back to the class
            @id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
