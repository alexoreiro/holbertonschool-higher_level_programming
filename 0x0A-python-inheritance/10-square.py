#!/usr/bin/python3
"""
Class Square (inherits from Rectangle)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size):
        """ instantiation of a square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
