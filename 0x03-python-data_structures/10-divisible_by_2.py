#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""

    newList = []
    for _ in my_list:
        if _ % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
