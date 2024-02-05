#!/usr/bin/python3
"""My list"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
