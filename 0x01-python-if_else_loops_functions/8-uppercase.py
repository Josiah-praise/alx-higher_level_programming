#!/usr/bin/python3

def uppercase(str: str) -> None:
    """converts to uppercase """
    for _ in str:
        print('{}'.format(chr(ord(_)-32)), end='')
    print('')


uppercase("holberton")
