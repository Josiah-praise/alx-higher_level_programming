#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers
    tuple (<score>, <weight>)"""
    if not my_list:
        return 0

    def mul_tuply(my_tuple):
        """multiply all elements in a tuple"""
        product = 1
        for _ in my_tuple:
            product *= _
        return product

    def divisor(my_list):
        """adds all the last values in the tuple"""
        return sum(_[-1] for _ in my_list)

    multiples_of_tuple = sum(mul_tuply(_) for _ in my_list)

    return multiples_of_tuple/divisor(my_list)
