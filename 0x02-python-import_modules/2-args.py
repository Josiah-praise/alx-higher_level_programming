#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    if argc == 1:
        print('{0} arguments.'.format(argc - 1))
    elif argc == 2:
        print('{0} argument:'.format(argc - 1))
    elif argc > 2:
        print('{0} arguments:'.format(argc - 1))

    count = 1
    if argc > 1:
        for _ in argv:
            if count < argc:
                print('{0}: {1}'.format(count, argv[count]))
                count += 1
