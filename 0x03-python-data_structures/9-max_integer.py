#!/usr/bin/python3

def max_integer(my_list=[]):
    """find the biggest integer in the list"""
    if len(my_list) == 0:
        return None
    largest = 0
    for _ in my_list:
        if _ > largest:
            largest = _
    return largest
