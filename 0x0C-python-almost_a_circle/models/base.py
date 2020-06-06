#!/usr/bin/python3
"""FOR UNNECESSARY DOCSTRINGS IN FILES, ADD DOCS"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        ----------------------
        METHOD: TO JSON STRING
        ----------------------
        Description:
            Returns the JSON representation
            of the current instance
        Args:
            @list_dictionaries: list
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        --------------------
        METHOD: SAVE TO FILE
        --------------------
        Description:
            Dumps JSON representation of a
            Python object to a given file
        Args:
            @cls: class-wide method
            @list_objs: objects to be added
        """
        filename = cls.__name__ + ".json"
        serialized_dump = []

        if list_objs is not None:
            for objects in list_objs:
                serialized_dump.append(objects.to_dictionary())

        deserialized = Base.to_json_string(serialized_dump)

        with open(filename, 'w') as jsonfile:
            jsonfile.write(deserialized)

    @staticmethod
    def from_json_string(json_string):
        """
        ------------------------
        METHOD: FROM JSON STRING
        ------------------------
        Description:
            Takes in a JSON string and returns
            a Python representation of it.
        Args:
            @json_string: json string to be
            deserialized
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        --------------
        METHOD: CREATE
        --------------
        Description:
            Returns an instance of the class with the
            attributes pre-assigned to it.
        Args:
            @cls: class-wide method
            @dictionary: dictionary containing all the
            values to assign onto the new instance
        """
        dummy = cls(1, 1)  # Added the two neccessary inputs
        dummy.update(dictionary)
        return dummy
