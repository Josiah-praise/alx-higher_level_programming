#!/usr/bin/python3

def fizzbuzz() -> None:
    """
    prints Fizbuzz for every number in the range 1-100(inclusive)
    that is a multiple of 3 and 5, Fizz for those that are multiples
    of 3 and Buzz for those that are multiples of 5
    """
    for _ in range(1, 100 + 1):
        if (_ % 3 == 0) and (_ % 5 == 0):
            print("FizzBuzz", end=' ')
        elif _ % 3 == 0:
            print('Fizz', end=' ')
        elif _ % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(_, end=' ')
