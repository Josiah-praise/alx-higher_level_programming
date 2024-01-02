#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 0
    sum = 0
    if len(argv) == 1:
        print(sum)
    else:
        for _ in argv:
            if count != 0:
                sum += int(_)
            count += 1
        print(sum)
