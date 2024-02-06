#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age) -> None:
        """Contructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of instance attributes"""

        if attrs is not None and all(isinstance(_, str) for _ in attrs):
            dict__ = dict()
            for attribute in attrs:
                if attribute in self.__dict__:
                    dict__[attribute] = self.__dict__[attribute]
            return dict__
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
