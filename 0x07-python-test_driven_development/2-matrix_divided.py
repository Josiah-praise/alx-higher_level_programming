#!/usr/bin/python3
"""Divide a matrix"""

def __check_float_int_list(matrix):
    """checks if matrix is a list of lists of floats or integers"""
    error = TypeError("matrix must be" \
    " a matrix (list of  lists) of integers/floats")
    # check if matrix contains only lists
    if matrix is None:
        raise error
    if not all(isinstance(_, list) for _ in matrix):
        raise error

    for _ in matrix: #traverse the matrix
        for value in _: #traverse the inner list
            if not isinstance(value, (int, float)):
                raise error

def __check_matrix_size(matrix):
    """checks if the rows are of the same size"""
    length = {len(_) for _ in matrix}
    if len(length) != 1:
        raise TypeError("Each row of the matrix must have the same size")

def __check_div(div):
    """check if div is an int or a float"""
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

def __check_zero_division(div):
    """check if div is 0"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

def matrix_divided(matrix, div) -> list:
    """divides all elements of a matrix"""
    __check_float_int_list(matrix)
    __check_matrix_size(matrix)
    __check_div(div)
    __check_zero_division(div)
    return [[round((_/div), 2) for _ in list_] for list_ in matrix]
