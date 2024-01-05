#!/usr/bin/python3

def element_at(my_list, idx):
    """retrieves element at index from my list
    :arg
        mylist: list of elements
        idx: index of element to be retrieved
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
