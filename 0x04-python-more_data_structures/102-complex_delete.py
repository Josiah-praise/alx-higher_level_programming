#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ deletes keys with a specific value in a dictionary"""
    keys = [key for key, _value in a_dictionary.items() if value == _value]
    print(keys)
    map(lambda x: a_dictionary.pop(x), keys)
    return a_dictionary
