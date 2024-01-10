#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    score = 0
    student = None
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            student = key
    return student
