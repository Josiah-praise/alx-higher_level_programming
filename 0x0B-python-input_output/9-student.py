#!/usr/bin/python3
"""Student to Json"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age) -> None:
        """Contructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of instance attributes"""
        return self.__dict__
