#!/usr/bin/python3
"""Square class with size validation"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """creates a class instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
