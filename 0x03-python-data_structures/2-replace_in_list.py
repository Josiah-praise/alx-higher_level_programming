#!/usr/bin/python3

def replace_in_list(my_list: list, idx: int, element) -> list:
    """replaces element at specified index
    :arg
        my_list: list of elements
        idx: index to be replaced
        element: element to be inserted
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
