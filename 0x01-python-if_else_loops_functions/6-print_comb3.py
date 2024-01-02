#!/usr/bin/python3

for _ in range(10):
    for i in range(_ + 1, 10):
        if _ != 8 or i != 9:
            print('{}{}'.format(_, i), end=', ')
        else:
            print(_, i, sep='')
