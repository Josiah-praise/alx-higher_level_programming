#!/usr/bin/python3
a = 97
z = 122
for _ in range(a, (z + 1)):
    if chr(_) not in {'q', 'e'}:
        print(chr(_), end='')
