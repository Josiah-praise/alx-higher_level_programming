#!/usr/bin/python3
"""Text indentation"""

def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    flag = True
    _str = ""
    chars = ['.', '?', ':']
    for char in text:
        if flag:
            _str += char
        else:
            if char == " ":
                continue
            else:
                flag = True
                _str = '' + char
        if char in chars:
            print(_str + '\n')
            flag = False
