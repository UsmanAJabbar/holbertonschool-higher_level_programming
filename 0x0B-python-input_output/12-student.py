#!/usr/bin/python3
"""CLASS STUDENT"""


class Student:
    """
    --------------
    CLASS: STUDENT
    --------------
    """

    def __init__(self, first_name, last_name, age):
        """
        ----------------
        METHOD: __INIT__
        ----------------
        Description:
            Initializes public variables.
        Args:
            @self: refers back to the class
            @first_name: first name
            @last_name: last name
            @age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"
        ---------------
        METHOD: TO JSON
        ---------------
        """
        search = {}
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        if type(attrs) is list:
            for keys in attrs:
                if type(keys) is not str:
                    return self.__dict__
                if keys in self.__dict__:
                    search[keys] = self.__dict__[keys]
            return search
