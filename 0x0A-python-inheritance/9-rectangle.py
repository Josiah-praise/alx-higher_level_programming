#!/usr/bin/python3
'''Full rectangle'''

Baseclass = __import__('7-base_geometry').BaseGeometry


class Rectangle(Baseclass):
    '''Rectangle class'''

    def __init__(self, width, height):
        '''creates an instance'''

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''calculate the area of a rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''string representation'''
        return f"[Rectangle] {self.__width}/{self.__height}"
