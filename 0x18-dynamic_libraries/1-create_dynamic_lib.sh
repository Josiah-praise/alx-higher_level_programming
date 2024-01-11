#!/bin/bash
gcc -Wall -Werror -pedantic -std=gnu89 -Wextra -c *.c -fpic
gcc *.o -shared -o liball.so
