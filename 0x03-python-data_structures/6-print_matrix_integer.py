#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""

    for _, value in enumerate(matrix):
        if not value:
            print('')
            continue
        for i, element in enumerate(matrix[_]):
            if i == (len(matrix[_]) - 1):
                print("{:d}".format(element))
                continue
            print("{:d}".format(element), end=' ')
