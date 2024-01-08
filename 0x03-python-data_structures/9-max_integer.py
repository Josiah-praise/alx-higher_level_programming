#!/usr/bin/python3

def max_integer(my_list=[]):
    """find the biggest integer in the list"""

    if not my_list:
        return None
    largest = 0
    for _ in my_list:
        if _ > largest:
            largest = _
    return largest
