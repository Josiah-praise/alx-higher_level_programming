#!/usr/bin/python3
from calculator import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    """Perform calculations on the inputs"""

    errorMessage = 'Unknown operator. Available operators: +, -, * and /'
    hint = 'Usage: ./100-my_calculator.py <a> <operator> <b>'
    argc = len(argv)
    operators = [('+', add), ('-', sub), ('/', div), ('*', mul)]

    if (argc - 1) != 3:
        print('{:s}'.format(hint))
        exit(1)

    for _ in operators:
        if argv[2] in _:
            ans = _[1](int(argv[1]), int(argv[3]))
            print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], ans))
            exit(0)
    print('{}'.format(errorMessage))
    exit(1)
