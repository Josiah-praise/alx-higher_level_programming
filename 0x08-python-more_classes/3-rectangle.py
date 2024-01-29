#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """create a rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter"""
        return 0 if self.__width == 0\
            or self.__height == 0 else 2 * (self.__width + self.__height)

    def __display_rectangle(self):
        """displays the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            print('', end='')
        for _ in range(self.__height):
            if _ < self.height - 1:
                print('#' * self.__width)
            else:
                print('#' * self.__width, end="")

    def __str__(self):
        """returns string representation"""
        self.__display_rectangle()
        return ''
