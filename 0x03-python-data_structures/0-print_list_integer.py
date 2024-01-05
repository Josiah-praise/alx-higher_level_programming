#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    prints all integers in a list
    :param my_list: list of intgers
    """
    for _ in my_list:
        print("{:d}".format(_))
