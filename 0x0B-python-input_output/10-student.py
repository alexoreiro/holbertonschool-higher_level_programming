#!/usr/bin/python3

# Class Student

class Student:
    # Defines class Student 
    def __init__(self, first_name, last_name, age):
        # initiates attributes for student instance 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # json function
        if attrs is not None:
            new_dict = {}
            for obj in attrs:
                if type(obj) != str:
                    return self.__dict__
            for obj in attrs:
                if obj in self.__dict__:
                    new_dict[obj] = self.__dict__[obj]
            return new_dict
        else:
            return self.__dict__
