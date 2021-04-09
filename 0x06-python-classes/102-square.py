#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Constructor method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __gt__(self, Square):
        """Method comparative"""
        return self.area() > Square.area()

    def __lt__(self, Square):
        """Method comparative"""
        return self.area() < Square.area()

    def __eq__(self, Square):
        """Method comparative"""
        return self.area() == Square.area()

    def __ge__(self, Square):
        """Method comparative"""
        return self.area() >= Square.area()

    def __le__(self, Square):
        """Method comparative"""
        return self.area() <= Square.area()

    def area(self):
        """Method to calculate the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @size.setter
    def size(self, value=0):
        """Defines size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
