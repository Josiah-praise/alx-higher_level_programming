#!/usr/bin/python3
def square(my_list):
    """square the elements of a list"""
    return list(map(lambda x: x*x, my_list))


def square_matrix_simple(matrix_2d):
    """square the elements of a 2d matrix"""
    return list(map(square, matrix_2d))
