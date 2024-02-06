#!/usr/bin/python3
"""READ file"""


def read_file(filename: str = ""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(file=filename, mode="r", encoding="utf-8") as f_obj:
        lines = f_obj.read()
        print(lines, end="")
