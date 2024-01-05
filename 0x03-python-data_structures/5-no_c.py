#!/usr/bin/python3

def no_c(my_string: str) -> str:
    """remove c and C from string"""
    new = ''.join(_ for _ in my_string if _ not in ['c', 'C'])
    return new
