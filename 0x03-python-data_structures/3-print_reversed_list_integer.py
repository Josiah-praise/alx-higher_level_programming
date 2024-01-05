#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list"""
    for _ in my_list[::-1]:
        print("{:d}".format(_))
