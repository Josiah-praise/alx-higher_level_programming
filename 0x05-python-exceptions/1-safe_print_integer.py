#!/usr/bin/python3

def safe_print_integer(value):
    """_summary_

    Args:
        value: any type of value
    Return: True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
