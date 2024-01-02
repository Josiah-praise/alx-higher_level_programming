#!/usr/bin/python3

def print_last_digit(number: int) -> int:
    """print last digit"""
    last_digit = number % 10
    dig = -last_digit + 10 if number < 0 else last_digit
    print(dig, end='')
    return(dig)
