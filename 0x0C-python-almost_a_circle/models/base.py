#!/usr/bin/python3
"""FOR UNNECESSARY DOCSTRINGS IN FILES, ADD DOCS"""
import json
import csv


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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Added the two neccessary inputs
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        ----------------------
        METHOD: LOAD FROM FILE
        ----------------------
        Description:
            Returns a list of instances using a class.
        Args:
            @cls: takes in a class
        """
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename) as buffer:
                # * FROM_JSON_STRING returns a python repr of a JSON file
                # * CREATE creates a dummy instance and updates its values with
                # the values defined in a dictonary
                # TASK -
                    # The current class method returns a list of instances aka
                    # [class(), class(), class()]
                    # if the file does not exist, return an empty list
                # MASTER PLAN:
                # Try opening the file with the try method, if an exception is raised
                # return an empty list
                # If the file does exist, then return load the values from the json
                # file and use the create method to load up those attributes.
                # Once thats done, then create an empty list then would append the
                # returns from create.
                # After all that's done, return the final list
                json_list_of_dictionaries = []
                for lines in buffer:
                    json_list_of_dictionaries += (Base.from_json_string(lines))

                for elements in json_list_of_dictionaries:
                    instance_list.append(cls.create(**elements))

                return instance_list

        except FileNotFoundError:
                return instance_list

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """
            ------------------------
            METHOD: SAVE TO CSV FILE
            ------------------------
            Description:
                Serializes a Python object into CSV
                format and saves it into a csv file
            Args:
                @cls:
            """
            filename = cls.__name__ + ".csv"
            serialized_dump = []

            try:
                with open(filename, 'w') as csvfile:
                    if list_objs is not None:
                        #  Generate the field names based off the class name
                        if cls.__name__ == "Rectangle":
                            fields = ['id', 'width', 'height', 'x', 'y']
                        elif cls.__name__ == "Square":
                            fields = ['id', 'size', 'x', 'y']

                        #  Access and append the dictionaries in the instance
                        for objects in list_objs:
                            serialized_dump.append(objects.to_dictionary())

                        #  Start writing to the file
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        for dictonaries in serialized_dump:
                            writer.writerow(dictionaries)

            except FileNotFound:
                with open(fieldnames, "w") as csvfile:
                    csvfile.write(serialized_dump)
