#!/usr/bin/python3
'''Rectangle'''


Baseclass = __import__('7-base_geometry').BaseGeometry


class Rectangle(Baseclass):
    '''Rectangle class'''

    def __init__(self, width, height):
        '''creates an instance'''

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
