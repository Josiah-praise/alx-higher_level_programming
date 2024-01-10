#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary with keys sorted in alphabetical order."""
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f'{key}: {value}')
