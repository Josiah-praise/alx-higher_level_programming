#!/usr/bin/python3

def remove_char_at(str: str, n: int) -> str:
    """removes the character at index n"""
    new_str = ''
    count = 0
    for _ in str:
        count += 1
        if count - 1 != n:
            new_str += _
    return new_str
