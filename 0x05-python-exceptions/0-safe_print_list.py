#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): list of elements. Defaults to [].
        x (int, optional): number of elements to print. Defaults to 0.
    Return: the real number of elements printed
    """
    count = 0
    try:
        for _ in range(x):
            print(my_list[_], end='')
            count += 1
        print('')
        return count
    except IndexError:
        print('')
        return count
