#!/usr/bin/python3

def reverse_print() -> None:
    """prints the alphabets in reverse"""
    for _ in range(122, 96, -1):
        if _ % 2 == 0:
            print(chr(_), end='')
        else:
            print(chr(_-32), end='')


if __name__ == '__main__':
    reverse_print()
