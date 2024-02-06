#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    '''
    Returns a list of lists of integers
    representing the Pascal's triangle of n
    '''
    current = [1]
    if n == 0:  # rerturn empty list if is 0
        return [[]]

    def pascal_recursive(list_):
        '''recurcsive solution'''
        new_list = [1]

        if len(list_) == n:  # base call when list contains n elements
            return list_

        nonlocal current  # make current  nonlocal
        current_length = len(current)
        for _ in range(current_length):
            next_ = _ + 1
            if next_ <= current_length - 1:
                new_list.append(current[_] + current[next_])
            else:
                new_list.append(current[_] + 0)
        current = new_list
        list_.append(new_list)
        return pascal_recursive(list_)

    return pascal_recursive([[1]])
