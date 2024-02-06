#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-*") as file_stream:
        return file_stream.write(text)
