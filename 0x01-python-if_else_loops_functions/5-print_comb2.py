#!/usr/bin/python3
for _ in range(0, 99 + 1):
    if _ < 99:
        print('{0:02d}'.format(_), end=', ')
    else:
        print('{0:02d}'.format(_))
