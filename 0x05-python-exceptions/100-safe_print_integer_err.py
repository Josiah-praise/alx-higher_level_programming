#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """prints an integer"""
    _val = False
    try:
        print("{:d}".format(value))
        _val = True
    except Exception as exc:
        print(f"Exception: {exc}", file=sys.stderr)
    finally:
        return _val
