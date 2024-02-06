#!/usr/bin/python3
"""Load, add, save"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_filename = "add.json"
json_list = []

if len(argv) == 1:
    save_to_json_file(json_list, json_filename)
else:
    try:
        json_list = load_from_json_file(json_filename)
    except Exception as E:
        save_to_json_file(json_list, json_filename)

    for _ in range(1, len(argv)):
        json_list.append(argv[_])
    save_to_json_file(json_list, json_filename)
