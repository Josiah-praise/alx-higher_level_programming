#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    return {x: y*2 for x, y in a_dictionary.items()}
