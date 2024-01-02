#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    func_list = [(add, '+'), (sub, '-'), (mul, '*'), (div, '/')]
    a = 10
    b = 5
    for func, sign in func_list:
        print("{0} {1} {2} = {3}".format(a, sign, b, func(a, b)))
