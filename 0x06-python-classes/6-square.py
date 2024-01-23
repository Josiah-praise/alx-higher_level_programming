#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """creates a class instance"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        self.__validate_position(value)
        self.__position = value

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int) or value is None:
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
                prefix = self.__position[0] * ' '
                suffix = self.__size * '#'
                print('{}{}'.format(prefix, suffix))
        else:
            print()

    def __validate_position(self, _tuple: tuple) -> bool:
        """checks if a tuple is of len 2 and
        both elements are positive"""
        if _tuple is None:
            raise TypeError("must be a tuple of 2 positive integers")

        if not isinstance(_tuple, tuple) or len(_tuple) != 2:
            raise TypeError("must be a tuple of 2 positive integers")

        a, b = _tuple
        if a < 0 or b < 0:
            raise TypeError("must be a tuple of 2 positive integers")
        return True
