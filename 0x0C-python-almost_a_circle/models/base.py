#!/usr/bin/python3
"""
Module containing class Base
"""

import json


class Base:
    """ class Base; tracks id """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_objs to a file """
        list_obj = []
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(filename, mode='w', encoding="utf-8") as f:
                f.write(cls.to_json_string(list_obj))
        else:
            for obj in list_objs:
                list_obj.append(cls.to_dictionary(obj))
            with open(filename, mode='w', encoding='utf-8') as f:
                f.write(cls.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        json_list = []
        if json_string is None:
            return json_list
        if len(json_string) == 0:
            return json_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy_cls = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy_cls = cls(1, 1)
        dummy_cls.update(**dictionary)
        return dummy_cls

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        json_list = []
        instance_list = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
            for element in json_list:
                instance_list.append(cls.create(**element))
            return instance_list
        except FileNotFoundError:
            return json_list

 @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
