#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print all the names defined by a compiled module"""

    names = dir(hidden_4)

    for name in names:
        if name[:2] != "__":
            print(name)
