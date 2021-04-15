#!/usr/bin/python3

class MyInt(int):
   
    def __init__(self, value):
       
        self.value = value

    def __eq__(self, value):
        return self.value != value

    def __ne__(self, value):
        return self.value == value
