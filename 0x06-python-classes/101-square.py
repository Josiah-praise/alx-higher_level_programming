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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def __lt__(self, value):
        """implements the < operator"""
        if not isinstance(value, Square):
            raise TypeError(
                "unsupported operand type(s) for <" ":'{}' and '{}'".format(
                    type(self).__name__, type(value).__name__
                )
            )
        return True if self.__size < value.size else False

    def __gt__(self, value):
        """implements the > operator"""
        if not isinstance(value, Square):
            raise TypeError(
                "unsupported operand type(s) for >" ":'{}' and '{}'".format(
                    type(self).__name__, type(value).__name__
                )
            )
        return True if self.__size > value.size else False

    def __eq__(self, value):
        """implements the == operator"""
        if not isinstance(value, Square):
            raise TypeError(
                "unsupported operand type(s) for ==" ":'{}' and '{}'".format(
                    type(self).__name__, type(value).__name__
                )
            )
        return True if self.__size == value.size else False

    def __le__(self, value):
        """implements the <= operator"""
        if not isinstance(value, Square):
            raise TypeError(
                "unsupported operand type(s) for <=" ":'{}' and '{}'".format(
                    type(self).__name__, type(value).__name__
                )
            )
        return True if self.__size <= value.size else False

    def __ge__(self, value):
        """implements the >= operator"""
        if not isinstance(value, Square):
            raise TypeError(
                "unsupported operand type(s) for >=" ":'{}' and '{}'".format(
                    type(self).__name__, type(value).__name__
                )
            )
        return True if self.__size >= value.size else False


s1 = Square(4)
s2 = Square(4.4)
print(s1 < s2, "s1:{}, s2:{}".format(s1.size, s2.size))

print(s1 > "tyu", "s1:{}, s2:{}".format(s1.size, s2.size))
