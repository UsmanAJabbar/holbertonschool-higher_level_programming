#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, __size = None):
        """
        Method that initializes the class and checks
        for good input
        Args:
            self: refers back to the class
            size: default = 0, else defined input
        """    
        self.__size = __size
