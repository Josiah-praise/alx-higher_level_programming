#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """writes text to filename"""
    with open(filename, "w", encoding="utf-8") as file_stream:
        return file_stream.write(text)
