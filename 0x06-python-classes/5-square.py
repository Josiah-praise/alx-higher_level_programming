#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """creates a class instance"""
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints # * self.__size"""
        if self.__size:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print()
