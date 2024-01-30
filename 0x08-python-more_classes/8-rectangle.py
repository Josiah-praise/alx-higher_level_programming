#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width: int = 0, height: int = 0) -> bool:
        """create a rectangle instance"""
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value: int) -> bool:
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value: int) -> bool:
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """calculates the area"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """calculates the perimeter"""
        return 0 if self.__width == 0\
            or self.__height == 0 else 2 * (self.__width + self.__height)

    def __display_rectangle(self) -> bool:
        """displays the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            print('', end='')
            return None
        for _ in range(self.__height):
            if _ < self.height - 1:
                print(f'{self.print_symbol}' * self.__width)
            else:
                print(f'{self.print_symbol}' * self.__width, end="")

    def __str__(self) -> str:
        """returns string representation"""
        self.__display_rectangle()
        return ''

    def __repr__(self) -> str:
        """return a fromal string representation"""
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self) -> bool:
        """delete a rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() == rect_1.area():
            return rect_1

        return rect_1 if rect_1.area() > rect_2.area() else rect_2
