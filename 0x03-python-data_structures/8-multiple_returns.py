#!/usr/bin/python3

def multiple_returns(sentence: str) -> tuple:
    """returns a tuple with the length
    of a string and it's first character
    """
    length = len(sentence)
    return (length, None) if length == 0 else (length, sentence[0])
