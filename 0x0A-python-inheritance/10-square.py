#!/usr/bin/python3
"""Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square object"""

    def __init__(self, size):
        """Initialize a Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
