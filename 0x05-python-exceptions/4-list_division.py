#!/bin/usr/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists"""
    new_list = []
    for idx in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(quotient)
    return new_list
